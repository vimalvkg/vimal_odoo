# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError




class AccountMove(models.Model):
    _inherit = 'account.move'

    def send_invoice_payment_email(self):
        template = self.env.ref('vm_invoice_send_payment_link.email_template_invoice_payment')
        for invoice in self:
            template.send_mail(invoice.id, force_send=True)
