# Project: Group Task Scheduler



# Assignment Overview:

# Build a comprehensive group task scheduling application that helps teams assign tasks, detect scheduling conflicts, track progress, and export weekly plans. This project demonstrates mastery of Python data structures, functions, error handling, file I/O, and datetime manipulation.



# Required Features

# Core Functionality (Mandatory):



# 1. Team Members:  

#    - Support 2–8 team members  

#    - Collect unique names and availability (days of week) for each  

#    - Store member info in a dictionary  

#Part1 - Completed


# 2. Task Entry:  

#    - Allow adding multiple tasks with names, estimated hours, and deadline (day)  

#    - Support continuous task entry until user selects `'done'`  

#    - Track each task's requirements  



# 3. Assignment Rules:  

#    - Each task can be assigned in three ways:  

#      - Assigned to one specific person  

#      - Split among multiple people (hours divided equally)  

#      - Unassigned (to be auto-assigned later)  

#    - Validate that assigned people exist in the team  



# 4. Workload Limit:  

#    - Set configurable maximum hours per person per day (e.g., 8 hours)  

#    - Prevent assignments exceeding limit  

#    - Display warning when close to limit  



# 5. Conflict Detection:  

#    - Detect if a person is assigned to overlapping time slots  

#    - Check if deadline can be met given current workload  

#    - Flag impossible assignments before finalizing  



# 6. Progress Tracking:  

#    - Mark tasks as `pending`, `in-progress`, or `completed`  

#    - Update remaining hours dynamically  

#    - Show completion percentage per person and overall  





#  Input Validation & Error Handling (Mandatory):



# 7. Robust Input Validation:  

#    - Hours: Positive numbers (0.5–12)  

#    - Team size: Integer between 2–8  

#    - Names: Unique, non-empty strings  

#    - Days: Monday–Sunday only  

#    - Deadlines: Valid future day relative to project start  
# Project: Group Task Scheduler



# Assignment Overview:

# Build a comprehensive group task scheduling application that helps teams assign tasks, detect scheduling conflicts, track progress, and export weekly plans. This project demonstrates mastery of Python data structures, functions, error handling, file I/O, and datetime manipulation.



# Required Features

# Core Functionality (Mandatory):



# 1. Team Members:  

#    - Support 2–8 team members  

#    - Collect unique names and availability (days of week) for each  

#    - Store member info in a dictionary  



# 2. Task Entry:  

#    - Allow adding multiple tasks with names, estimated hours, and deadline (day)  

#    - Support continuous task entry until user selects `'done'`  

#    - Track each task's requirements  



# 3. Assignment Rules:  

#    - Each task can be assigned in three ways:  

#      - Assigned to one specific person  

#      - Split among multiple people (hours divided equally)  

#      - Unassigned (to be auto-assigned later)  

#    - Validate that assigned people exist in the team  



# 4. Workload Limit:  

#    - Set configurable maximum hours per person per day (e.g., 8 hours)  

#    - Prevent assignments exceeding limit  

#    - Display warning when close to limit  



# 5. Conflict Detection:  

#    - Detect if a person is assigned to overlapping time slots  

#    - Check if deadline can be met given current workload  

#    - Flag impossible assignments before finalizing  



# 6. Progress Tracking:  

#    - Mark tasks as `pending`, `in-progress`, or `completed`  

#    - Update remaining hours dynamically  

#    - Show completion percentage per person and overall  





#  Input Validation & Error Handling (Mandatory):



# 7. Robust Input Validation:  

#    - Hours: Positive numbers (0.5–12)  

#    - Team size: Integer between 2–8  

#    - Names: Unique, non-empty strings  

#    - Days: Monday–Sunday only  

#    - Deadlines: Valid future day relative to project start  

#    - Handle all non-numeric/non-format inputs gracefully  





#  Data Management (Mandatory):



# 8. Data Structures:  

#    Use dictionaries to store:  

#    - `members`: `{name: {'availability': [days], 'workload': {day: hours}}}`  

