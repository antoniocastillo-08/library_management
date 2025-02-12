{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Module for managing library books, authors, categories, and loans',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base'],
    'data': [
        #'views/books_view.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/author_view.xml',
        'views/users_view.xml',

       #' 'views/category_view.xml',
        #''views/loan_view.xml',
       
    ],
    'installable': True,
    'application': True,
}
