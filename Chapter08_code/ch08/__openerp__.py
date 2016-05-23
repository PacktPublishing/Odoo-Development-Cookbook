# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Odoo cookbook - Chapter 8",
    "version": "9.0.1.0.0",
    "author": "Odoo cookbook",
    "license": "AGPL-3",
    "category": "Odoo cookbook",
    "summary": "All the code from chapter 7",
    "depends": [
        'base',
        # that's for the later recipes
        'project',
    ],
    "data": [
        "views/add_a_menu_item_and_window_action.xml",
        "views/have_an_action_open_a_specific_view.xml",
        "views/adding_content_and_widgets_to_a_form_view.xml",
        "views/passing_parameters_to_forms_and_actions_context.xml",
        "views/defining_filters_on_record_lists_domain.xml",
        "views/list_views.xml",
        "views/search_views.xml",
        "views/changing_existing_views_view_inheritance.xml",
        "views/kanban_views.xml",
        "views/calendar_and_gantt_views.xml",
        "views/graph_and_pivot_views.xml",
        "views/qweb_reports.xml",
        "views/server_actions.xml",
    ],
}
