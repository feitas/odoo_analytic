from odoo import models


class AccountAnalyticGroup(models.Model):
    _inherit = 'account.analytic.group'
    _rec_name = 'name'