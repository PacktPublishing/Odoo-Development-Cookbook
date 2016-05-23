# coding: utf-8

from openerp import models, api, fields


class SomeModel(models.Model):
    _inherit = 'some.model'

    @api.model
    def partners_with_email(self, partners):
        def predicate(partner):
            if partner.email:
                return True
            return False
        return partners.filter(predicate)

    @api.model
    def partners_with_email_variant(self, partners):
        return partners.filter(lambda p: p.email)

    @api.model
    def partners_with_email_variant2(self, partners):
        return partners.filter('email')
