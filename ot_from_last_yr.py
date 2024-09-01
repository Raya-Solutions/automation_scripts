import frappe
from frappe.utils import now, add_days
import random

def insert_employee_checkin():
    # List of all employee check-ins to be inserted TEST
    employee_checkin_data = [
    # Regular Workdays (Monday to Saturday) with no overtime
    {'employee': '11831242', 'time': '2023-06-03 07:16:24', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-06-03 15:43:35', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-04 07:16:26', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-06-04 15:43:37', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-05 07:16:28', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-06-05 15:43:38', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-06 07:16:30', 'log_type': 'IN'},  # Thursday
    {'employee': '11831242', 'time': '2023-06-06 15:43:39', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-07 07:16:32', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-06-07 15:43:40', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-08 07:16:34', 'log_type': 'IN'},  # Saturday
    {'employee': '11831242', 'time': '2023-06-08 15:43:41', 'log_type': 'OUT'},

    # Ordinary Day Overtime (Monday)
    {'employee': '11831242', 'time': '2023-06-10 08:00:01', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-06-10 19:00:01', 'log_type': 'OUT'},  # 3 hours overtime

    # Regular Days between overtime scenarios to ensure continuity of work presence
    {'employee': '11831242', 'time': '2023-06-11 07:16:35', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-06-11 15:43:42', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-06-12 07:16:36', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-06-12 15:43:43', 'log_type': 'OUT'},
    
    # Rest Day Overtime (in excess of 8hrs) (Sunday) - Fail
    {'employee': '11831242', 'time': '2023-06-16 08:00:02', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-06-16 21:00:02', 'log_type': 'OUT'},  # 5 hours overtime on rest day

    # Regular Days before the next overtime scenario
    {'employee': '11831242', 'time': '2023-08-19 07:16:37', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-08-19 15:43:44', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-08-20 07:16:38', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-08-20 15:43:45', 'log_type': 'OUT'},
    
    # Special Non-Working Holiday Overtime (in excess of 8hrs) (Ninoy Aquino Day) - Fail
    {'employee': '11831242', 'time': '2023-08-21 08:00:03', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-08-21 22:00:03', 'log_type': 'OUT'},  # 6 hours overtime on a special holiday

    # Regular Days before the next overtime scenario
    {'employee': '11831242', 'time': '2023-08-22 07:16:39', 'log_type': 'IN'},  # Thursday
    {'employee': '11831242', 'time': '2023-08-22 15:43:46', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-08-23 07:16:40', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-08-23 15:43:47', 'log_type': 'OUT'},

    # Regular Holiday Overtime (in excess of 8hrs) (National Heroes Day)
    {'employee': '11831242', 'time': '2023-08-26 08:00:04', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-08-26 22:00:04', 'log_type': 'OUT'},  # 6 hours overtime on regular holiday

    # Regular Days before the next overtime scenario
    {'employee': '11831242', 'time': '2023-12-23 07:16:41', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-12-23 15:43:48', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-12-24 07:16:42', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-12-24 15:43:49', 'log_type': 'OUT'},

    # Double Holiday Overtime (Christmas Day and Rizal Day) - 
    {'employee': '11831242', 'time': '2023-12-25 08:00:05', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-12-25 17:00:05', 'log_type': 'OUT'},  # 1 hour overtime

    # Regular Day to ensure continuity before the next special day scenario
    {'employee': '11831242', 'time': '2023-12-27 07:16:43', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-12-27 15:43:50', 'log_type': 'OUT'},

    # Double Holiday and Rest Day Overtime (Christmas Day and Rest Day on Sunday)
    {'employee': '11831242', 'time': '2023-12-29 08:00:06', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-12-29 18:00:06', 'log_type': 'OUT'},  # 2 hours overtime

    # Regular Workdays before next scenario
    {'employee': '11831242', 'time': '2023-02-07 07:16:44', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-02-07 15:43:51', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-02-08 07:16:45', 'log_type': 'IN'},  # Thursday
    {'employee': '11831242', 'time': '2023-02-08 15:43:52', 'log_type': 'OUT'},

    # Special Non-Working Holiday Premium (Monthly Paid, EDSA People Power Revolution Anniversary)
    {'employee': '11831242', 'time': '2023-02-25 08:00:07', 'log_type': 'IN'},  # Saturday
    {'employee': '11831242', 'time': '2023-02-25 17:00:07', 'log_type': 'OUT'},  # Monthly paid special holiday

    # Regular Workdays before next scenario
    {'employee': '11831242', 'time': '2023-02-05 07:16:46', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-02-05 15:43:53', 'log_type': 'OUT'},
    {'employee': '11831242', 'time': '2023-02-06 07:16:47', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-02-06 15:43:54', 'log_type': 'OUT'},

    # Special Non-Working Holiday (Daily Paid, Chinese New Year)
    {'employee': '11831242', 'time': '2023-02-10 08:00:08', 'log_type': 'IN'},  # Saturday
    {'employee': '11831242', 'time': '2023-02-10 17:00:08', 'log_type': 'OUT'},  # Daily paid special holiday

    # Regular Day before the next holiday workday
    {'employee': '11831242', 'time': '2023-06-21 07:16:48', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-06-21 15:43:55', 'log_type': 'OUT'},

    # Rest Day (Sunday)
    {'employee': '11831242', 'time': '2023-06-23 08:00:09', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-06-23 17:00:09', 'log_type': 'OUT'},  # Worked on rest day

    # Regular Day before holiday workday scenario
    {'employee': '11831242', 'time': '2023-06-11 07:16:49', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-06-11 15:43:56', 'log_type': 'OUT'},

    # Regular Holiday Premium (Independence Day)
    {'employee': '11831242', 'time': '2023-06-12 08:00:10', 'log_type': 'IN'},  # Wednesday
    {'employee': '11831242', 'time': '2023-06-12 18:00:10', 'log_type': 'OUT'},  # 2 hours overtime on regular holiday

    # Regular Day before holiday workday scenario
    {'employee': '11831242', 'time': '2023-11-28 07:16:50', 'log_type': 'IN'},  # Thursday
    {'employee': '11831242', 'time': '2023-11-28 15:43:57', 'log_type': 'OUT'},

    # Regular Holiday that falls on Special Holiday Premium (Bonifacio Day)
    {'employee': '11831242', 'time': '2023-11-30 08:00:11', 'log_type': 'IN'},  # Saturday
    {'employee': '11831242', 'time': '2023-11-30 17:00:11', 'log_type': 'OUT'},  # Regular holiday coinciding with special holiday

    # Regular Day before next holiday workday scenario
    {'employee': '11831242', 'time': '2023-03-29 07:16:51', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-03-29 15:43:58', 'log_type': 'OUT'},

    # Regular Holiday Rest Day Overtime (in excess of 8hrs) (Easter Sunday)
    {'employee': '11831242', 'time': '2023-03-31 08:00:12', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-03-31 19:00:12', 'log_type': 'OUT'},  # 3 hours overtime on rest day during a regular holiday

    # Regular Day before next holiday workday scenario
    {'employee': '11831242', 'time': '2023-11-01 07:16:52', 'log_type': 'IN'},  # Friday
    {'employee': '11831242', 'time': '2023-11-01 15:43:59', 'log_type': 'OUT'},

    # Special Non-Working Holiday that falls on Rest Day (All Saints' Day)
    {'employee': '11831242', 'time': '2023-11-03 08:00:13', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-11-03 17:00:13', 'log_type': 'OUT'},  # Special holiday on rest day

    # Regular Day before next holiday workday scenario
    {'employee': '11831242', 'time': '2023-10-31 07:16:53', 'log_type': 'IN'},  # Thursday
    {'employee': '11831242', 'time': '2023-10-31 15:44:00', 'log_type': 'OUT'},

    # Special Non-Working Holiday that falls on Rest Day (in excess of 8hrs) (All Souls' Day)
    {'employee': '11831242', 'time': '2023-11-02 08:00:14', 'log_type': 'IN'},  # Saturday
    {'employee': '11831242', 'time': '2023-11-02 19:00:14', 'log_type': 'OUT'},  # 3 hours overtime beyond 8 hours

    # Monthly Paid Night Differential in excess of 7PM to 4AM Work Schedule
    {'employee': '11831242', 'time': '2023-06-25 20:00:15', 'log_type': 'IN'},  # Tuesday
    {'employee': '11831242', 'time': '2023-06-26 02:00:15', 'log_type': 'OUT'},  # Night differential from 8 PM to 2 AM

    # Regular Holiday, Special Holiday & Rest Day Premium (Christmas Eve on Sunday)
    {'employee': '11831242', 'time': '2023-12-24 08:00:16', 'log_type': 'IN'},  # Sunday
    {'employee': '11831242', 'time': '2023-12-24 20:00:16', 'log_type': 'OUT'},  # 4 hours overtime on regular holiday, special holiday, and rest day

    # Double Regular Holiday Premium (Rizal Day and New Year's Eve)
    {'employee': '11831242', 'time': '2023-12-30 08:00:17', 'log_type': 'IN'},  # Monday
    {'employee': '11831242', 'time': '2023-12-30 18:00:17', 'log_type': 'OUT'},  # 2 hours overtime on double regular holiday
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
