from odoo import models, fields, api


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

    ngay_hoan_thanh = fields.Date(
        string='Ngày hoàn thành',
        readonly=True
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

    tien_do = fields.Integer(
        string='Tiến độ (%)',
        compute='_compute_tien_do',
        store=True
    )

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên thực hiện'
    )

    khach_hang_id = fields.Many2one(
        'khach_hang',
        string='Khách hàng'
    )

    @api.depends('trang_thai')
    def _compute_tien_do(self):
        for rec in self:
            if rec.trang_thai == 'moi':
                rec.tien_do = 0
            elif rec.trang_thai == 'dang_thuc_hien':
                rec.tien_do = 50
            elif rec.trang_thai == 'hoan_thanh':
                rec.tien_do = 100
            else:
                rec.tien_do = 0

    def action_bat_dau(self):
        for rec in self:
            rec.trang_thai = 'dang_thuc_hien'

    def action_hoan_thanh(self):
        for rec in self:
            rec.trang_thai = 'hoan_thanh'
            rec.ngay_hoan_thanh = fields.Date.today()

            if rec.khach_hang_id:

                tat_ca = rec.khach_hang_id.cong_viec_ids

                if tat_ca and all(
                    x.trang_thai == 'hoan_thanh'
                    for x in tat_ca
                ):
                    rec.khach_hang_id.trang_thai = 'hoan_thanh'
