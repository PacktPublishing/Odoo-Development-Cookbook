# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.http import request


class Main(http.Controller):
    @http.route('/my_module/book_details', type='http', auth='none')
    def book_details(self, book_id):
        record = request.env['library.book'].sudo().browse(int(book_id))
        return '<html><body><h1>%s</h1>Authors: %s' % (
            record.name,
            ', '.join(record.author_ids.mapped('name')) or 'none',
        )

    @http.route("/my_module/book_details/<model('library.book'):book>",
                type='http', auth='none')
    def book_details_in_path(self, book):
        return self.book_details(book.id)

    # this is for the exercise
    @http.route("/my_module/book_details/<model_name('library.book'):book>",
                type='http', auth='user')
    def book_details_in_path_name(self, book):
        return self.book_details(book.id)
