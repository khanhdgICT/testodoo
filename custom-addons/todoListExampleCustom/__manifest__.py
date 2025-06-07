# __manifest__.py
{
    'name': 'ToDo123 List',
    'version': '1.0',
    'summary': 'Simple To-Do List Module',
    'author': 'Khanh Dang',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'views/todo_task_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'web_icon': 'todolistexamplecustom/static/description/icon.png'
}