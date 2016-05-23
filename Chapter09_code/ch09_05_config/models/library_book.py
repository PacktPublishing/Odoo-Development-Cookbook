# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date(
        'Release Date', 
        groups='ch09_05_config.group_release_dates')
    author_ids = fields.Many2many('res.partner', string='Authors')
