# coding: utf-8

from openerp import models, api, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title')
    isbn = fields.Char('ISBN')
    author_ids = fields.Many2many('res.partner', 'Authors')

    @api.model
    def name_get(self):
        result = []
        for book in self:
            authors = book.author_ids.mapped('name')
            name = u'%s (%s)' % (book.title,
                                 u', '.join(authors))
            result.append((book.id, name))
    return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike',
                     limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not(name=='' and operator=='ilike'):
            args += ['|', '|',
                     ('name', operator, name),
                     ('isbn', operator, name),
                     ('author_ids.name', operator, name)
                     ]
        return super(LibraryBook, self)._name_search(
            name='', args=args, operator='ilike',
            limit=limit, name_get_uid=name_get_uid)
