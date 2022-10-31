import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class AccountAnalyticDefaultExt(models.Model):
    _inherit = "account.analytic.default"

    first_name = fields.Char(string='操作数1名称')
    first_type = fields.Selection([('model','模型'),('api','接口'),('pre','上级结果')],string="操作数1类型",default="model")
    first_model = fields.Many2one('ir.model',string="模型")
    first_api = fields.Char(string='接口')
    first_field_name = fields.Char(string='操作数1字段名称')
    first_field_config_name = fields.Many2one('field.config.table',string='操作数1字段名称')

    second_name = fields.Char(string='操作数2名称')
    second_type = fields.Selection([('model','模型'),('api','接口'),('pre','上级结果')],string="操作数2类型",default="model")
    second_model = fields.Many2one('ir.model',string="模型")
    second_api = fields.Char(string='接口')
    second_field_name = fields.Char(string='操作数2字段名称')
    second_field_config_name = fields.Many2one('field.config.table',string='操作数2字段名称')
    operator = fields.Selection([('add','＋'),('reduce','－'),('multiply','×'),('divide','÷')],string="操作符")

    @api.onchange('first_field_config_name')
    def _onchange_first_field_config_name(self):
        for record in self:
            record.first_model = record.first_field_config_name.model_name.id
            record.first_field_name = record.first_field_config_name.field_name.name
    
    @api.onchange('second_field_config_name')
    def _onchange_second_field_config_name(self):
        for record in self:
            record.second_model = record.second_field_config_name.model_name.id
            record.second_field_name = record.second_field_config_name.field_name.name

    @api.onchange('first_type')
    def _onchange_first_type(self):
        for record in self:
            record.first_model=""
            record.first_field_name=""
            record.first_field_config_name=""
    
    @api.onchange('second_type')
    def _onchange_second_type(self):
        for record in self:
            record.second_model=""
            record.second_field_name=""
            record.second_field_config_name=""
