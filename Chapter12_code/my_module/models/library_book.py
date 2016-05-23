# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread']
    name = fields.Char('Title', required=True, track_visibility=True)
    date_release = fields.Date('Release Date', track_visibility=True)
    author_ids = fields.Many2many('res.partner', string='Authors')

    def _track_subtype(self, init_values):
        if 'date_release' in init_values:
            return 'mail.mt_comment'
        return False
