# coding: utf-8

from datetime import date, timedelta
from openerp.osv import orm, fields
from openerp.tools import _, DEFAULT_SERVER_DATE_FORMAT as DATE_FMT


class library_book(orm.Model):
    _name = 'library.book'
    _columns = {
        'name': fields.char('Name', required=True),
        'author_ids': fields.many2many('res.partner'),
    }


class library_member(orm.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}

    _columns = {
        'partner_id': fields.many2one('res.partner',
                                      'Partner',
                                      required=True),
        'loan_duration': fields.integer('Loan duration',
                                        required=True),
        'date_start': fields.date('Member since'),
        'date_end': fields.date('Expiration date'),
        'number': fields.char('Number', required=True),
    }

    _defaults = {
        'loan_duration': 10,
    }

    def on_change_date_end(self, cr, uid, date_end, context=None):
        date_end = date.strptime(date_end, DATE_FMT)
        today = date.today()
        if date_end <= today:
            return {
                'value': {'loan_duration': 0},
                'warning': {
                    'title': 'expired membership',
                    'message': 'This member membership has expired',
                },
            }

    def borrow_books(self, cr, uid, ids, book_ids, context=None):
        if len(ids) != 1:
            raise orm.except_orm(
                _('Error!'),
                _('It is forbidden to loan the same books '
                  'to multiple members.'))
        loan_obj = self.pool['library.book.loan']
        member = self.browse(cr, uid, ids[0], context=context)
        for book_id in book_ids:
            val = self._prepare_loan(
                cr, uid, member, book_id, context=context
            )
            loan_id = loan_obj.create(cr, uid, val, context=context)

    def _prepare_loan(self, cr, uid,
                      member, book_id,
                      context=None):
        return {'book_id': book_id,
                'member_id': member.id,
                'duration': member.loan_duration}


class library_book_loan(orm.Model):
    _name = 'library.book.loan'

    def _compute_date_due(self, cr, uid, ids,
                          fields, arg, context=None):
        res = {}
        for loan in self.browse(cr, uid, ids, context=context):
            start_date = date.strptime(loan.date, DATE_FMT)
            due_date = start_date + timedelta(days=loan.duration)
            res[loan.id] = due_date.strftime(DATE_FMT)
        return res

    _columns = {
        'book_id': fields.many2one('library.book', required=True),
        'member_id': fields.many2one('library.member',
                                     required=True),
        'state': fields.selection([('ongoing', 'Ongoing'),
                                   ('done', 'Done')],
                                  'State', required=True),
        'date': fields.date('Loan date', required=True),
        'duration': fields.integer('Duration'),
        'date_due': fields.function(
            fnct=_compute_date_due,
            type='date',
            store=True,
            string='Due for'),
    }

    def _default_date(self, cr, uid, context=None):
        return date.today().strftime(DATE_FMT)

    _defaults = {
        'duration': 15,
        'date': _default_date,
    }
