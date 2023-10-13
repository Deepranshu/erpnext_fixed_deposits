// Copyright (c) 2023, Hybrowlabs Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bank Transfer', {
	// refresh: function(frm) {
	// 	console.log('asdfsfsdf')
	// 	frappe.call({
	// 		method: "erpnext_fixed_deposits.erpnext_fixed_deposits.erpnext_fixed_deposits.doctype.bank_transfer.bank_transfer.naming_series",
	// 		args: {
	// 			"name":frm.doc.name
	// 		},
	// 		callback: function(r) {
	// 			console.log(r)
	// 		}
	// 	});
	// },
	account_from:function(frm) {
		frappe.call({
			method: "erpnext.accounts.utils.get_balance_on",
			args: {
				account:frm.selected_doc.account_from
			},
			callback: function(r) {
				console.log(r)
				var balance = r.message
				frm.doc.bank_balance_from = balance
				frm.refresh_field('bank_balance_from')
			}
		});
		frm.set_value("accounts","")
	},
	amount:function(frm) {
		frm.set_value("accounts","")
	},
	bank_account_to:function(frm) {
		frm.set_value("accounts","")
	}
});
