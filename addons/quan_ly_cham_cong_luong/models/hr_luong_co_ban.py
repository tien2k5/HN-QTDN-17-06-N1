from odoo import models, fields

class HRLuongCoBan(models.Model):
    _name = 'hr.luong.co.ban'
    _description = 'Lương cơ bản nhân viên'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)

    luong_co_ban = fields.Float("Lương cơ bản", default=0.0)
    phu_cap_an_trua = fields.Float("Ăn trưa", default=0.0)
    phu_cap_trach_nhiem = fields.Float("Trách nhiệm", default=0.0)
