from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"
    message = fields.Char(string='Custom Message')
    other_informations = fields.Char(string='Other Informations')
    message_2 = fields.Char(string='Custom Message 2')

