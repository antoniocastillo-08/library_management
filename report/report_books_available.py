from odoo import models, api

class ReportBooksAvailable(models.AbstractModel):
    _name = 'report.library_management.report_books_available'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['library.book'].search([('available_copies', '>', 0)])
        return {
            'doc_ids': docids,
            'doc_model': 'library.book',
            'docs': docs,
        }