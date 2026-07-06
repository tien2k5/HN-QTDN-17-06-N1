{
    'name': 'Quản lý Chấm công & Tính lương',
    'version': '1.0',
    'category': 'Human Resources',

    # KẾT NỐI MODULE NHÂN SỰ
    'depends': ['base', 'nhan_su'],

    'data': [
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
}
