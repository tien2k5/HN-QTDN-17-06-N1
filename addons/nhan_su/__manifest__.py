# -*- coding: utf-8 -*-

{
    'name': 'Quản lý nhân sự',

    'summary': 'Quản lý nhân viên trong hệ thống ERP',

    'description': '''
Module quản lý nhân sự.

Chức năng:
- Quản lý nhân viên
- Quản lý đơn vị
- Quản lý chức vụ
- Quản lý lịch sử công tác
- Quản lý chứng chỉ
- Liên kết với module khách hàng
- Liên kết với module công việc
''',

    'author': 'FIT-DNU',

    'website': 'https://dnu.edu.vn',

    'category': 'Human Resources',

    'version': '15.0.1.0.0',

    'license': 'LGPL-3',

    'depends': [
        'base'
    ],

    'data': [

        'security/ir.model.access.csv',

        'views/chuc_vu.xml',
        'views/don_vi.xml',
        'views/nhan_vien.xml',
        'views/lich_su_cong_tac.xml',
        'views/chung_chi_bang_cap.xml',
        'views/danh_sach_chung_chi_bang_cap.xml',

        'views/menu.xml',

    ],

    'application': True,

    'installable': True,

    'auto_install': False,
}
