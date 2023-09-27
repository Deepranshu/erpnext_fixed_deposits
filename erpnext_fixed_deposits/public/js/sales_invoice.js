frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
	    if(!cur_frm.is_new()){
    	    if((frappe.user_roles.includes("Taxation User"))&&(frm.selected_doc.workflow_state=="E-Invoice Pending")){
        	    frm.add_custom_button(__('Book e-Invoice'), function () {
        			frappe.call({
        				method: "erpnext_fixed_deposits.erpnext_fixed_deposits.si_controll_number.book_e_invoice",
        				args: {
        					name: frm.selected_doc.name,
        				},
        				callback: function (r) {
        				    location.reload()
        
        				}
        			})
        		},__("Generate"));
    	    }
    	  if((frappe.user_roles.includes("Taxation User"))&&(frm.selected_doc.workflow_state=="Update Control Number by Taxation User")){
    	        frm.add_custom_button(__('Generate Control Number'), function () {
        			frappe.call({
        				method: "erpnext_fixed_deposits.erpnext_fixed_deposits.si_controll_number.generate_control_number",
        				args: {
        					name: frm.selected_doc.name,
        				},
        				callback: function (r) {
        				    location.reload()
        
        				}
        			})
        		},__("Generate"));
    	    }
	    }
	    if(cur_frm.is_new()){
    	    frm.set_value("company_address"," ")
    	    //frm.set_value("shipping_address"" ")
	    }
	   //  frm.set_query('item_code', 'items', () => {
        // return {
              // filters: [
				//	['Item', 'item_name', '=', "Services"]
			//	]
        // }
        // })
        frm.set_query("custom_gst_debit_to", function() {
            return {
                "filters": {
                    "is_group": 0,
                    "company":frm.selected_doc.company
                }
            };
        });

        // Calculate Advance Tax deduction
	    // if(frm.doc.custom_total_advance_tax != 0 || frm.doc.custom_total_advance_tax != undefined){
	    //     calculate_advance_tax_deduction(frm);
	    // }
        // Calculate Advance Tax deduction
	    calculate_advance_tax_deduction(frm);
		
	},
	before_save: function(frm){
	    // Calculate Taxes on before save
        calculate_advance_tax(frm);
        
        // Calculate Allocated advance
        calculate_advance_allocated_amount(frm);
	},
	customer_address: function(frm) {
		
        // Get the selected value of the custom select field
        //var selectedValue = frm.doc.billing_address_gstin;
        // console.log(selectedValue);
		// if(selectedValue!="undefined"){
		// 	frm.doc.custom_customer_gst = selectedValue
		// }
		//frm.doc.custom_customer_gst = selectedValue
        // Do something with the selected value
        // if (selectedValue === 'Option 1') {
        //     // Perform actions when Option 1 is selected
        // } else if (selectedValue === 'Option 2') {
        //     // Perform actions when Option 2 is selected
        // }
    }
})

frappe.ui.form.on('Sales Invoice Advance', {
	allocated_amount: function(frm,cdt,cdn) {
	    // Calculate tax amount
		calculate_tax_amount(frm,cdt,cdn);
	}
});

// Function to Calculate tax amount from taxable value
function calculate_tax_amount(frm,cdt,cdn){
    let local_variable = locals[cdt][cdn];
    let reference_type = local_variable.reference_type;
    let allocated_amount = local_variable.allocated_amount;
    let advance_tax = 0;
    let final_advance_tax = 0;
    if(reference_type == 'Payment Entry'){
        frappe.call({
            'method': 'frappe.client.get',
            'args':{
                'doctype': 'Payment Entry',
                'filters':{
                    'name': local_variable.reference_name
                }
            },
            callback: function(r){
                let taxes = r.message.taxes;
                taxes.forEach(function(item,index){
                    if(item.account_head == 'Output Tax SGST - WL' || item.account_head == 'Output Tax CGST - WL' || item.account_head == 'Output Tax IGST - WL'){
                        advance_tax = (allocated_amount * item.rate)/100;
                        final_advance_tax += advance_tax;
                    }
                });
                frappe.model.set_value(cdt,cdn,'advance_deduction_',final_advance_tax);
            }
        });
    }
}

// Function to Calculate tax amount from taxable value
function calculate_advance_tax(frm) {
    let advance_table = frm.doc.advances;
    if (advance_table !== undefined) {
        advance_table.forEach(function (item, index) {
            let allocated_amount = item.allocated_amount;
            if (item.reference_type == 'Payment Entry') {
                frappe.call({
                    'method': 'frappe.client.get',
                    'args': {
                        'doctype': 'Payment Entry',
                        'filters': {
                            'name': item.reference_name
                        }
                    },
                    callback: function (r) {
                        let taxes = r.message.taxes;
                        let final_advance_tax = 0;
                        taxes.forEach(function (taxItem, taxIndex) {
                            let advance_tax = 0;
                            if (taxItem.account_head == 'Output Tax SGST - WL' || taxItem.account_head == 'Output Tax CGST - WL' || taxItem.account_head == 'Output Tax IGST - WL') {
                                advance_tax = (allocated_amount * taxItem.rate) / 100;
                                final_advance_tax += advance_tax;
                            }
                        });
                        item.advance_deduction_ = final_advance_tax;
                    }
                });
            }
        });
    }
}

// Function to calculate total allocated amount and total advance deduction from advances
function calculate_advance_allocated_amount(frm){
    let advances = frm.doc.advances;
    let total_allocated_advance = 0;
    if (advances !== undefined) {
        advances.forEach(function(item,index){
            total_allocated_advance += item.allocated_amount;
        });
    }
    frm.set_value('custom_total_allocated_advance',total_allocated_advance);
    frm.refresh_fields('custom_total_allocated_advance');
}

// Function to calculate total advance deduction from advances
function calculate_advance_tax_deduction(frm){
    let advances = frm.doc.advances;
    let total_advance_tax = 0;
    if(advances.length !== 0){
        advances.forEach(function(item,index){
            total_advance_tax += item.advance_deduction_;
        });
    }
    frm.set_value('custom_total_advance_tax',total_advance_tax);
    frm.refresh_fields('custom_total_advance_tax');
}