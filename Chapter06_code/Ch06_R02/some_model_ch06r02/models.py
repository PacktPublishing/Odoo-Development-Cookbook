# coding: utf-8

from openerp import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def stock_in_location(self, location):
        product_in_loc = self.with_context(
            location=location.id,
            active_test=False
        )
        all_products = product_in_loc.search([])
        stock_levels = []
        for product in all_products:
            if product.qty_available:
                stock_levels.append((product.name,
                                     product.qty_available))
        return stock_levels
