from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    title = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    author_id = fields.Many2one('library.author', string='Author')
    category_id = fields.Many2one('library.category', string='Category')
    available_copies = fields.Integer(string='Available Copies', default=0)
