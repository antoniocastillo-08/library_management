from odoo import models, api

class ReportActiveLoans(models.AbstractModel):
    _name = 'report.library_management.report_active_loans'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['library.loan'].search([('loan_status', '=', 'ongoing')])
        return {
            'doc_ids': docids,
            'doc_model': 'library.loan',
            'docs': docs,
        }