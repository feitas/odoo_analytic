import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountAnalyticLineExt(models.Model):
    _inherit = 'account.analytic.line'

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

        if 'account_id' in vals and 'move_id' in vals and vals.get('account_id') and vals.get('account_id'):
            arg1 = self.env["account.move.line"].sudo().browse(vals.get('move_id')).price_unit
            defaults = self.env["account.analytic.default"].sudo().search([('analytic_id.id', '=', vals['account_id']),('first_model.model', '=', 'product.product')])
            if defaults and defaults[0].second_model and defaults[0].second_field_name:
                second_model = defaults[0].second_model.model
                second_field_name = defaults[0].second_field_name
                arg2 = sum(self.env[second_model].sudo().search([]).mapped(second_field_name))
                amount = exec_operator(defaults[0].operator, arg1, arg2)
                vals["amount"] = amount
        return super(AccountAnalyticLineExt, self).create(vals)