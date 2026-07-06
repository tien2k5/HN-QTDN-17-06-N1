from odoo import models, fields


class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Cong Viec'

    ten_cong_viec = fields.Char(
        string='Tên công việc',
        required=True
    )

    mo_ta = fields.Text(
        string='Mô tả'
    )

    ngay_tao = fields.Date(
        string='Ngày tạo',
        default=fields.Date.today
    )

    han_hoan_thanh = fields.Date(
        string='Hạn hoàn thành'
    )

    trang_thai = fields.Selection(
        [
            ('moi', 'Mới'),
            ('dang_thuc_hien', 'Đang thực hiện'),
            ('hoan_thanh', 'Hoàn thành')
        ],
        default='moi',
        string='Trạng thái'
    )

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên thực hiện'
    )

    khach_hang_id = fields.Many2one(
        'khach_hang',
        string='Khách hàng'
    )
