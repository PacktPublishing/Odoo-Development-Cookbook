#!/usr/bin/env python2
import json
import urllib2

db = 'odoo9'
user = 'admin'
password = 'admin'

request = urllib2.Request(
    'http://localhost:8069/web/session/authenticate',
    json.dumps({
        'jsonrpc': '2.0',
        'params': {
            'db': db,
            'login': user,
            'password': password,
        },
    }),
    {'Content-type': 'application/json'})
result = urllib2.urlopen(request).read()
result = json.loads(result)
session_id = result['result']['session_id']
request = urllib2.Request(
    'http://localhost:8069/web/dataset/call_kw',
    json.dumps({
        'jsonrpc': '2.0',
        'params': {
            'model': 'ir.module.module',
            'method': 'search_read',
            'args': [
                [('state', '=', 'installed')],
                ['name'],
            ],
            'kwargs': {},
        },
    }),
    {
        'X-Openerp-Session-Id': session_id,
        'Content-type': 'application/json',
    })
result = urllib2.urlopen(request).read()
result = json.loads(result)
for module in result['result']:
    print module['name']
