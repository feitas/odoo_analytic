from odoo import models, fields


class AccountAnalyticVersion(models.Model):
    _name = 'account.analytic.version'
    _description = 'Account Analytic Version'

    name = fields.Char()
    type = fields.Selection([('standard', '标准'),('infact', '实际')], string="类型")
    active = fields.Boolean(default=True)
    description = fields.Char("描述")