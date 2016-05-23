# coding: utf-8

from openerp import models, api, fields


class LibraryBookLoan(models.Model):
    _name = 'library.book.loan'
    book_id = fields.Many2one('library.book', 'Book', required=True)
    member_id = fields.Many2one('library.member', 'Borrower',
                                required=True)
    state = fields.Selection([('ongoing', 'Ongoing'),
                              ('done', 'Done')],
                             'State',
                             default='ongoing', require=True)


class LibraryLoanWizard(models.TransientModel):
    _name = 'library.loan.wizard'
    member_id = fields.Many2one('library.member', 'Member')
    book_ids = fields.Many2many('library.book', 'Books')

    @api.multi
    def record_loans(self):
        for wizard in self:
            member = wizard.member_id
            loan = self.env['library.book.loan']
            for book in wizard.book_ids:
                loan.create({'member_id': member.id,
                             'book_id': book.id})
