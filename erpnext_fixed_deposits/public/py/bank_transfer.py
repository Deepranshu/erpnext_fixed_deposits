# import frappe
# from frappe.model.naming import make_autoname

# @frappe.whitelist()
# def make_naming_series_(name):
#     doc = name
#     doc = frappe.get_doc("Bank Transfer",doc)
#     month = frappe.utils.formatdate(doc.custom_posting_date, "MM")
#     # year = frappe.utils.formatdate(doc.custom_posting_date, "YY")

#     # doc.naming_series = make_autoname(("BT")+("-")+str(month)+("-")+str(".YY.")+("-")+str(".#####").upper())