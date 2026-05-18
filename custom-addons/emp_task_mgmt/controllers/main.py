from odoo import http
from odoo.http import request

class DashboardController(http.Controller):

    @http.route('/emp_task/dashboard', auth='user', website=False)
    def dashboard(self, **kwargs):
        # Data fetch karo
        employees = request.env['hr.employee.custom'].search([])
        tasks = request.env['emp.task'].search([])

        # Count karo
        total_employees = len(employees)
        total_tasks = len(tasks)
        new_tasks = len(tasks.filtered(lambda t: t.status == 'new'))
        in_progress = len(tasks.filtered(lambda t: t.status == 'in_progress'))
        done_tasks = len(tasks.filtered(lambda t: t.status == 'done'))

        values = {
            'total_employees': total_employees,
            'total_tasks': total_tasks,
            'new_tasks': new_tasks,
            'in_progress': in_progress,
            'done_tasks': done_tasks,
            'recent_tasks': tasks[:5],
            'employees': employees[:5],
        }
        return request.render('emp_task_mgmt.dashboard_template', values)
