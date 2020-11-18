# -*- coding: utf-8 -*-
from odoo import http

# class MyFirstModule(http.Controller):
#     @http.route('/my_first_module/my_first_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_first_module/my_first_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_first_module.listing', {
#             'root': '/my_first_module/my_first_module',
#             'objects': http.request.env['my_first_module.my_first_module'].search([]),
#         })

#     @http.route('/my_first_module/my_first_module/objects/<model("my_first_module.my_first_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_first_module.object', {
#             'object': obj
#         })