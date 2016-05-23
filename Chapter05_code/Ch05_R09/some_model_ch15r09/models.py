# coding: utf-8

from openerp import models, api


class SomeModel(models.Model):
    _name = 'some.model'

    @api.model
    def get_email_addresses(self, partner):
        partner.ensure_one()
        return partner.mapped('child_ids.email')

    @api.model
    def get_companies(self, partners):
        return partners.mapped('parent_id')
