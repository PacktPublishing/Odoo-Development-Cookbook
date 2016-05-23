# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
        )

    author_ids = fields.Many2many(
        'res.partner', string='Authors')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    book_ids = fields.One2many(
        'library.book', 'publisher_id',
        string='Published Books')

    book_ids = fields.Many2many(
        'library.book',
        string='Authored Books',
        # relation='library_book_res_partner_rel'  # optional
        )
