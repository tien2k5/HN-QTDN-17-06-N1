{
    'name': 'Quản lý khách hàng',
    'version': '15.0.1.0.0',
    'category': 'Business',
    'summary': 'Quản lý khách hàng',
    'author': 'FIT-DNU',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'nhan_su',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/khach_hang.xml',
    ],

    'installable': True,
    'application': True,
} 
