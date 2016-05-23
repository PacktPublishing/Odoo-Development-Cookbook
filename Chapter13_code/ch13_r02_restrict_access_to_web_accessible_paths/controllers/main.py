# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.http import request


class Main(http.Controller):
    @http.route('/my_module/all-books', type='http', auth='none')
    def all_books(self):
        records = request.env['library.book'].sudo().search([])
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>'.join(records.mapped('name'))
        result += '</td></tr></table></body></html>'
        return result

    @http.route('/my_module/all-books/mark_mine', type='http', auth='public')
    def all_books_mark_mine(self):
        records = request.env['library.book'].sudo().search([])
        result = '<html><body><table>'
        for record in records:
            result += '<tr>'
            if record.author_ids & request.env.user.partner_id:
                result += '<th>'
            else:
                result += '<td>'
            result += record.name
            if record.author_ids & request.env.user.partner_id:
                result += '</th>'
            else:
                result += '</td>'
            result += '</tr>'
        result += '</table></body></html>'
        return result

    @http.route('/my_module/all-books/mine', type='http', auth='user')
    def all_books_mine(self):
        records = request.env['library.book'].search([
            ('author_ids', 'in', request.env.user.partner_id.ids),
        ])
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>'.join(records.mapped('name'))
        result += '</td></tr></table></body></html>'
        return result

    @http.route('/my_module/all-books/mine_base_group_user', type='http',
                auth='base_group_user')
    def all_books_mine_base_group_user(self):
        return self.all_books_mine()

    # this is for the exercise
    @http.route('/my_module/all-books/mine_groups', type='http',
                auth='groups(base.group_no_one)')
    def all_books_mine_groups(self):
        return self.all_books_mine()