#    - `tasks`: `{task_id: {'name': str, 'hours': float, 'deadline': str, 'assigned_to': [names], 'status': str}}`



# 9. File Export:  

#    - Save weekly schedule to `team_schedule.txt`  

#    - Include timestamp in filename  

#    - Format should match console output  



# 10. Detailed Weekly Report:  

#     - Generate identical output for screen and file  

#     - Show:  

#       - Task list with assignments & deadlines  

#       - Daily workload per person  

#       - Conflict summary (if any)  

#       - Overall team progress percentage  







#  Sample Console Output:



# === Group Task Scheduler ===



#  Team Setup 

# Enter number of team members (2-8): 3

# Enter names:

# Member 1: Priya

# Available days (comma-separated, Mon-Sun): Mon,Tue,Wed,Thu,Fri

# Member 2: Raj

# Available days: Tue,Wed,Thu,Fri,Sat

# Member 3: Anita

# Available days: Mon,Wed,Fri



#  Workload Limit 

# Max hours per person per day (default 8): 8



#  Add Tasks 

# Task name: Design UI

# Est. hours: 6

# Deadline (day): Fri

# Assigned to (name or 'unassigned'): Priya

# ✓ Added: Design UI (6 hrs, Fri) → Priya



# Task name: Backend API

# Est. hours: 10

# Deadline: Wed

# Assigned to: unassigned

# ✓ Added: Backend API (10 hrs, Wed) → unassigned



# Task name: Testing

# Est. hours: 4

# Deadline: Sat

# Assigned to: Raj,Anita

# ✓ Added: Testing (4 hrs, Sat) → Raj, Anita



# Task name (or 'done'): done



#  Conflict Detection 

# Warning: Backend API (10 hrs) needs assignment before Wed

# ✓ No other conflicts detected



#  Progress 

# Task: Design UI → In-progress? (y/n): y

# Task: Backend API → Pending

# Task: Testing → Pending



#  Weekly Schedule Report 

# Date: 2025-03-20 10:30:00



# TASKS:

# 1. Design UI (6 hrs, Fri) - Priya [IN-PROGRESS]

# 2. Backend API (10 hrs, Wed) - UNASSIGNED [PENDING]

# 3. Testing (4 hrs, Sat) - Raj, Anita [PENDING]



# DAILY WORKLOAD:

# Priya: Mon(0), Tue(0), Wed(0), Thu(0), Fri(6), Sat(0), Sun(0)

# Raj:   Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)

# Anita: Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)



# CONFLICTS: Backend API needs assignment by Wed



# PROGRESS: 33% complete (1 of 3 tasks in-progress/completed)



# Exported to: team_schedule_20250320_103000.txt









# File Output Format :

# Group Task Scheduler Report

# Date: 2025-03-20 10:30:00

# Team: Priya, Raj, Anita

# Max daily hours: 8



# TASK BREAKDOWN:

# - Design UI (6 hrs, Fri) → Priya [IN-PROGRESS]

# - Backend API (10 hrs, Wed) → UNASSIGNED [PENDING]

# - Testing (4 hrs, Sat) → Raj, Anita [PENDING]



# DAILY WORKLOAD:

# Priya: Mon(0), Tue(0), Wed(0), Thu(0), Fri(6), Sat(0), Sun(0)

# Raj:   Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)

# Anita: Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)



# CONFLICT SUMMARY:

# - Backend API needs assignment before Wednesday



# PROGRESS:

# - Overall: 33%

# - Completed: 0 | In-progress: 1 | Pending: 2



# Constants:

# MAX_TEAM_SIZE = 8

# MIN_TEAM_SIZE = 2

# MAX_HOURS_PER_DAY = 8

# DAYS_OF_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# OUTPUT_FILE_PREFIX = "team_schedule"
#    - Handle all non-numeric/non-format inputs gracefully  





#  Data Management (Mandatory):



# 8. Data Structures:  

#    Use dictionaries to store:  

