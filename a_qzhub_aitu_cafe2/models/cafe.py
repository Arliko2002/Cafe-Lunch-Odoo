# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.addons.a_qzhub_aitu_cafe2.models.client import ClientSurvey


class CafeMenu(models.Model):
    _name = "cafe.admin"
    _description = "Cafe Admin"
    _rec_name = "cafename"

    cafename = fields.Char(string='Cafe name', required=True)
    adminname = fields.Char(string='Administrator name', required=True)
    address = fields.Char(string='Address of Cafe')
    menu = fields.Text(string="Menu")
    # menu_lines = fields.One2many('cafe.menu', 'menu_id', string="Menu Lines")
    menus_id = fields.Many2many('cafe.menus', 'cafe_id', string="GHJK")

    product_first = fields.Text(string='First', related="menus_id.product_first")
    product_second = fields.Text(string='Second', related="menus_id.product_second")
    product_salat = fields.Text(string='Salat', related="menus_id.product_salat")

    user_id = fields.Many2one(
        'res.users', string='Created by', index=True, tracking=True,
        default=lambda self: self.env.user, check_company=True)

    # def compute_menuname(self):
    #     menuname = self.env['cafe.menus'].search([('cafename', '=', self.cafename)])
    #     print('menuname', menuname)


    # def compute_product_first(self):
    #     product_first = self.env['cafe.menus'].search(['product_first', '=', self.product_first])
    #     self.product_first = product_first
    #
    #
    # def compute_product_second(self):
    #         product_second = self.env['cafe.menus'].search(['product_second', '=', self.product_second])
    #         self.product_second = product_second
    #
    #
    # def compute_product_salat(self):
    #     product_salat = self.env['cafe.menus'].search(['product_salat', '=', self.product_salat])
    #     self.product_salat = product_salat


     # menu_clients = fields.Many2many('client.survey', string="Cafe name")

    # def copy(self, default=None):
    #     default = dict(default or {})
    #     if default is None:
    #         default = {}
    #     return super(CafeMenu, self).copy(default=default)

    def add_to_cart(self):
        return True


    #     for rec in self:
    #         cafename = self.env['client.survey'].search(['id', '=', self.id])
    #         print('cafename: ', cafename)

    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     self.ensure_one()
    #     default = dict(default or {})
    #     # if 'cafename' not in default:
    #     #     default['cafename'] = _("%s (copy)") % (self.cafename or '')
    #     return super(CafeMenu, self).copy(default=ClientSurvey)
#
# class CafeMenuLines(models.Model):
#     _name = "cafe.menu"
#     _description = "Cafe Menu"
#
#     # product_id = fields.Many2one('product.category', string='product')
#     product_first = fields.Text(string='First')
#     product_second = fields.Text(string='Second')
#     product_salat = fields.Text(string='Salat')
#     menu_id = fields.Many2one('cafe.admin', string='Menu ID')