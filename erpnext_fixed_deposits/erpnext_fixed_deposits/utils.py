import frappe


def sales_invoice(user):
    if not user:
        user = frappe.session.user
    roles = frappe.get_roles(user)
    if "Administrator" not in roles:
        return "IF(`tabSales Invoice`.workflow_state='Draft',`tabSales Invoice`.owner ='%s',`tabSales Invoice`.owner IS NOT NULL)"%user

def purchase_invoice(user):
    if not user:
        user = frappe.session.user
    roles = frappe.get_roles(user)
    if "Administrator" not in roles:
        return "IF(`tabPurchase Invoice`.workflow_state='Pending',`tabPurchase Invoice`.owner ='%s',`tabPurchase Invoice`.owner IS NOT NULL)"%user

def journal_entry(user):
    if not user:
        user = frappe.session.user
    roles = frappe.get_roles(user)
    if "Administrator" not in roles:
        return "IF(`tabJournal Entry`.workflow_state='Pending',`tabJournal Entry`.owner ='%s',`tabJournal Entry`.owner IS NOT NULL)"%user