#    - `members`: `{name: {'availability': [days], 'workload': {day: hours}}}`  

#    - `tasks`: `{task_id: {'name': str, 'hours': float, 'deadline': str, 'assigned_to': [names], 'status': str}}`



# 9. File Export:  

#    - Save weekly schedule to `team_schedule.txt`  

#    - Include timestamp in filename  

#    - Format should match console output  



# 10. Detailed Weekly Report:  

#     - Generate identical output for screen and file  

#     - Show:  

#       - Task list with assignments & deadlines  

#       - Daily workload per person  

#       - Conflict summary (if any)  

#       - Overall team progress percentage  







#  Sample Console Output:



# === Group Task Scheduler ===



#  Team Setup 

# Enter number of team members (2-8): 3

# Enter names:

# Member 1: Priya

# Available days (comma-separated, Mon-Sun): Mon,Tue,Wed,Thu,Fri

# Member 2: Raj

# Available days: Tue,Wed,Thu,Fri,Sat

# Member 3: Anita

# Available days: Mon,Wed,Fri



#  Workload Limit 

# Max hours per person per day (default 8): 8



#  Add Tasks 

# Task name: Design UI

# Est. hours: 6

# Deadline (day): Fri

# Assigned to (name or 'unassigned'): Priya

# ✓ Added: Design UI (6 hrs, Fri) → Priya



# Task name: Backend API

# Est. hours: 10

# Deadline: Wed

# Assigned to: unassigned

# ✓ Added: Backend API (10 hrs, Wed) → unassigned



# Task name: Testing

# Est. hours: 4

# Deadline: Sat

# Assigned to: Raj,Anita

# ✓ Added: Testing (4 hrs, Sat) → Raj, Anita



# Task name (or 'done'): done



#  Conflict Detection 

# Warning: Backend API (10 hrs) needs assignment before Wed

# ✓ No other conflicts detected



#  Progress 

# Task: Design UI → In-progress? (y/n): y

# Task: Backend API → Pending

# Task: Testing → Pending



#  Weekly Schedule Report 

# Date: 2025-03-20 10:30:00



# TASKS:

# 1. Design UI (6 hrs, Fri) - Priya [IN-PROGRESS]

# 2. Backend API (10 hrs, Wed) - UNASSIGNED [PENDING]

# 3. Testing (4 hrs, Sat) - Raj, Anita [PENDING]



# DAILY WORKLOAD:

# Priya: Mon(0), Tue(0), Wed(0), Thu(0), Fri(6), Sat(0), Sun(0)

# Raj:   Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)

# Anita: Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)



# CONFLICTS: Backend API needs assignment by Wed



# PROGRESS: 33% complete (1 of 3 tasks in-progress/completed)



# Exported to: team_schedule_20250320_103000.txt









# File Output Format :

# Group Task Scheduler Report

# Date: 2025-03-20 10:30:00

# Team: Priya, Raj, Anita

# Max daily hours: 8



# TASK BREAKDOWN:

# - Design UI (6 hrs, Fri) → Priya [IN-PROGRESS]

# - Backend API (10 hrs, Wed) → UNASSIGNED [PENDING]

# - Testing (4 hrs, Sat) → Raj, Anita [PENDING]



# DAILY WORKLOAD:

# Priya: Mon(0), Tue(0), Wed(0), Thu(0), Fri(6), Sat(0), Sun(0)

# Raj:   Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)

# Anita: Mon(0), Tue(0), Wed(0), Thu(0), Fri(0), Sat(2), Sun(0)



# CONFLICT SUMMARY:

# - Backend API needs assignment before Wednesday



# PROGRESS:

# - Overall: 33%

# - Completed: 0 | In-progress: 1 | Pending: 2



# Constants:

# MAX_TEAM_SIZE = 8

# MIN_TEAM_SIZE = 2

# MAX_HOURS_PER_DAY = 8

# DAYS_OF_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# OUTPUT_FILE_PREFIX = "team_schedule"