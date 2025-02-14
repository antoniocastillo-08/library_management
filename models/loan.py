from odoo import models, fields, api, exceptions
from datetime import timedelta

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    user_id = fields.Many2one('library.user', string='User', required=True)
    book_id = fields.Many2one('library.book', string='Book', required=True)
    loan_date = fields.Date(string='Loan Date', required=True, default=fields.Date.today)
    return_date = fields.Date(string='Return Date', required=True, default=lambda self: fields.Date.today() + timedelta(days=7))
    loan_status = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('late', 'Late')
    ], string='Loan Status', default='ongoing')

    @api.model
    def create(self, vals):
        # Check if the user has more than 3 ongoing loans
        ongoing_loans = self.search_count([
            ('user_id', '=', vals['user_id']),
            ('loan_status', '=', 'ongoing')
        ])
        if ongoing_loans >= 3:
            raise exceptions.UserError('User has more than 3 ongoing loans.')

        # Set the return date to 7 days from the loan date if not provided
        if 'return_date' not in vals:
            vals['return_date'] = fields.Date.to_string(
                fields.Date.from_string(vals['loan_date']) + timedelta(days=7)
            )

        # Reduce the available copies of the book
        book = self.env['library.book'].browse(vals['book_id'])
        if book.available_copies <= 0:
            raise exceptions.UserError('No copies of this book are available.')
        book.available_copies -= 1

        return super(LibraryLoan, self).create(vals)

    def return_book(self):
        for loan in self:
            if loan.loan_status == 'ongoing':
                loan.loan_status = 'returned'
                # Increase the available copies of the book
                loan.book_id.available_copies += 1
            else:
                raise exceptions.UserError('This loan is not ongoing.')

# Add a method to the library.book model to manage the quantity
class LibraryBook(models.Model):
    _inherit = 'library.book'

    quantity = fields.Integer(string='Quantity', default=1)

    def name_get(self):
        result = []
        for book in self:
            name = f"{book.title} ({book.isbn})"
            result.append((book.id, name))
        return result

class LibraryUser(models.Model):
    _inherit = 'library.user'

    def name_get(self):
        result = []
        for user in self:
            name = f"{user.name} ({user.email})"
            result.append((user.id, name))
        return result