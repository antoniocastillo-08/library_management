from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    user_id = fields.Many2one('library.user', string='User', required=True)
    book_id = fields.Many2one('library.book', string='Book', required=True)
    loan_date = fields.Date(string='Loan Date', required=True)
    return_date = fields.Date(string='Return Date')
    loan_status = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('late', 'Late')
    ], string='Loan Status', default='ongoing')
