frappe.ui.form.on('Purchase Invoice', {
    before_save: function(frm){
        // Calculate Taxes on before save
        calculate_advance_tax(frm);
    },
    onload_post_render(frm){
        if(!frm.doc.custom_control_number){
            frm.set_value('custom_control_number',"Pending From GST Cell")
        }
        cur_frm.set_query("shipping_address", function() {
						if(cur_frm.doc.supplier) {
							return {
								query: 'frappe.contacts.doctype.address.address.address_query',
								filters: { link_doctype: 'Company', link_name: cur_frm.doc.company }
							};
						} 
					});
    },
	refresh(frm) {
	    cur_frm.set_query("shipping_address", function() {
						if(cur_frm.doc.supplier) {
							return {
								query: 'frappe.contacts.doctype.address.address.address_query',
								filters: { link_doctype: 'Company', link_name: cur_frm.doc.company }
							};
						} 
					});
	    console.log("Working")
	    if(frappe.user_roles.includes("Taxation User")){
    	    frm.add_custom_button(__('Generate Control Number'), function () {
                			frappe.call({
                				method: "erpnext_fixed_deposits.erpnext_fixed_deposits.si_controll_number.pi_control_number",
                				args: {
                					name: frm.selected_doc.name,
                				},
                				callback: function (r) {
                				    location.reload()
                
                				}
                			})
                },__("Generate"));
	    }
	    var tax_ded;
        frappe.db.get_value("Address",frm.selected_doc.billing_address,"state",function (val){
            tax_ded = val.state;
        });
        frm.set_query("tax_category", function() {
            return {
                "filters": {
                    "gst_state": tax_ded
                }
            };
        });
        frm.set_query("taxes_and_charges", function() {
            return {
                "filters": {
                    "tax_category": frm.selected_doc.tax_category
                }
            };
        });
        
    
        frm.set_query("custom_cgst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        frm.set_query("custom_sgst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        frm.set_query("custom_igst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        
        
        var tax_ded;
        frappe.db.get_value("Address",frm.selected_doc.billing_address,"state",function (val){
            tax_ded = val.state;
        });
        var supplier_address;
        frappe.db.get_value("Address",frm.selected_doc.supplier_address,"state",function (val){
            supplier_address = val.state;
            
            
            if(frm.selected_doc.docstatus !=1 || frm.selected_doc.docstatus !=2){
                if(tax_ded==supplier_address){
                    frm.set_value("custom_gst_tds_category","In State")
                }else{
                    frm.set_value("custom_gst_tds_category","Out State")
                }
                frm.refresh_fields("custom_gst_tds_category");
            }
            
        });
	    
	    
	    
	    if(cur_frm.is_new()){
    	    frm.set_value("billing_address"," ")
    	    frm.set_value("shipping_address"," ")
	    }
	    
	    
		frm.set_query("custom_gst_credit_to", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        frm.set_query("custom_cgst_tds_account", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        frm.set_query("custom_sgst_tds_account", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        frm.set_query("custom_igst_tds_account", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        frm.set_query("custom_retention_percentage_account", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        frm.set_query("custom_labour_cess_account", function() {
            return {
                "filters": {
                    "account_type": "Tax",
                    "company":frm.selected_doc.company
                }
            };
        });
        
        // var tax_ded;
        // frappe.db.get_value("Address",frm.selected_doc.billing_address,"state",function (val){
        //     console.log(val.state)
        //     tax_ded = val.state;
        // });
        // frm.set_query("tax_category", function() {
        //     return {
        //         "filters": {
        //             "gst_state": tax_ded
        //         }
        //     };
        // });
        // frm.set_query("taxes_and_charges", function() {
        //     return {
        //         "filters": {
        //             "tax_category": frm.selected_doc.tax_category
        //         }
        //     };
        // });
        

	},
	
	
	
	
	"billing_address": function(frm) {
	    var tax_ded;
        frappe.db.get_value("Address",frm.selected_doc.billing_address,"state",function (val){
            tax_ded = val.state;
        });
        frm.set_query("tax_category", function() {
            return {
                "filters": {
                    "gst_state": tax_ded
                }
            };
        });
        frm.set_query("taxes_and_charges", function() {
            return {
                "filters": {
                    "tax_category": frm.selected_doc.tax_category
                }
            };
        });
        var tax_ded;
        frappe.db.get_value("Address",frm.selected_doc.billing_address,"state",function (val){
            tax_ded = val.state;
        });
        var supplier_address;
        frappe.db.get_value("Address",frm.selected_doc.supplier_address,"state",function (val){
            supplier_address = val.state;

            if(tax_ded==supplier_address){
                frm.set_value("custom_gst_tds_category","In State")
            }else{
                frm.set_value("custom_gst_tds_category","Out State")
            }
            frm.refresh_fields("custom_gst_tds_category");
        });
        
        
        
        
        
        frm.set_query("custom_cgst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        frm.set_query("custom_sgst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        frm.set_query("custom_igst_tds_account", function() {
            return {
                "filters": {
                    "state": tax_ded
                }
            };
        });
        
        
        //  frm.set_query("supplier", function() {
        //     return {
        //         "filters": {
        //             "workflow_state": "Approved",
        //         }
        //     };
        // });  
        
        
        
        
        
        
	    
	},
    before_save: function(frm){
        // Calculate Taxes on before save
        calculate_advance_tax(frm);
    }
// 	"gst_tds": function(frm) {
	    
// 	    if ((frm.selected_doc.gst_tds)&& (!frm.selected_doc.tax_category)){
//             frappe.throw("Please select Tax Categoty")
// 	    }
// 	},
//     "cgst_tds_account": function(frm) {
//         if(frm.selected_doc.gst_tds){
// 		    if(frm.selected_doc.tax_category=="In-State"){
// 		        let temp = frm.selected_doc.cgst_tds_account
// 		        var cgst = frm.fields_dict.taxes.grid.add_new_row();
//     			frappe.model.set_value(cgst.doctype, cgst.name, "charge_type", "On Net Total");
//                 frappe.model.set_value(cgst.doctype, cgst.name, "account_head", temp);
//                 frappe.model.set_value(cgst.doctype, cgst.name, "add_deduct_tax", "Deduct");
// 		    }
            
// 			}
//     },
//     "sgst_tds_account": function(frm) {
//         if(frm.selected_doc.gst_tds){
// 		    if(frm.selected_doc.tax_category=="In-State"){
// 		        let temp = frm.selected_doc.sgst_tds_account
//                 var sgst = frm.fields_dict.taxes.grid.add_new_row();
//                 frappe.model.set_value(sgst.doctype, sgst.name, "charge_type", "On Net Total");
//     			frappe.model.set_value(sgst.doctype, sgst.name, "account_head", temp);
//     			frappe.model.set_value(sgst.doctype, sgst.name, "add_deduct_tax", "Deduct");
//                 }
            
// 			}
//     },
//     "igst_tds_account": function(frm) {
//         if(frm.selected_doc.gst_tds){
// 		    if(frm.selected_doc.tax_category=="Out-State"){
// 		        let temp = frm.selected_doc.igst_tds_account
// 		        var igst = frm.fields_dict.taxes.grid.add_new_row();
//                 frappe.model.set_value(igst.doctype, igst.name, "charge_type", "On Net Total");
//     			frappe.model.set_value(igst.doctype, igst.name, "account_head", temp);
//     			frappe.model.set_value(igst.doctype, igst.name, "add_deduct_tax", "Deduct");


// 		    }
            
// 			}
//     },
    
    // "labour_cess_account": function(frm) {
    //     if(frm.selected_doc.labour_cess_account != 'Nil'){
    //         let temp = frm.selected_doc.labour_cess_account
    //         var cess_pay = frm.fields_dict.taxes.grid.add_new_row();
    //         frappe.model.set_value(cess_pay.doctype, cess_pay.name, "charge_type", "On Net Total");
    //     	frappe.model.set_value(cess_pay.doctype, cess_pay.name, "account_head", temp);
    //     	frappe.model.set_value(cess_pay.doctype, cess_pay.name, "add_deduct_tax", "Deduct");
    // 	}
    // },
    // "retention_percentage_account": function(frm) {
    // 	if(frm.selected_doc.retention_percentage_account != 'Nil'){
    // 	    let temp = frm.selected_doc.retention_percentage_account
    // 	    var retention_row = frm.fields_dict.taxes.grid.add_new_row();
    // 	    frappe.model.set_value(retention_row.doctype, retention_row.name, "account_head", temp);
    // 		frappe.model.set_value(retention_row.doctype, retention_row.name, "charge_type", "On Net Total");
    // 		frappe.model.set_value(retention_row.doctype, retention_row.name, "add_deduct_tax", "Deduct");
    		
    // 		frappe.model.set_value(retention_row.doctype, retention_row.name, "rate", "2");
    //     }
    // }
    
    
})



frappe.ui.form.on('Purchase Invoice Advance', {
	allocated_amount: function(frm,cdt,cdn){
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
                // console.log(r.message,'message')
                let taxes = r.message.taxes;
                taxes.forEach(function(item,index){
                    advance_tax = (allocated_amount * item.rate)/100;
                    final_advance_tax += advance_tax;
                });
                frappe.model.set_value(cdt,cdn,'custom_advance_deduction',final_advance_tax);
            }
        });
    }
}

// Calculate Taxes on before save
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
                        let completedTaxCalculations = 0;
                        taxes.forEach(function (taxItem, taxIndex) {
                            let advance_tax = 0;
                            frappe.call({
                                'method': 'frappe.client.get',
                                'args': {
                                    'doctype': 'Account',
                                    'filters': {
                                        'name': taxItem.account_head
                                    }
                                },
                                callback: function (res) {
                                    if(res.message.custom_deduct_tax == 1){
                                        advance_tax = (allocated_amount * taxItem.rate) / 100;
                                        final_advance_tax += advance_tax;
                                    }
                                    completedTaxCalculations++;
                                    // Check if all tax calculations are complete
                                    if (completedTaxCalculations === taxes.length) {
                                        // Assign the final_advance_tax value to item.advance_deduction
                                        item.custom_advance_deduction = final_advance_tax;
                                    }
                                }
                            });
                        });
                    }
                });
            }
        });
    }
}