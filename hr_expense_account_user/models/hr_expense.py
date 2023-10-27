from odoo import fields, models

class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    def activity_update(self):
        user_account_id = self.env["res.config.settings"].get_values().get("hr_expense_user_account_id")
        user_account_all = self.env["res.users"].search([])
        user_account = False
        for user in user_account_all:
            if user.id == user_account_id:
                user_account = user
                break
        if user_account:
            notification_ids = [((0, 0, {'res_partner_id': user_account.partner_id.id,
                                         'notification_type': 'inbox'}))]
            message = ("Expense report approve by manager")
            for expense_report in self:
                if expense_report.state == 'approve':
                    expense_report.message_post(
                           body=(message),
                           message_type='notification',
                           subtype_xmlid="mail.mt_comment",
                           notification_ids=notification_ids,
                           partner_ids=[user_account.id],
                           notify_by_email=False,
                           )
        super(HrExpenseSheet, self).activity_update()
