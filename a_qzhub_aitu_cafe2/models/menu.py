# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CafeMenu(models.Model):
    _name = "cafe.menus"
    _description = "Menu Cafe"
    _rec_name = "menu_lines"

    # cafename = fields.Char(string='Cafe name', required=True)
    # adminname = fields.Char(string='Administrator name', required=True)
    # address = fields.Char(string='Address of Cafe')
    menu = fields.Text(string="Menu")

    cafe_data = fields.Many2one('cafe.admin', string="Menu Lines")
    # cafe_name = fields.One2many('cafe.admin', 'cafename', string="Menu Lines")
    menu_lines = fields.One2many('cafe.menu', 'cafe_id', string="Menu Lines")

    product_first = fields.Text(string='First')
    product_second = fields.Text(string='Second')
    product_salat = fields.Text(string='Salat')
    cafe_id = fields.Many2one('cafe.admin', string='Cafe ID')

    # cafe_name = fields.Char(string='Cafe Name', related="cafe_id.cafename")


    menu_lines = fields.Many2one('cafe.admin', string="Menu Lines")
    menus_id = fields.One2many('cafe.menus', 'cafe_id', string="GHJK")
    cafename = fields.Char(string='Cafe name', related="menu_lines.cafename", required=True)

    # menulike = fields.Char(string="Liked")



    # def like_menu(self):
    #     self.menulike = 'True'

# class CafeMenuLines(models.Model):
#     _name = "cafe.menu.lines"
#     _description = "Cafe Menu"
#
#     # product_id = fields.Many2one('product.category', string='product')
#     product_first = fields.Text(string='First')
#     product_second = fields.Text(string='Second')
#     product_salat = fields.Text(string='Salat')
#     cafe_id = fields.Many2one('cafe.admin', string='Cafe ID')
