# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Odoo cookbook - Chapter 15, recipe 03",
    "version": "9.0.1.0.0",
    "author": "Odoo cookbook",
    "license": "AGPL-3",
    "category": "Odoo cookbook",
    "summary": "Making RPC calls to the server",
    "depends": [
        'web',
    ],
    "qweb": [
        'static/src/xml/ch15_r03.xml',
    ],
    "data": [
        "views/res_partner.xml",
        "views/templates.xml",
    ],
}
