# -*- coding: utf-8 -*-
from openerp import models, fields
from openerp import api


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'
    authored_book_ids = fields.Many2many(
        'library.book', string='Authored Books')
    count_books = fields.Integer(
        'Number of Authored Books',
        compute='_compute_count_books'
        )

    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)
