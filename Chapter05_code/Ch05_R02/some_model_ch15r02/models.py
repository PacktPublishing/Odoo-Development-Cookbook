# coding: utf-8

import os

from openerp import models, fields, api
from openerp.exceptions import UserError


class SomeModel(models.Model):
    _name = 'some.model'

    data = fields.Text('Data')

    @api.multi
    def save(self, filename):
        if '/' in filename or '\\' in filename:
            raise UserError('Illegal filename %s' % filename)
        path = os.path.join('/opt/exports', filename)
        try:
            with open(path, 'w') as fobj:
                for record in self:
                    fobj.write(record.data)
                    fobj.write('\n')
        except (IOError, OSError) as exc:
            message = 'Unable to save file: %s' % exc
            raise UserError(message)
