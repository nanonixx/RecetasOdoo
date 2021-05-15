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
    
    dateAdded = fields.Date()
    #Imagen?

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100