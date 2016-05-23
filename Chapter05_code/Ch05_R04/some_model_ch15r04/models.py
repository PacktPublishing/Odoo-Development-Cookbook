# coding: utf-8

from openerp import models, api, fields


class SomeModel(models.Model):
    _name = 'some.model'

    @api.multi
    def create_company(self):
        today_str = fields.Date.contex_today()
        val1 = {'name': u'Eric Idel',
                'email': u'eric.idle@example.com',
                'date': today_str,
                }
        val2 = {'name': u'John Cleese',
                'email': u'john.cleese@example.com',
                'date': today_str,
                }
        company_val = {'name': u'Flying Circus',
                       'email': u'm.python@example.com',
                       'date': today_str,
                       'is_company': True,
                       'child_ids': [(0, 0, val1),
                                     (0, 0, val2),
                                     ],
                       }
        record = self.env['res.company'].create(company_val)
        return record
