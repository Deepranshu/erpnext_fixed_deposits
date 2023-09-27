# Copyright (c) 2023, Hybrowlabs Technologies and contributors
# For license information, please see license.txt

import frappe
import calendar
import json


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data

def get_columns():
	column = [
	{"label":"Invoice No.","fieldname": "name","fieldtype": "data","width":200},
	{"label":"Supplier","fieldname": "supplier","fieldtype": "data","width":200},
	{"label":"TDS Category","fieldname": "custom_gst_tds_category","fieldtype": "data","width":100},
	{"label":"CGST TDS Account","fieldname": "custom_cgst_tds_account","fieldtype": "data","width":100},
	{"label":"CGST Amount","fieldname": "cgst_amount","fieldtype": "data","width":100},
	{"label":"SGST TDS Account","fieldname": "custom_sgst_tds_account","fieldtype": "data","width":100},
	{"label":"SGST Amount","fieldname": "sgst_amount","fieldtype": "data","width":100},
	{"label":"IGST TDS Account","fieldname": "custom_igst_tds_account","fieldtype": "data","width":100},
	{"label":"IGST Amount","fieldname": "igst_amount","fieldtype": "data","width":100},
	]
	return column

def get_conditions(filters):
	conditions = ""
	if filters.get("supplier"):
		conditions += "and so.customer = '%s'" % filters["supplier"]
	return conditions

def get_data():
    # condition = get_conditions(filters)
    data = frappe.db.sql(f"""select so.name, so.supplier, so.supplier_name,
                        so.custom_gst_tds_category, so.custom_cgst_tds_account, so.custom_sgst_tds_account, so.custom_igst_tds_account,
                        cgst.tax_amount as "cgst_amount", sgst.tax_amount as "sgst_amount", igst.tax_amount as "igst_amount",
                        MonthName(so.posting_date) as month, year(so.posting_date) as year 
                        from `tabPurchase Invoice` as so
                        left join `tabPurchase Taxes and Charges` as cgst on cgst.parent = so.name and cgst.account_head = so.custom_cgst_tds_account
                        left join `tabPurchase Taxes and Charges` as sgst on sgst.parent = so.name and sgst.account_head = so.custom_sgst_tds_account
                        left join `tabPurchase Taxes and Charges` as igst on igst.parent = so.name and igst.account_head = so.custom_igst_tds_account
						 where so.name="PINV-23-00033"
                        group by so.name""", as_dict=1)
    # frappe.msgprint(str(data))
    return data

