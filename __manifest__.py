# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Module for managing library books, authors, categories, and loans',
    'author': 'Antonio',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/author_view.xml',
        'views/books_view.xml',
        'views/users_view.xml',
        'views/loan_view.xml',
        'views/category_view.xml',
        'report/report_books_available.xml',
        'report/report_active_loans.xml',
        'report/report_loan_history.xml',
        'report/report_registered_users.xml',
        'views/menu.xml',

    ],
    'installable': True,
    'application': True,
}
