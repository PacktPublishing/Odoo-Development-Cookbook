# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import exceptions, http, models
from openerp.http import request


class IrHttp(models.Model):
    _inherit = 'ir.http'

    def _auth_method_base_group_user(self):
        self._auth_method_user()
        if not request.env.user.has_group('base.group_user'):
            raise exceptions.AccessDenied()

    # this is for the exercise
    def _auth_method_groups(self, group_xmlids=None):
        self._auth_method_user()
        if not any(map(request.env.user.has_group, group_xmlids or [])):
            raise exceptions.AccessDenied()

    def __getattr__(self, name):
        if name.startswith('_auth_method_groups(') and name.endswith(')'):
            return lambda: self._auth_method_groups(
                map(str.strip, name[7:-1].split(',')))
        return self.__getattribute__(name)
