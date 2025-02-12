from odoo import models, fields

class User(models.Model):
    _name = 'library.user'
    _description = 'Library User'

    full_name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    registration_date = fields.Date(string='Registration Date', default=fields.Date.today)
