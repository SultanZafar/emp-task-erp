{
    'name': 'Employee Task Management',
    'version': '18.0.1.0.0',
    'summary': 'Manage employees and their tasks efficiently',
    'description': 'Employee Task Management System for managing employee records and tasks',
    'author': 'SultanZafar',
    'category': 'Human Resources',
    'depends': ['base', 'mail', 'web'],
    'controllers': ['controllers/main.py'],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/employee_views.xml',
        'views/task_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'emp_task_mgmt/static/src/css/dashboard.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
