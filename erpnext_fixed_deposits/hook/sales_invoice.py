import frappe

def get_taxable_tax_amount(doc,method):
    if doc.get_doc_before_save():
        old_doc = doc.get_doc_before_save()
        if old_doc.workflow_state == "Pending" and doc.workflow_state =="Approved":
            if not doc.all_document_are_verfied:
                frappe.throw("Please accept that all documents have been verified.")
    total_taxable_value = 0 #Taxable Value
    total_tax_value = 0 #tax value
    if doc.advances:
        for item in doc.advances:
              total_taxable_value = total_taxable_value + item.custom_taxable_value
              total_tax_value = total_tax_value + item.custom_tax_value
    
    doc.advance_tax =  total_tax_value
    doc.advance_value_ =  total_taxable_value        
    
def validate_outstanding_amount(doc,method):
    # frappe.log_error("test","hi test")
    if doc.get_doc_before_save():
        old_doc = doc.get_doc_before_save()
        if old_doc.workflow_state == "Pending" and doc.workflow_state =="Approved":
            if not doc.all_document_are_verfied:
                frappe.throw("Please accept that all documents have been verified.")
    advance_deduction = 0
    #if doc.advances:
    #    for item in doc.advances:
            # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
            # item.advance_deduction_ = doc_rec already comment
            # doc_rec  = frappe.get_doc(item.reference_type,item.reference_name)
            # per = item.allocated_amount/doc_rec.paid_amount
            # amt = doc_rec.total_taxes_and_charges*per
            # item.advance_deduction_ = amt
            # advance_deduction = advance_deduction +amt
    #        advance_deduction +=item.custom_tax_value
    
                   
    # doc.custom_total_taxes_and_charges_before_deduction = doc.base_total_taxes_and_charges
    # doc.total_taxes_and_charges = doc.custom_total_taxes_and_charges_before_deduction-advance_deduction
    # total_taxes_and_charges_= doc.total_taxes_and_charges
    # doc.base_total_taxes_and_charges = total_taxes_and_charges_
    # grand_total_= doc.grand_total
    # doc.grand_total = doc.total +  doc.total_taxes_and_charges
    # grand_total = doc.grand_total
    # doc.rounded_total = doc.grand_total
    # doc.in_words = frappe.utils.money_in_words(doc.grand_total)
    doc.outstanding_amount = doc.grand_total - doc.total_advance
    #doc.total = grand_total - total_taxes_and_charges_
    
# def tax_amount_overwrite(doc,method):
#     if doc.get_doc_before_save():
#         if doc.advances:
#             total = 0
#             totalTax = 0
#             for item in doc.advances:
#             # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
#             # item.advance_deduction_ = doc_rec
#                 total+= item.advance_deduction_   
#             #final = doc.total_taxes_and_charges_before_deduction - total
            
#             for taxesIteam in doc.taxes:
#                 totalTax +=taxesIteam.tax_amount
                
#             final = totalTax - total
#             doc.total_taxes_and_charges = final
# def tax_amount_overwrite_database(doc,method):
    
#     if doc.advances:
#         total = 0
#         totalTax = 0
#         for item in doc.advances:
#         # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
#         # item.advance_deduction_ = doc_rec
#             total+= item.advance_deduction_   
#         #final = doc.total_taxes_and_charges_before_deduction - total
            
#         for taxesIteam in doc.taxes:
#             totalTax +=taxesIteam.tax_amount
                
#         final = totalTax - total
#         #doc.total_taxes_and_charges = final
#         doc.db_set('total_taxes_and_charges', final)
#         doc.db_set('base_total_taxes_and_charges',final)
#         outstanding_amt = doc.grand_total - (doc.total_taxes_and_charges + doc.total_advance)
#         doc.db_set('outstanding_amount',outstanding_amt)
        
