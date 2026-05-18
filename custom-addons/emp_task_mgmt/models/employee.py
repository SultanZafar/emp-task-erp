from odoo import models, fields

class EmployeeCustom(models.Model):
    _name = 'hr.employee.custom'
    _description = 'Employee'

    employee_id = fields.Char ('Employee ID', required=True)
    name = fields.Char('Name', required=True)
    department = fields.Char('Department', required=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email', required=True)
    designation = fields.Char('Designation')
    joining_date = fields.Date('Joining Date')
    location = fields.Selection([
        ('lahore', 'Lahore'),
        ('islamabad', 'Islamabad'),
        ('karachi', 'Karachi'),
    ], 'Location')
    employment_type = fields.Selection([
        ('permanent', 'Permanent'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
    ], 'Employee Type')
    work_mode = fields.Selection([
        ('onsite', 'On site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    ], 'Work Mode')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], 'Status', default='active')
    reporting_manager = fields.Many2one(
        'hr.employee.custom',
        'Reporting Manager',
    )