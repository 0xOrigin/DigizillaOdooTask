{
    'name':'Digizilla',
    'version': '1.0.0',
    'author': '0xOrigin',
    'license': 'Other proprietary',
    'summary': 'Assessment task for Python developer role.',
    'sequence': 1,
    'description':'This is an Assessment task for Python developer role at Digizilla Company.',
    'category':'Customization',
    'website':'https://github.com/0xOrigin',
    'depends':['base', 'web', 'mail'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'report/report_template.xml',
        'report/digizilla_report.xml',
        'views/digizilla_view.xml',
    ],
    'qweb': [
        'views/digizilla_view.xml', 
    ]
}
