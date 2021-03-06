# -*- encoding: utf-8 -*-
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    "name": "MRP Bom Catch Product Code",
    "version": "1.0",
    "author": "OdooMRP team",
    "category": "MRP",
    "website": "http://www.odoomrp.com",
    "description": """
    This module performs the following:

    1.- When the product template is selected, the internal code is brought to
        the reference in BoM list.
    2.- When the product is selected, the internal code is brought to the
        reference in BoM list.

   """,
    "depends": ['mrp',
                'product_variant_default_code',
                ],
    "data": [],
    "installable": True
}
