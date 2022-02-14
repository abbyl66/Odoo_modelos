# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo51y(http.Controller):
#     @http.route('/odoo51y/odoo51y/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo51y/odoo51y/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo51y.listing', {
#             'root': '/odoo51y/odoo51y',
#             'objects': http.request.env['odoo51y.odoo51y'].search([]),
#         })

#     @http.route('/odoo51y/odoo51y/objects/<model("odoo51y.odoo51y"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo51y.object', {
#             'object': obj
#         })
