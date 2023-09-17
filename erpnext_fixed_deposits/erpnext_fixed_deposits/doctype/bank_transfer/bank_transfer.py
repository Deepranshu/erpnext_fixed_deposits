# Copyright (c) 2023, Hybrowlabs Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from erpnext.accounts.utils import  get_balance_on
from frappe.utils import today

class BankTransfer(Document):
	pass
	# def validate(self):
	# 	self.bank_balance_from = get_balance_on(self.account_from, today(), cost_center=None)
