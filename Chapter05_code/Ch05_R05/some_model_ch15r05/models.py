# coding: utf-8

from openerp import models, api, fields


class SomeModel(models.Model):
    _name = 'some.model'

    @api.model
    def add_contact(self, partner, contacts):
        partner.ensure_one()
        if contacts:
            partner.date = fields.Date.context_today()
            partner.child_ids |= contacts

    @api.model
    def add_contacts_option2(self, partner, contacts):
        partner.ensure_one()
        if contacts:
            today = fields.Date.context_today()
            partner.update(
                {'date': fields.Date.to_string(today),
                 'child_ids': partner.child_ids | contacts}
            )
