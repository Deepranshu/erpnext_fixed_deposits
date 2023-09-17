import frappe
from frappe.model.naming import make_autoname

@frappe.whitelist()
def book_e_invoice(name):
    # year = frappe.utils.now_datetime().year
    doc = name
    year = 2324
    doc = frappe.get_doc("Sales Invoice",doc)
    if doc.e_invoice_number !="Pending From GST Cell":
        frappe.throw("E-Invoice already Booked")
    settings = frappe.get_doc("E-Invoice")
    s_id = frappe.db.get_value("Address",doc.company_address,'state')
    state_code = frappe.db.get_value("State",s_id,"state_code")
    doc.e_invoice_number = make_autoname(f" {'ENV/'+str(year)+'/'+str(state_code)+str('.####')}")
    # doc.e_invoice_number = f" {'ENV/'+str(year)+'/'+str(state_code)+str(settings.e_invoice_number).zfill(5)}" 
    doc.save()
    doc.reload()

    # settings.e_invoice_number = int(settings.e_invoice_number) + 1
    settings.save(ignore_permissions=True)
    
    frappe.msgprint("E-Invoice Booked") 

@frappe.whitelist()
def generate_control_number(name):
    # year = frappe.utils.now_datetime().year
    year = 2324
    doc = name
    doc = frappe.get_doc("Sales Invoice",doc)
    if doc.control_number !="Pending From GST Cell":
        frappe.throw("Control Number already Generated")
    settings = frappe.get_doc("E-Invoice")
    s_id = frappe.db.get_value("Address",doc.company_address,'state')
    state_code = frappe.db.get_value("State",s_id,"state_code")
    if doc.type == "Taxable Turnover":
        doc.control_number = make_autoname(f" {'T'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'T'+str(state_code)+'/'+str(year)+'/'+str(settings.tyyyy).zfill(4)}"
        # settings.tyyyy = int(settings.tyyyy) + 1
    elif doc.type == "Bill Of Supply":
        doc.control_number = make_autoname(f" {'BO'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'BO'+str(state_code)+'/'+str(year)+'/'+str(settings.boyyyy).zfill(4)}" 
        # settings.boyyyy = int(settings.boyyyy) + 1
    elif doc.type == "Exports":
        doc.control_number = make_autoname(f" {'ET'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'ET'+str(state_code)+'/'+str(year)+'/'+str(settings.etyyyy).zfill(4)}" 
        # settings.etyyyy = int(settings.etyyyy) + 1
    elif doc.type == "Credit Note":
        doc.control_number = make_autoname(f" {'CRN'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'CRN'+str(state_code)+'/'+str(year)+'/'+str(settings.crnyyyy).zfill(4)}" 
        # settings.crnyyyy = int(settings.crnyyyy) + 1
    elif doc.type == "Receipt Voucher":
        doc.control_number = make_autoname(f" {'R'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'R'+str(state_code)+'/'+str(year)+'/'+str(settings.ryyyy).zfill(4)}" 
        # settings.ryyyy = int(settings.ryyyy) + 1
    elif doc.type == "Non Operating Income":
        doc.control_number = make_autoname(f" {'NOI'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'NOI'+str(state_code)+'/'+str(year)+'/'+str(settings.noyyyy).zfill(4)}" 
        # settings.noyyyy = int(settings.noyyyy) + 1
    elif doc.type == "Sef Invoice":
        doc.control_number = make_autoname(f" {'S'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'S'+str(state_code)+'/'+str(year)+'/'+str(settings.syyyy).zfill(4)}" 
        # settings.syyyy = int(settings.syyyy) + 1
    elif doc.type == "E-Invoice Generated":
        doc.control_number = make_autoname(f" {'EINV'+str(state_code)+'/'+str(year)+'/.####'}")
        # doc.control_number = f" {'EINV'+str(state_code)+'/'+str(year)+'/'+str(settings.e_invoice_number).zfill(4)}" 
        # settings.einvyyyy = int(settings.einvyyyy) + 1
    doc.save()
    doc.reload()

    settings.save(ignore_permissions=True)

    frappe.msgprint("Control Number Generated")    
