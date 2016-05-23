# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    publisher_id = fields.Many2one(
        'res.partner', string='Publisher')

    publisher_city = fields.Char(
        'Publisher City',
        related='publisher_id.city')
