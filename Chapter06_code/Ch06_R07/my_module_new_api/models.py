from datetime import date, timedelta
from openerp import models, fields, api, exceptions
from openerp.tools import _


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char('Name', required=True)
    author_ids = field.Many2many('res.partner')


class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner',
                                 'Partner',
                                 required=True)
    loan_duration = fields.Integer('Loan duration',
                                   default=10,
                                   required=True)
    date_start = fields.Date('Member since')
    date_end = fields.Date('Expiration date')
    number = fields.Char('Number', required=True)

    @api.multi
    def borrow_books(self, book_ids):
        if len(self) != 1:
            raise exceptions.UserError(
                _('It is forbidden to loan the same books '
                  'to multiple members.')
            )
        loan_model = self.env['library.book.loan']
        for book in self.env['library.book'].browse(book_ids):
            val = self._prepare_loan(book)
            loan = loan_model.create(val)

    @api.multi
    def _prepare_loan(self, book):
        self.ensure_one()
        return {'book_id': book.id,
                'member_id': self.id,
                'duration': self.loan_duration}

    @api.onchange('date_end')
    def on_change_date_end(self):
        date_end = fields.Date.from_string(self.date_end)
        today = date.today()
        if date_end <= today:
            self.loan_duration = 0
            return {
                'warning': {
                    'title': 'expired membership',
                    'message': "Membership has expired",
                },
            }


class LibraryBookLoan(models.Model):
    _name = 'library.book.loan'

    def _default_date(self):
        return fields.Date.today()

    book_id = fields.Many2one('library.book', required=True)
    member_id = fields.Many2one('library.member',
                                required=True)
    state = fields.Selection([('ongoing', 'Ongoing'),
                              ('done', 'Done')],
                             'State', required=True)
    date = fields.Date('Loan date', required=True,
                       default=_default_date)
    duration = fields.Integer('Duration', default=15)
    date_due = fields.Date(
        compute='_compute_date_due',
        store=True,
        string='Due for'
        )

    @api.depends('start_date', 'due_date')
    def _compute_date_due(self):
        for loan in self:
            start_date = fields.Date.from_string(loan.date)
            due_date = start_date + timedelta(days=loan.duration)
            loan.date_due = fields.Date.to_string(due_date)
