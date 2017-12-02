# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task','mail.thread']
    user_id = fields.Many2one('res.users','Responsable')
    date_deadline = fields.Date('Data caducitat')
    name = fields.Char(help="Què s'ha de fer?")

    @api.multi
    def do_clear_done(self):
        domain = [('isDone', '=', True),
                  '|', ('user_id', '=', self.env.uid),
                  ('user_id', '=', False)]

        done_recs = self.search(domain)
        done_recs.write({'isActive': False})
        return True

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()