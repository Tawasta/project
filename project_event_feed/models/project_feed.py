# -*- coding: utf-8 -*-

# 1. Standard library imports:
from datetime import datetime, timedelta
# 2. Known third party imports:
import re
# 3. Odoo imports (openerp):
from openerp import api, fields, models, tools, _
from openerp.addons.mail.mail_message import MLStripper


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

class ProjectFeed(models.Model):
    # 1. Private attributes
    _inherit = 'project.project'

    # 2. Fields declaration
    event_lines = fields.One2many(
        'project.event.line',
        'project_id',
        string='Event lines',
        compute='compute_event_lines'
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_event_lines(self):

        # Clear duplicates of table
        self._cr.execute('truncate table project_event_line')

        # Get the project_task_works and order them ASC by create_date
        # Secondary order by with id ASC is for multiple records done with one save
        task_works = self.env['account.analytic.line'].search(
            [('task_id', 'in', self.tasks.ids)], order='write_date ASC, create_date ASC, id ASC')

        # Get tasks messages and order them DESC by write_date
        messages = self.env['mail.message'].search(
            [('res_id', 'in', self.tasks.ids), ('model', '=', 'project.task')], order='write_date ASC, create_date ASC, id DESC')

        # Initialize time_used for every task, task id used as key
        time_used = {}

        for task in self.tasks:
            time_used[task.id] = 0.0

        for work in task_works:

            info = _("Added hours: ") + work.name
            time_used[work.task_id.id] += work.unit_amount

            self.event_lines += self.event_lines.create({
                'task_id': work.task_id.id,
                'name': info,
                'unit_amount': work.unit_amount,
                'time_left': work.task_id.planned_hours - time_used[work.task_id.id],
                'date': work.write_date,
                'user_id': work.user_id.id,
                'project_id': self.id
            })

        for message in messages:

            # If message has subject, set is as infotext
            if message.subject:
                info = message.subject
            else:
                info = message.subtype_id.name or _("Task Continued")
                subtype_id = self.env['mail.message.subtype'].sudo().with_context(
                    lang= False).search(
                    [('res_model', '=', 'project.task'), ('name', '=', 'Task Assigned')]
                )

                # Find from message.body the assigned to and stage changed
                if len(re.findall("[:]([^<]+)", message.body)) == 1:
                    extra = re.search("[:]([^<]+)", message.body)
                    info += extra.group()
                elif len(re.findall("[:]([^<]+)", message.body)) == 6 and subtype_id and message.parent_id:
                    extra = re.findall("[:]([^<]+)", message.body)
                    info += ": " + extra[1]

            self.event_lines += self.event_lines.create({
                'task_id': message.res_id,
                'name': info,
                'unit_amount': 0,
                'time_left': 0,
                'date': message.write_date,
                'user_id': message.create_uid.id,
                'project_id': self.id
            })

        self.event_lines = self.event_lines.sorted(key=lambda event: event.date, reverse=True)

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
