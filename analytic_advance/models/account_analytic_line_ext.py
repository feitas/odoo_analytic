import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountAnalyticLineExt(models.Model):
    _inherit = 'account.analytic.line'
    # TODO 创建核算项目account.analytic.line的时候，从默认核算规则上获取算法来创建
