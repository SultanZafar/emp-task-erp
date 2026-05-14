from odoo import models, fields

class EmployeeTask(models.Model):
    _name = 'emp.task'
    _description = 'Employee Task'

    name = fields.Char('Task Title', required=True)
    description = fields.Text('Task Description')
    deadline = fields.Date('Deadline')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ],string='Status', default='new')
    assigned_to = fields.Many2one(
        'hr.employee.custom',
        string='Assigned To'
    )