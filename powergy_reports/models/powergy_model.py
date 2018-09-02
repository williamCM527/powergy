from odoo import api, _, tools, fields, models, exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime
from . import amount_to_text


class ReportPurchase(models.Model):
	"""docstring for ReportPurchase"""
	_inherit = 'purchase.order'

	type_of_order = fields.Selection([('national','National'),
							   		('international','International')], help='Choose the type of order', default='national',required=True)
	observations= fields.Text(string='Observations')
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
                                 help='Amount of the invoice in letter')
	
	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)


class ReportFactura(models.Model):

	_inherit = 'account.invoice'

	observations= fields.Text(string='Observations')


class ReportPago(models.Model):

	_inherit = 'account.payment'

	cambio = fields.Float(string='Tipo Cambio')

class QuotationsFields(models.Model):
	"""docstring for Quitations"""
	_inherit = 'sale.order'

	indiv_orders = fields.Text(string='Pedidos Individuales')	
	name_site = fields.Char(string='Nombre de sitio')
	no_adrisa = fields.Char(string='No. Adrisa/Grafo')
	folio_patrimonial = fields.Char(string='Folio de pase de acceso de Seguridad Patrimonial')