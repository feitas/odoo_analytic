import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountAnalyticLineExt(models.Model):
    _inherit = 'account.analytic.line'

    month_id = fields.Many2one('account.analytic.month', string="成本月份")

    @api.model
    def create(self, vals):
        def exec_operator(operator, arg1, arg2):
            if operator == "add":
                return arg1 + arg2
            elif operator == "reduce":
                return arg1 - arg2
            elif operator == "multiply":
                return arg1 * arg2
            elif operator == "divide":
                return arg1 / arg2 if arg2 else 0
            return 0

        if 'account_id' in vals and vals.get('account_id'):
            defaults = self.env["account.analytic.default"].sudo().search([('analytic_id.id', '=', vals['account_id'])])
            rule = defaults and defaults[0]
            if rule and rule.first_model and rule.first_field_name and rule.second_model and rule.second_field_name and rule.operator:
                first_model = rule.first_model.model
                first_field_name = rule.first_field_name
                arg1 = sum(self.env[first_model].sudo().search([]).mapped(first_field_name))
                second_model = rule.second_model.model
                second_field_name = rule.second_field_name
                arg2 = sum(self.env[second_model].sudo().search([]).mapped(second_field_name))
                amount = exec_operator(rule.operator, arg1, arg2)
                vals["amount"] = amount
                _logger.warning("操作数1：{}".format(arg1))
                _logger.warning("操作数2：{}".format(arg2))
            else:
                vals["amount"] = 0
                _logger.warning("找不到对应规则或规则中缺少参数！")
        return super(AccountAnalyticLineExt, self).create(vals)