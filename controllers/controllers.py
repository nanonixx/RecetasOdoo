# -*- coding: utf-8 -*-
# from odoo import http


# class Recetas(http.Controller):
#     @http.route('/recetas/recetas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recetas/recetas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recetas.listing', {
#             'root': '/recetas/recetas',
#             'objects': http.request.env['recetas.recetas'].search([]),
#         })

#     @http.route('/recetas/recetas/objects/<model("recetas.recetas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recetas.object', {
#             'object': obj
#         })
