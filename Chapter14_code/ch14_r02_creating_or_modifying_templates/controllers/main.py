# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.http import request


class Main(http.Controller):
    @http.route('/books', type='http', auth="user", website=True)
    def route(self):
        return request.render(
            'ch14_r02_creating_or_modifying_templates.books',
            {
                'books': request.env['library.book'].search([]),
            })
