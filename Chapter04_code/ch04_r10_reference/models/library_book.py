# -*- coding: utf-8 -*-
from openerp import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    @api.model
    def _referencable_models(self):
        models = self.env['res.request.link'].search([])
        return [(x.object, x.name) for x in models]

    ref_doc_id = fields.Reference(
        selection=_referencable_models,
        string='Reference Document')

