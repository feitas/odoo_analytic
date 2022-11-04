from odoo import models, fields


class AccountAnalyticMonth(models.Model):
    _name = 'account.analytic.month'
    _description = 'Account Analytic Month'

    name = fields.Char()
    type = fields.Selection([('standard', '标准'),('infact', '实际')], string="类型")
    start_date = fields.Date(string="开始日期")
    end_date = fields.Date(string="结束日期")
    state = fields.Selection([('draft', '草稿'),('done', '完成')], string="状态")