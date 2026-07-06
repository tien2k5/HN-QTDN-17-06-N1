from odoo import models, fields


class HrKhenThuongKyLuat(models.Model):
    _name = 'hr.khen.thuong.ky.luat'
    _description = 'Khen thưởng & Kỷ luật'

    nhan_vien_id = fields.Many2one('nhan.vien', required=True)
    loai_quyet_dinh = fields.Selection([
        ('thuong', 'Thuận thưởng'),
        ('phat', 'Kỷ luật phạt')
    ], required=True)

    so_tien = fields.Float(required=True)
    ngay_ap_dung = fields.Date(required=True)
