import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class AccountAnalyticDefaultExt(models.Model):
    _inherit = "account.analytic.default"

    # TODO 扩展默认核算规则的模型。
    # TODO 添加字段：操作数1名称、类型（模型/接口/上级结果）、字段、操作数2类型（模型/接口/上级结果）、操作符（加/减/乘/除）

    """
    操作数1名称 -> char
    操作数1类型 -> selection: 模型/接口/上级结果
    操作数1字段名称 -> char
    操作数2名称 -> char
    操作数2类型 -> selection: 模型/接口/上级结果
    操作数1字段名称 -> char
    操作符 -> selection: 加/减/乘/除
    """
