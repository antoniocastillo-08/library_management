from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    author_id = fields.Many2one('library.author', string='Author')
    category_id = fields.Many2one('library.category', string='Category')
    total_copies = fields.Integer(string='Total Copies', required=True, default=1)
    available_copies = fields.Integer(string='Available Copies', required=True, default=1)