# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ShipmentRequest(models.Model):
    _name = "shipment.request"

    name = fields.Char(string='Customer name', required=True, translate=True)
    phone = fields.Char(string='Phone', required=True, translate=True)
    weight = fields.Integer(string='Weight', required=True, translate=True)
    object = fields.Char(string='Object', required=True, translate=True)

    @api.model
    def create(self, vals):
        res_id = super(ShipmentRequest, self).create(vals)
        return res_id
