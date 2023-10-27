{
    "name": "HR Expense Account User",
    "summary": """Add account_user""",
    "version": "16.0.1.0.0",
    "category": "Human Resoursers/Expenses",
    "website": "https://www.odoo.com/page/expenses",
    "maintainers": ["solo4games"],
    "author": "solo4games",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["hr_expense"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/hr_expense_views.xml",
        "reports/hr_expense_reports.xml"
    ],
}
