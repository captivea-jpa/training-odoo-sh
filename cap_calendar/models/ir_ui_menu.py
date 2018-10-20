# coding: utf-8
# Part of CAPTIVEA. Odoo 11.

from odoo import models


class IRUIMenu(models.Model):
    """Manage 'ir.ui.menu' model. Overriding model."""
    _inherit = "ir.ui.menu"
