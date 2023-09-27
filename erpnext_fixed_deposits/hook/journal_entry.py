import frappe

def permission_query(user):
	if "All Doc" in frappe.get_roles(user):
		return None
	else:
		return """`tabJournal Entry`.owner='{user}' or `tabJournal Entry`._assign like '%{user}%'""".format(user=user)