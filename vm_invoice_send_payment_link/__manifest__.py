# -*- coding: utf-8 -*-
{
    'name': "Send Payment Link to Customer ",

    'summary': "Send your invoice payment link to your  customer",

    'description': """
Send your invoice payment link to your  customer on click button on invoice 
    """,

    'author': "Vimal",
    'website': "Vimal",

    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'data/data_email_payment_link.xml',
        'views/account_move_view.xml'
        
    ],
    'license': 'LGPL-3',
    'price': 10.00,
    'currency': 'USD'
}

