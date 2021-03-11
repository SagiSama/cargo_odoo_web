# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.tools.translate import _

class CargoShipmentTrack(http.Controller):

    @http.route(['/track_shipment_form'], type='http', auth="public", website=True)
    def track_shipment_form(self, **kw):
        return http.request.render("web_track_shipment.track_shipment_form", {"initial_load": True})

    @http.route(['/track_shipment'], type='http', auth="public", website=True)
    def track_shipment(self, **kw):
#         result = request.env['shipment'].search([('name', '=', kw['shipment_code'])])
        if kw and kw['shipment_code']:
            result = request.env['res.partner'].sudo().search([('name', '=', kw['shipment_code'])])
            shipment_code_arg = kw['shipment_code']
            initial_load = False
        else:
            result = []
            shipment_code_arg = ''
            initial_load = True
        return request.render("web_track_shipment.track_shipment_form", {"shipment_details": result, "shipment_code": shipment_code_arg, "initial_load": initial_load})

