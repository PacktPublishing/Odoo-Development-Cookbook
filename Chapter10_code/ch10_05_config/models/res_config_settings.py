# -*- coding: utf-8 -*-
from openerp import models, fields


class ConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'
    group_release_dates = fields.Boolean(
            "Manage book release dates",
            group='base.group_user',
            implied_group='ch10_05_config.group_release_dates')
    module_note = fields.Boolean("Install Notes app")
