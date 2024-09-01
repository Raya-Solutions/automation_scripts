import frappe
from frappe.utils import now, add_days
import random

def insert_employee_checkin():
    # List of all employee check-ins to be inserted TEST
    employee_checkin_data = [
        # Employee '36174'
        {'employee': '803124201', 'time': '2024-06-09 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-09 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-10 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-10 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-11 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-11 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-12 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-12 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-13 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-13 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-14 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-14 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-15 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-15 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-16 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-16 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-17 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-17 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-18 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-18 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-19 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-19 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-20 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-20 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-21 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-21 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-22 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-22 15:43:36', 'log_type': 'OUT'},
        {'employee': '803124201', 'time': '2024-06-23 07:16:24', 'log_type': 'IN'},
        {'employee': '803124201', 'time': '2024-06-23 15:43:36', 'log_type': 'OUT'},

    ]

    # Insert each check-in record into Frappe
    for record in employee_checkin_data:
        # Generate unique naming series
      
        
        # Create new Employee Checkin record
        doc = frappe.get_doc({
            'doctype': 'Employee Checkin',
            'naming_series': 'EMP-CKIN-.MM.-.YYYY.-.######',
            'employee': record['employee'],
            'time': record['time'],
            'log_type': record['log_type'],
            'skip_auto_attendance': 0,
            'device_id': 1,
            #'shift': 'Row5-6'
        })

        # Insert the document into Frappe
        doc.insert()

    frappe.db.commit()

insert_employee_checkin()
