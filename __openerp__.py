# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: 
#    Copyright 2015 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html.
#
##############################################################################

{
    'name': 'Project feed',
    'description': """

        Module for project events feed.

    """,
    'version': '8.0.0.1.4',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'depends': [
        'project', 
        'link_many2one_clickable',
        'hr_timesheet_task'
    ],
    'data': [
        'views/project_feed_view.xml'
    ],
    'installable': True,
    'auto-install': False,
    
}
