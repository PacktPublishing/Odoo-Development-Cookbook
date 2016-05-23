# -*- coding: utf-8 -*-
from openerp import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    short_name = fields.Char(
        string='Short Title',
        size=100,  # For Char only
        translate=False,  # also for Text fields
        )

    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('avaiable', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html(
        'Description',
        # optional:
        sanitize=True,
        strip_style=False,
        )
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    reader_rating = fields.Float(
        'Reader Average Rating',
        (14, 4),  # Optional precision (total, decimals)
        )

    pages = fields.Integer(
        string='Number of Pages',
        default=0,
        help='Total book page count',
        groups='base.group_user',
        states={'cancel': [('readonly', True)]},
        copy=True,
        index=False,
        readonly=False,
        required=False,
        company_dependent=False,
        )
