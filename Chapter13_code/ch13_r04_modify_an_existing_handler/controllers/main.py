# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.addons.website.controllers.main import Website


class Website(Website):
    @http.route()
    def website_info(self):
        result = super(Website, self).website_info()
        result.qcontext['apps'] = result.qcontext['apps'].filtered(
            'website')
        return result
