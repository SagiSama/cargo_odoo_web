# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.tools.translate import _

class CargoShipmentRequest(http.Controller):

    @http.route(['/request_shipment_form'], type='http', auth="public", website=True)
    def request_shipment_form(self, **kw):
        return http.request.render("web_track_shipment.request_shipment_form", {})

    @http.route(['/request_shipment'], type='http', auth="public", website=True)
    def request_shipment(self, **kw):
        result = request.env['shipment.request'].sudo().create(kw)
        if result:
            res = True
        else:
            res = False
        return request.render("web_track_shipment.request_shipment_response", {"shipment_request_res": res})

