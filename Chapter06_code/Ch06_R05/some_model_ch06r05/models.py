# coding: utf-8

from openerp import models, api, fields


class LibraryReturnsWizard(models.TransientModel):
    _name = 'library.returns.wizard'

    member_id = fields.Many2one('library.member', 'Member')
    book_ids = fields.Many2many('library.book', 'Books')

    @api.multi
    def record_returns(self):
        loan = self.env['library.book.loan']
        for rec in self:
            loans = loan.search(
                [('state', '=', 'ongoing'),
                 ('book_id', 'in', self.book_ids.ids),
                 ('member_id', '=', self.member_id.id)]
            )
            loans.write({'state': 'done'})

    @api.onchange('member_id')
    def onchange_member(self):
        loan = self.env['library.book.loan']
        loans = loan.search(
            [('state', '=', 'ongoing'),
             ('member_id', '=', self.member_id.id)]
        )
        self.book_ids = loans.mapped('book_id')
