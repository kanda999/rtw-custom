# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class sale_line_bom_stock(models.Model):
    _inherit = "sale.order.line"

    bom_id = fields.Many2one("mrp.bom",compute="_compute_product_bom_id")
    bom_stock = fields.Char()

    def _compute_product_bom_id(self):
        for line in self:
            product_bom = 
            line.bom_id = False
            if product_bom == line.product_id:
                line.bom_id = product_bom.id
