import frappe

def validate_outstanding_amount(doc,method):
    frappe.log_error("Sales Invoice Hook Test","hi test")
    if doc.get_doc_before_save():
        old_doc = doc.get_doc_before_save()
        if old_doc.workflow_state == "Pending" and doc.workflow_state =="Approved":
            if not doc.all_document_are_verfied:
                frappe.throw("Please accept that all documents have been verified.")
    advance_deduction = 0
    if doc.advances:
        for item in doc.advances:
            # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
            # item.advance_deduction_ = doc_rec
            doc_rec  = frappe.get_doc(item.reference_type,item.reference_name)
            per = item.allocated_amount/doc_rec.paid_amount
            amt = doc_rec.total_taxes_and_charges*per
            frappe.log_error(str(amt),"Amt Test")
            item.advance_deduction_ = amt
            advance_deduction = advance_deduction +amt
    doc.total_taxes_and_charges_before_deduction = doc.base_total_taxes_and_charges
    doc.total_taxes_and_charges = doc.total_taxes_and_charges_before_deduction-advance_deduction
    total_taxes_and_charges_= doc.total_taxes_and_charges
    doc.base_total_taxes_and_charges = total_taxes_and_charges_
    grand_total_= doc.grand_total
    doc.grand_total = grand_total_ - advance_deduction
    grand_total = doc.grand_total
    doc.rounded_total = doc.grand_total
    doc.in_words = frappe.utils.money_in_words(doc.grand_total)
    doc.outstanding_amount = grand_total - doc.total_advance
    
    
def validate_outstanding_after_amount(doc,method):
    # frappe.log_error("test","hi test")
    advance_deduction = 0
    if doc.advances:
        for item in doc.advances:
            # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
            # item.advance_deduction_ = doc_rec
            doc_rec  = frappe.get_doc(item.reference_type,item.reference_name)
            per = item.allocated_amount/doc_rec.paid_amount
            amt = doc_rec.total_taxes_and_charges*per
            item.advance_deduction_ = amt
            advance_deduction = advance_deduction +amt
            
            
    # frappe.log_error(str(advance_deduction),"advance_deduction")        
    # doc.total_taxes_and_charges_before_deduction = doc.base_total_taxes_and_charges
    doc.total_taxes_and_charges = doc.total_taxes_and_charges_before_deduction-advance_deduction
    doc.db_set('total_taxes_and_charges', doc.total_taxes_and_charges)
    doc.db_set('base_total_taxes_and_charges', doc.total_taxes_and_charges)
    total = (doc.total + doc.total_taxes_and_charges)
    doc.db_set('base_grand_total', total)
    doc.db_set('grand_total', total)
    outstanding_amount = (doc.grand_total - doc.total_advance)
    doc.db_set('outstanding_amount',outstanding_amount)
    
    # frappe.log_error(str(advance_deduction),"advance_deduction")
    # total_taxes_and_charges_= doc.total_taxes_and_charges
    # doc.base_total_taxes_and_charges = total_taxes_and_charges_
    # grand_total_= doc.grand_total
    # doc.grand_total = grand_total_ - advance_deduction
    #grand_total = doc.grand_total
    # doc.rounded_total = doc.grand_total
    # doc.in_words = frappe.utils.money_in_words(doc.grand_total)
    # doc.outstanding_amount = grand_total - doc.total_advance
