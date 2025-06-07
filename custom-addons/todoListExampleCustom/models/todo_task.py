from odoo import models, fields

class TodoTask (models.Model):
    _name ='todo.task'
    _description='Todo task'

    name = fields.Char('Task name', required = True)
    description = fields.Char('Ghi chú Task', required = True)
    due_date = fields.Date(string='')
    done = fields.Boolean('Done task!!!', default =False)
