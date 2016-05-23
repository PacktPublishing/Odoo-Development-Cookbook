# coding: utf-8

from openerp import models, api


class SomeModel(models.Model):
    _name = 'some.model'

    @api.model
    def find_partners_and_contacts(self, name):
        partner = self.env['res.partner']
        domain = ['|',
                  '&',
                  ('is_company', '=', True),
                  ('name', 'like', name),
                  '&',
                  ('is_company', '=', False),
                  ('parent_id.name', 'like', name)
                  ]
        return partner.search(domain)
