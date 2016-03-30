# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:



class ProjectProject(models.Model):
    
    # 1. Private attributes
    _inherit = 'project.project'

    # 2. Fields declaration
    note_ids = fields.One2many(
        "project.project.note",
        'project_id',
        'Project notes'
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    





class ProjectNote(models.Model):
    
    # 1. Private attributes
    _name = 'project.project.note'

    # 2. Fields declaration
    name = fields.Char("Title", size=256)
    note = fields.Text("Note")
    project_id = fields.Many2one("project.project", "Project")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    