# -*- coding: utf-8 -*-
from openerp import models, fields
from openerp.addons import decimal_precision as dp


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    cost_price = fields.Float(
        'Book Cost', dp.get_precision('Book Price'))
