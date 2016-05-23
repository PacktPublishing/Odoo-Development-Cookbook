# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import werkzeug
from openerp import api, fields, models
from openerp.http import request


class ModelNameSearchConverter(werkzeug.routing.BaseConverter):
    def __init__(self, url_map, model):
        super(ModelNameSearchConverter, self).__init__(url_map)
        self.model = model
        self.regex = r'((\w|\+)+)'

    def to_python(self, value):
        result = request.env[self.model].browse(
            map(lambda x: x[0], request.env[self.model].sudo().name_search(
                value.replace('+', ' '), operator='=ilike', limit=1)))
        if not result:
            raise werkzeug.exceptions.NotFound()
        return result

    def to_url(self, value):
        return value.name_get()[1].replace(' ', '+')


class IrHttp(models.Model):
    _inherit = 'ir.http'

    def _get_converters(self):
        result = super(IrHttp, self)._get_converters()
        result['model_name'] = ModelNameSearchConverter
        return result
