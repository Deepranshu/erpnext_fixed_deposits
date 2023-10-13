# Copyright (c) 2023, Hybrowlabs Technologies and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import getdate

class BankTransfer(Document):
	pass
	# def validate(self):
	# 	self.bank_balance_from = get_balance_on(self.account_from, today(), cost_center=None)



# # @frappe.whitelist()
# # def naming_series(name):
#     # doc = name
#     doc = frappe.get_doc("Bank Transfer",doc)
#     month = frappe.utils.formatdate(doc.custom_posting_date, "MM")
#     year = frappe.utils.formatdate(doc.custom_posting_date, "YY")

#     doc.naming_series = make_autoname(("BT")+("-")+str(month)+("-")+str(".YY.")+("-")+str(".#####").upper())

# @frappe.whitelist()
# def autoname_series(self, method):
#     month = frappe.utils.formatdate(self.custom_posting_date, "MM")
# 	# year = frappe.utils.formatdate(self.custom_posting_date, "YY")
#     if self. is_new():
#         naming_series = ("BT")+("-")+str(month)+("-")+str(".YY.")+("-")
#         self.name = make_autoname(naming_series + ".####")
