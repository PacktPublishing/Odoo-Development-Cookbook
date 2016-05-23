# coding: utf-8

from openerp import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def partners_by_country(self):
        sql = ('SELECT country_id, array_agg(id) '
               'FROM res_partner '
               'WHERE active=true AND country_id IS NOT NULL '
               'GROUP BY country_id')
        self.env.cr.execute(sql)
        result = {}
        for country_id, partner_ids in self.env.cr.fetchall():
            country = self.country_id.browse(country_id)
            partners = self.browse(partner_ids)
            result[country] = partners
        return result
