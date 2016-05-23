# coding: utf-8

from openerp import models, api, fields


class LibraryMember(models.Model):
    _name = 'library.member'

    @api.multi
    def return_all_books(self):
        self.ensure_one
        wizard = self.env['library.returns.wizard']
        values = {'member_id': self.id}
        specs = wizard._onchange_spec()
        updates = wizard.onchange(values, ['member_id'], specs)
        values.update(updates.get('value', {}))
        record = wizard.create(values)
