// Copyright (c) 2023, Hybrowlabs Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["TDS GST booked on Supplier Bills"] = {
	"filters": [
		{
			"fieldname":"supplier",
			"label": __("Supplier"),
			"fieldtype": "Link",
			"width": "80",
			"options":"Supplier"
		},
		{
          	"fieldname": "month",
            "label": "Month",
            "fieldtype": "Select",
            "options": ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            // "default": "January"
        	},
		{
            "fieldname": "year",
            "label": "year",
            "fieldtype": "Select",
            "options": ['','2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028'],
			// "default": "2023"
	        },
	]
};
