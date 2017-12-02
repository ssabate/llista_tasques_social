# -*- coding: utf-8 -*-
from odoo import http

# class LlistaTasquesSocial(http.Controller):
#     @http.route('/llista_tasques_social/llista_tasques_social/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/llista_tasques_social/llista_tasques_social/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('llista_tasques_social.listing', {
#             'root': '/llista_tasques_social/llista_tasques_social',
#             'objects': http.request.env['llista_tasques_social.llista_tasques_social'].search([]),
#         })

#     @http.route('/llista_tasques_social/llista_tasques_social/objects/<model("llista_tasques_social.llista_tasques_social"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('llista_tasques_social.object', {
#             'object': obj
#         })