from odoo import models, fields

class EmployeeCustom(models.Model):
    _name = 'hr.employee.custom'
    _description = 'Employee'

    name = fields.Char('Name', required=True)
    department = fields.Char('Department', required=True)
    email = fields.Char('Email', required=True)
