# -*- coding: utf-8 -*-

from odoo import models, fields, api


class recetas(models.Model):
    _name = 'recetas.recetas'
#     _description = 'recetas.recetas'

    name = fields.Char()
    id = fields.Char()
    dificultad = fields.Char()

    time = fields.Integer()
    
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    steps = fields.Text()

    vegano = fields.Boolean()
    celiaco = fields.Boolean()
    
     
    image = fields.Image()
    dateAdded = fields.Date()
    #Imagen?

    # ingredientes = fields.Text()
    ingredientes = fields.One2many("recetas.ingredientes", "name", string="Ingredientes")
    anotaciones = fields.Text()

class ingredientes(models.Model):
    _name = 'recetas.ingredientes'

    nameIng = fields.Many2one("recetas.recetas", "ingredientes")
    # name = fields.Char()
    idIng = fields.Char()
    categoria=fields.Char()
    proveedor=fields.Char()

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100