def validate_outstanding_after_amount(doc,method):
    # frappe.log_error("test","hi test")
    advance_deduction = 0
    #if doc.advances:
        #for item in doc.advances:
            # doc_rec  = frappe.db.get_value(item.reference_type,item.reference_name,'total_taxes_and_charges')
            # item.advance_deduction_ = doc_rec
            # doc_rec  = frappe.get_doc(item.reference_type,item.reference_name)
            # per = item.allocated_amount/doc_rec.paid_amount
            # amt = doc_rec.total_taxes_and_charges*per
            # item.advance_deduction_ = amt
            # advance_deduction = advance_deduction +amt
            # advance_deduction +=item.custom_tax_value
            
            
    # frappe.log_error(str(advance_deduction),"advance_deduction")        
    # doc.total_taxes_and_charges_before_deduction = doc.base_total_taxes_and_charges
    #doc.total_taxes_and_charges = doc.custom_total_taxes_and_charges_before_deduction-advance_deduction
    # if advance_deduction < 0:
    #     doc.total_taxes_and_charges = doc.total_taxes_and_charges_before_deduction+advance_deduction
    # else:
    #     doc.total_taxes_and_charges = doc.total_taxes_and_charges_before_deduction-advance_deduction
    
    # doc.db_set('total_taxes_and_charges', doc.total_taxes_and_charges)
    # doc.db_set('base_total_taxes_and_charges', doc.total_taxes_and_charges)
    # total = (doc.total + doc.total_taxes_and_charges)
    # doc.db_set('base_grand_total', total)
    # doc.db_set('grand_total', total)
    # doc.db_set('base_rounded_total',total)
    # doc.db_set('rounded_total',total)
    # outstanding_amount = (doc.grand_total - doc.total_advance)
    # doc.db_set('outstanding_amount',outstanding_amount)
    # in_words = frappe.utils.money_in_words(outstanding_amount)
    # doc.db_set('base_in_words',in_words)
    # doc.db_set('in_words',in_words)
    # doc.outstanding_amount = outstanding_amount
    
    doc.db_set('total_taxes_and_charges', doc.total_taxes_and_charges)
    doc.db_set('base_total_taxes_and_charges', doc.total_taxes_and_charges)
    total = (doc.total + doc.total_taxes_and_charges)
    doc.db_set('base_grand_total', total)
    doc.db_set('grand_total', total)
    outstanding_amount = (doc.grand_total - doc.total_advance)
    doc.db_set('outstanding_amount',outstanding_amount)
    
    #validate_outstanding_general_ledger_amount(doc,method)
    
    
    # frappe.log_error(str(advance_deduction),"advance_deduction")
    # total_taxes_and_charges_= doc.total_taxes_and_charges
    # doc.base_total_taxes_and_charges = total_taxes_and_charges_
    # grand_total_= doc.grand_total
    # doc.grand_total = grand_total_ - advance_deduction
    #grand_total = doc.grand_total
    # doc.rounded_total = doc.grand_total
    # doc.in_words = frappe.utils.money_in_words(doc.grand_total)
    # doc.outstanding_amount = grand_total - doc.total_advance
    
def validate_outstanding_general_ledger_amount(doc,method):
    
    #sales_inv = frappe.get_doc("Sales Invoice",entry['voucher_no'])
    # Get the name (ID) of the submitted Sales Invoice
    invoice_name_to_fetch = doc.name  # Replace this with the actual Sales Invoice name
    frappe.log_error(doc.name,"invoice_name_to_fetch 1")
    fetched_invoice = fetch_sales_invoice_by_name(invoice_name_to_fetch)
    if(doc.total_advance > 0):
        if doc.advances:
            allocated_amount= 0
            advance_deduction = 0
            for item in doc.advances:
                doc_rec  = frappe.get_doc(item.reference_type,item.reference_name)
                allocated_amount = allocated_amount + item.allocated_amount
                advance_deduction = advance_deduction + item.advance_deduction_
        credit=0 
        credit_in_account_currency=0
        debit =0 
        debit_in_account_currency=0 
        creditTax=0
        creditTax_in_account_currency=0
        if(len(fetched_invoice)!=0):
            for data in fetched_invoice:
                # if (data["account"]==doc.debit_to): # Debit To
                #     # Update the 'status' column to the new_status for the given id
                #     credit = (doc.total - doc.total_advance)
                #     CreditQuery = "UPDATE `tabGL Entry` SET debit = %s,debit_in_account_currency=%s WHERE name = %s and account = %s AND voucher_type= %s ;"
                #     frappe.db.sql(CreditQuery, (credit,credit,data["name"],doc.debit_to,'Sales Invoice'))
                    #frappe.log_error(str(data["credit"]),"invoice_name_to_fetch")
                if(data["account"]==doc.gst_debit_to):   
                    debit = doc.total_taxes_and_charges
                    DebitQuery = "UPDATE `tabGL Entry` SET debit = %s,debit_in_account_currency=%s WHERE name = %s and account = %s AND voucher_type= %s ;"
                    frappe.db.sql(DebitQuery, (debit,debit, data["name"],doc.gst_debit_to,'Sales Invoice'))
                
                if(len(doc.taxes) > 1):
                    total_taxes_and_charges = doc.total_taxes_and_charges/2
                    for Itemtax in doc.taxes:
                        #frappe.log_error(str(Itemtax.account_head),"account")
                        if(Itemtax.account_head==data["account"]):
                            creditTax = total_taxes_and_charges
                            DebitTaxQuery = "UPDATE `tabGL Entry` SET credit = %s,credit_in_account_currency=%s WHERE name = %s and account = %s AND voucher_type= %s;"
                            frappe.db.sql(DebitTaxQuery, (creditTax,creditTax, data["name"],Itemtax.account_head,'Sales Invoice'))
                #for ItemOther in doc.items:
                 #   if(ItemOther.income_account==data["account"]):
                         
    
def fetch_sales_invoice_by_name(invoice_name):
    try:
        query = "SELECT name,account,cost_center,debit,credit,debit_in_account_currency,credit_in_account_currency,voucher_type,voucher_no FROM `tabGL Entry` WHERE voucher_no=%s and voucher_type='Sales Invoice' "
        values = (invoice_name)  # A tuple with the dynamic value(s)
        sales_invoice = frappe.db.sql(query, values=values,as_dict=True)

        return sales_invoice
    except frappe.DoesNotExistError:
        # If the Sales Invoice with the given name does not exist
        return None   
    
def validate(self,method=None):
     set_total_in_words(self)
    
def set_total_in_words(self):
		from frappe.utils import money_in_words
		if self.meta.get_field("custom_outstanding_in_word"):
			amount = abs(self.outstanding_amount)
			self.custom_outstanding_in_word = money_in_words(amount, self.currency)
        
    