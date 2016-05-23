# coding: utf-8

from openerp import models, api


class LibraryBook(models.Model):
    _inherit = 'library.book'

    @api.model
    def get_all_library_members(self):
        library_member_model = self.env['library.member']
        return library_member_model.search([])
