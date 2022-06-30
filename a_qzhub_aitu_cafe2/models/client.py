# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ClientSurvey(models.Model):
    _name = "client.survey"
    _description = "Client Survey"
    _rec_name = "cafename"


    menu_lines = fields.Many2one('cafe.admin', string="Cafe")
    id = fields.Integer(string='Id', required=True)
    cafename = fields.Char(string='Cafe name', related="menu_lines.cafename", required=True)
    adminname = fields.Char(string='Administrator name', related="menu_lines.adminname", required=True)
    address = fields.Char(string='Address of Cafe', related="menu_lines.address")

    # Menu fields
    menus_choose = fields.Many2one('cafe.menus', string="Menu")
    product_first = fields.Text(string='First', related="menus_choose.product_first")
    product_second = fields.Text(string='Second', related="menus_choose.product_second")
    product_salat = fields.Text(string='Salat', related="menus_choose.product_salat")


    user = fields.Char(string="User")

    def like_menu(self):
        return True

    menu = fields.Text(string="Menu")

    menus_id = fields.One2many('cafe.menus', 'cafe_id', string="GHJK")

    # def compute_menus_id(self):


    # menus_id = fields.Many2many('cafe.menus', 'cafe_id', string="GHJK")
    #
    # product_first = fields.Text(string='First', related="menus_id.product_first")
    # product_second = fields.Text(string='Second', related="menus_id.product_second")
    # product_salat = fields.Text(string='Salat', related="menus_id.product_salat")



    def get_data(self):
        fetched_data = self.env['cafe.admin'].search([])
        return fetched_data




# class CafeMenuLines(models.Model):
#     _name = "client.survey"
#     _description = "Cafe Menu"
#
#     # product_id = fields.Many2one('product.category', string='product')
#     product_first = fields.Text(string='First')
#     product_second = fields.Text(string='Second')
#     product_salat = fields.Text(string='Salat')
#     menu_id = fields.Many2one('cafe.admin', string='Menu ID')
