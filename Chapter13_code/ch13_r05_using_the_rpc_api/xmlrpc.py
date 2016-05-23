#!/usr/bin/env python2
import xmlrpclib

db = 'odoo9'
user = 'admin'
password = 'admin'
uid = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/2/common')\
    .authenticate(db, user, password, {})
odoo = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/2/object')
installed_modules = odoo.execute_kw(
    db, uid, password, 'ir.module.module', 'search_read',
    [[('state', '=', 'installed')], ['name']], {})
for module in installed_modules:
    print module['name']
