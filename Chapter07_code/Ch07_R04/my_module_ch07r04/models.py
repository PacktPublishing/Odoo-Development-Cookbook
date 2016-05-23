# coding: utf-8

from openerp import models, api, fields


class LibraryBook(models.Model):
    _inherit = 'library.book'

    state = fields.Selection([('draft', 'Unavailable'),
                              ('available', 'Available'),
                              ('borrowed', 'Borrowed'),
                              ('lost', 'Lost')],
                             'State')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue
