{
    'name': 'Quan Ly Khach Hang',
    'version': '15.0.1.0',
    'category': 'CRM',
    'summary': 'Quan ly khach hang',
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
