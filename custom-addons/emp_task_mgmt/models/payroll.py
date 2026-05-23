from odoo import models, fields, api

class EmployeePayroll(models.Model):
    _name = 'emp.payroll'
    _description = 'Employee Payroll'

    employee_id = fields.Many2one(
        'hr.employee.custom',
        string='Employee',
        required=True
    )
    month = fields.Selection([
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ], string='Month', required=True)
    year = fields.Integer('Year', default=2026)
    salary = fields.Float('Salary Amount', required=True)
    status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], string='Status', default='unpaid')
    payment_date = fields.Date('Payment Date', readonly=True)

    def action_pay_salary(self):
        self.status = 'paid'
        self.payment_date = fields.Date.today()
