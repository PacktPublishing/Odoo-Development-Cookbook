# coding: utf-8

from openerp import models, api, fields
from openerp.exceptions import UserError


class LibraryBook(models.Model):
    _inherit = 'library.book'
    manager_remarks = fields.Text('Manager Remarks')

    @api.model
    @api.returns(lambda rec: rec.id)
    def create(self, values):
        if not self.user_has_groups('library.group_library_manager'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to modify manager_remarks'
                )
        return super(LibraryBook, self).create(values)

    @api.multi
    def write(self, values):
        if not self.user_has_groups('library.group_library_manager'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to modify manager_remarks'
                )
        return super(LibraryBook, self).write(values)

    @api.model
    def fields_get(self,
                   allfields=None,
                   write_access=True,
                   attributes=None):
        fields = super(LibraryBook, self).fields_get(
            allfields=allfields,
            write_access=write_access,
            attributes=attributes
        )
        if not self.user_has_groups('library.group_library_manager'):
            if 'manager_remarks' in fields:
                fields['manager_remarks']['readonly'] = True
