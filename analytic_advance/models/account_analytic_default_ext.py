import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class AccountAnalyticDefaultExt(models.Model):
    _inherit = "account.analytic.default"

    """
    操作数1名称 -> char
    操作数1类型 -> selection: 模型/接口/上级结果
    操作数1字段名称 -> char
    操作数2名称 -> char
    操作数2类型 -> selection: 模型/接口/上级结果
    操作数1字段名称 -> char
    操作符 -> selection: 加/减/乘/除
    """
    first_name = fields.Char(string='操作数1名称')
    first_type = fields.Selection([('model','模型'),('api','接口'),('pre','上级结果')],string="操作数1类型",default="model")
    first_model = fields.Many2one('ir.model',string="模型")
    first_api = fields.Char(string='接口')
    first_field_name = fields.Char(string='操作数1字段名称')
    second_name = fields.Char(string='操作数2名称')
    second_type = fields.Selection([('model','模型'),('api','接口'),('pre','上级结果')],string="操作数2类型",default="model")
    second_model = fields.Many2one('ir.model',string="模型")
    second_api = fields.Char(string='接口')
    second_field_name = fields.Char(string='操作数2字段名称')
    operator = fields.Selection([('add','＋'),('reduce','－'),('multiply','×'),('divide','÷')],string="操作符")
