import frappe
from frappe.utils import now, add_days
import random

def insert_employee_checkin():
    # List of all employee check-ins to be inserted TEST
    employee_checkin_data = [
    # Regular Workday before a Regular Holiday (shift from 19:00 to 4:00)
    {'employee': '33831242', 'time': '2023-12-23 19:00:00', 'log_type': 'IN'},  # Night shift start before Christmas Day (Saturday)
    {'employee': '33831242', 'time': '2023-12-24 04:00:00', 'log_type': 'OUT'},  # Night shift end (Sunday)

    # Regular Holiday Overtime with Attendance on the Previous Day
    {'employee': '33831242', 'time': '2023-12-24 19:00:00', 'log_type': 'IN'},  # Night shift start on Christmas Day (Sunday)
    {'employee': '33831242', 'time': '2023-12-25 05:00:00', 'log_type': 'OUT'},  # Night shift end with 1 hour overtime (Monday)

    # Regular Workday before a Special Non-Working Holiday (shift from 19:00 to 4:00)
    {'employee': '33831242', 'time': '2023-10-30 19:00:00', 'log_type': 'IN'},  # Night shift start before All Saints' Day (Monday)
    {'employee': '33831242', 'time': '2023-10-31 04:00:00', 'log_type': 'OUT'},  # Night shift end (Tuesday)

    # Special Non-Working Holiday Overtime with Attendance on the Previous Day
    {'employee': '33831242', 'time': '2023-10-31 19:00:00', 'log_type': 'IN'},  # Night shift start on All Saints' Day (Tuesday)
    {'employee': '33831242', 'time': '2023-11-01 06:00:00', 'log_type': 'OUT'},  # Night shift end with 2 hours overtime (Wednesday)

    # Regular Workday before Combined Regular Holiday and Rest Day (shift from 19:00 to 4:00)
    {'employee': '33831242', 'time': '2023-12-28 19:00:00', 'log_type': 'IN'},  # Night shift start before Rizal Day (Thursday)
    {'employee': '33831242', 'time': '2023-12-29 04:00:00', 'log_type': 'OUT'},  # Night shift end (Friday)

    # Combined Regular Holiday and Rest Day Overtime with Attendance on the Previous Day
    {'employee': '33831242', 'time': '2023-12-29 19:00:00', 'log_type': 'IN'},  # Night shift start on Rizal Day (Friday)
    {'employee': '33831242', 'time': '2023-12-30 07:00:00', 'log_type': 'OUT'},  # Night shift end with 3 hours overtime (Saturday)

    # Regular Workday before Combined Special Non-Working Holiday and Rest Day (shift from 19:00 to 4:00)
    {'employee': '33831242', 'time': '2023-02-07 19:00:00', 'log_type': 'IN'},  # Night shift start before Chinese New Year (Tuesday)
    {'employee': '33831242', 'time': '2023-02-08 04:00:00', 'log_type': 'OUT'},  # Night shift end (Wednesday)

    # Combined Special Non-Working Holiday and Rest Day Overtime with Attendance on the Previous Day
    {'employee': '33831242', 'time': '2023-02-08 19:00:00', 'log_type': 'IN'},  # Night shift start on Chinese New Year (Wednesday)
    {'employee': '33831242', 'time': '2023-02-09 06:00:00', 'log_type': 'OUT'},  # Night shift end with 2 hours overtime (Thursday)
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
