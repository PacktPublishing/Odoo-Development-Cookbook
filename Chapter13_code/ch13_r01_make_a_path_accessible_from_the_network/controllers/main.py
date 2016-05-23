# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# import email
# import datetime
# from openerp import fields
from openerp import http
from openerp.http import request


class Main(http.Controller):
    @http.route('/my_module/books', type='http', auth='none')
    def books(self):
        records = request.env['library.book'].sudo().search([])
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>'.join(records.mapped('name'))
        result += '</td></tr></table></body></html>'
        # return request.make_response(
        #     result, [
        #         ('Last-modified', email.utils.formatdate(
        #             (
        #                 fields.Datetime.from_string(
        #                 request.env['library.book'].sudo()
        #                 .search([], order='write_date desc', limit=1)
        #                 .write_date) -
        #                 datetime.datetime(1970, 1, 1)
        #             ).total_seconds(),
        #             usegmt=True)),
        #     ])
        return result

    # test this with
    # curl -i -X POST -H "Content-Type: application/json" -d {} $URL
    @http.route('/my_module/books/json', type='json', auth='none')
    def books_json(self):
        records = request.env['library.book'].sudo().search([])
        return records.read(['name'])
