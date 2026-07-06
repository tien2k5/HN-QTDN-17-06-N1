from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_va_ten'
    _order = 'ten asc, tuoi desc'

    ma_dinh_danh = fields.Char(
        "Mã định danh",
        required=True
    )

    ho_ten_dem = fields.Char(
        "Họ tên đệm",
        required=True
    )

    ten = fields.Char(
        "Tên",
        required=True
    )

    ho_va_ten = fields.Char(
        "Họ và tên",
        compute="_compute_ho_va_ten",
        store=True
    )

    ngay_sinh = fields.Date("Ngày sinh")

    tuoi = fields.Integer(
        "Tuổi",
        compute="_compute_tuoi",
        store=True
    )

    que_quan = fields.Char("Quê quán")

    email = fields.Char("Email")

    so_dien_thoai = fields.Char("Số điện thoại")

    anh = fields.Binary("Ảnh")

    lich_su_cong_tac_ids = fields.One2many(
        "lich_su_cong_tac",
        "nhan_vien_id",
        string="Lịch sử công tác"
    )

    danh_sach_chung_chi_bang_cap_ids = fields.One2many(
        "danh_sach_chung_chi_bang_cap",
        "nhan_vien_id",
        string="Danh sách chứng chỉ"
    )

    so_nguoi_bang_tuoi = fields.Integer(
        string="Số người bằng tuổi",
        compute="_compute_so_nguoi_bang_tuoi",
        store=True
    )

    # ================= ERP =================

    khach_hang_ids = fields.One2many(
        "khach_hang",
        "nhan_vien_phu_trach",
        string="Khách hàng phụ trách"
    )

    cong_viec_ids = fields.One2many(
        "cong_viec",
        "nhan_vien_id",
        string="Công việc"
    )

    tong_khach_hang = fields.Integer(
        string="Tổng khách hàng",
        compute="_compute_kpi"
    )

    tong_cong_viec = fields.Integer(
        string="Tổng công việc",
        compute="_compute_kpi"
    )

    cong_viec_hoan_thanh = fields.Integer(
        string="Công việc hoàn thành",
        compute="_compute_kpi"
    )

    _sql_constraints = [
        (
            'ma_dinh_danh_unique',
            'unique(ma_dinh_danh)',
            'Mã định danh phải là duy nhất'
        )
    ]

    @api.depends("ho_ten_dem", "ten")
    def _compute_ho_va_ten(self):
        for record in self:
            if record.ho_ten_dem and record.ten:
                record.ho_va_ten = f"{record.ho_ten_dem} {record.ten}"
            else:
                record.ho_va_ten = False

    @api.depends("ngay_sinh")
    def _compute_tuoi(self):
        for record in self:
            if record.ngay_sinh:
                record.tuoi = date.today().year - record.ngay_sinh.year
            else:
                record.tuoi = 0
@api.depends("tuoi")
def _compute_so_nguoi_bang_tuoi(self):
    for record in self:
        if not record.tuoi:
            record.so_nguoi_bang_tuoi = 0
            continue

        if record.id and not isinstance(record.id, int):
            record.so_nguoi_bang_tuoi = 0
            continue

        domain = [
            ("tuoi", "=", record.tuoi)
        ]

        if record.id:
            domain.append(("id", "!=", record.id))

        record.so_nguoi_bang_tuoi = self.search_count(domain)
    @api.depends(
        "khach_hang_ids",
        "cong_viec_ids",
        "cong_viec_ids.trang_thai"
    )
    def _compute_kpi(self):
        for record in self:

            record.tong_khach_hang = len(record.khach_hang_ids)

            record.tong_cong_viec = len(record.cong_viec_ids)

            record.cong_viec_hoan_thanh = len(
                record.cong_viec_ids.filtered(
                    lambda x: x.trang_thai == "hoan_thanh"
                )
            )

    @api.onchange("ten", "ho_ten_dem")
    def _default_ma_dinh_danh(self):
        for record in self:
            if record.ho_ten_dem and record.ten:
                chu_cai = ''.join(
                    x[0]
                    for x in record.ho_ten_dem.lower().split()
                )
                record.ma_dinh_danh = record.ten.lower() + chu_cai

    @api.constrains("tuoi")
    def _check_tuoi(self):
        for record in self:
            if record.tuoi < 18:
                raise ValidationError(
                    "Tuổi không được bé hơn 18"
                )
