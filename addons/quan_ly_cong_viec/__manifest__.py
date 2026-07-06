{
    'name': 'Quản lý công việc',
    'version': '15.0.1.0.0',
    'category': 'Business',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'nhan_su',
        'quan_ly_khach_hang'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/cong_viec.xml',
    ],

    'installable': True,
    'application': True,
}
