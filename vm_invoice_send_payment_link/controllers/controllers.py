# -*- coding: utf-8 -*-
# from odoo import http


# class VmInvoiceSendPaymentLink(http.Controller):
#     @http.route('/vm_invoice_send_payment_link/vm_invoice_send_payment_link', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vm_invoice_send_payment_link/vm_invoice_send_payment_link/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vm_invoice_send_payment_link.listing', {
#             'root': '/vm_invoice_send_payment_link/vm_invoice_send_payment_link',
#             'objects': http.request.env['vm_invoice_send_payment_link.vm_invoice_send_payment_link'].search([]),
#         })

#     @http.route('/vm_invoice_send_payment_link/vm_invoice_send_payment_link/objects/<model("vm_invoice_send_payment_link.vm_invoice_send_payment_link"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vm_invoice_send_payment_link.object', {
#             'object': obj
#         })

