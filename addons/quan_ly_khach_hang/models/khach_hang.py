from odoo import models, fields, api


class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Thông tin khách hàng'

    ma_khach_hang = fields.Char(
        string='Mã khách hàng',
        required=True
    )

    ten_khach_hang = fields.Char(
        string='Tên khách hàng',
        required=True
    )

    so_dien_thoai = fields.Char(
        string='Số điện thoại'
    )

    email = fields.Char(
        string='Email'
    )

    dia_chi = fields.Text(
        string='Địa chỉ'
    )

    trang_thai = fields.Selection(
        [
            ('moi', 'Mới'),
            ('dang_cham_soc', 'Đang chăm sóc'),
            ('da_ky_hop_dong', 'Đã ký hợp đồng'),
            ('dang_trien_khai', 'Đang triển khai'),
            ('hoan_thanh', 'Hoàn thành')
        ],
        default='moi',
        string='Trạng thái'
    )

    nhan_vien_phu_trach = fields.Many2one(
        'nhan_vien',
        string='Nhân viên phụ trách'
    )

    # ================= ERP =================

    cong_viec_ids = fields.One2many(
        'cong_viec',
        'khach_hang_id',
        string='Danh sách công việc'
    )

    so_cong_viec = fields.Integer(
        string='Số công việc',
        compute='_compute_so_cong_viec'
    )

    @api.depends('cong_viec_ids')
    def _compute_so_cong_viec(self):
        for record in self:
            record.so_cong_viec = len(record.cong_viec_ids)

    def tao_cong_viec(self):
        """
        Tự động sinh công việc từ khách hàng
        """

        for record in self:

            # tránh tạo trùng
            if record.cong_viec_ids:
                continue

            self.env['cong_viec'].create({

                'ten_cong_viec':
                    'Chăm sóc khách hàng - %s' % record.ten_khach_hang,

                'mo_ta':
                    'Theo dõi và chăm sóc khách hàng %s'
                    % record.ten_khach_hang,

                'khach_hang_id':
                    record.id,

                'nhan_vien_id':
                    record.nhan_vien_phu_trach.id
                    if record.nhan_vien_phu_trach else False,

                'trang_thai':
                    'moi'

            })

            record.trang_thai = 'dang_trien_khai'

    def action_xem_cong_viec(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Công việc',
            'res_model': 'cong_viec',
            'view_mode': 'tree,form',
            'domain': [('khach_hang_id', '=', self.id)],
        }
