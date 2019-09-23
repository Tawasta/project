# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectProject(models.Model):

    # 1. Private attributes
    _inherit = 'project.project'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        """ Default stages for projects' that contain tasks """
        project = super(ProjectProject, self).create(vals)
        if vals.get('use_tasks') and (not vals.get('type_ids') or
                                      len(vals.get('type_ids')[0][2]) == 0):
            task_stages = self.env['project.task.type'].sudo().search([
                ('task_stage', '=', True),
            ])
            project.type_ids = [(6, 0, task_stages.ids)]
        return project

    # 7. Action methods

    # 8. Business methods
