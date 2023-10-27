from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    hr_expense_user_account_id = fields.Many2one("res.users", string="test hi", readonly=False)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()       
        params = self.env['ir.config_parameter'].sudo()
        hr_expense_user_account_id = params.get_param('hr_expense_account_user.hr_expense_user_account_id', default=False)
        res.update(
            hr_expense_user_account_id=int(hr_expense_user_account_id),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("hr_expense_account_user.hr_expense_user_account_id", self.hr_expense_user_account_id.id)