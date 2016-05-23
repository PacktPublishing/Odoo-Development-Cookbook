from openerp.test.common import TransactionCase


class LibraryTestCase(TransactionCase):

    def setUp(self):
        super(LibraryTestCase, self).setUp()
        book_model = self.env['library.book'].sudo(
            self.ref('base.user_demo')
        )
        self.book = book_model.create(
            {'name': 'Test book',
             'state': 'draft',
             }
        )

    def test_change_draft_available(self):
        '''test changing state from draft to available'''
        self.book.change_state('available')
        self.assertEqual(self.book.state, 'available')

    def test_change_available_draft_no_effect(self):
        '''test forbidden state change from available to draft'''
        self.book.change_state('available')
        self.book.change_state('draft')
        self.assertEqual(
            self.book.state,
            'available',
            'the state cannot change from available to %s' % self.book.state
        )
