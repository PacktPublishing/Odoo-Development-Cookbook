# coding: utf-8

from openerp import models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.multi
    def update_phone_number(self, new_number):
        self.ensure_one()
        company_as_superuser = self.sudo()
        company_as_superuser.phone = new_number
