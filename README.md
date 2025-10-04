# Automation_project1
Description: Developed a Python-based automation script to detect and delete and delete duplicate files from a directory periodically. The system automatically generates log files of operations performed and shares them via email for audit purposes.
•	Implemented checksum-based duplicate detection using hashlib (MDS).
•	Automated log generation with timestamps for periodic for every execution.
•	Used schedule library for periodic execution of duplicate file cleanup.
•	Integrated email automation (smtplib) to send logs automatically.
Tech Stack: Python, OS module, Hashlib, Schedule, smtplib 


# Automation_project2
Description: Designed a python automation project to periodically log details of running processes (PID, name, user, memory usage) on the system. Each execution generates a new log file with a time stamped filename for easy tracking.
•	Implemented process scanning using psutil to extract process details.
•	Automated log file created with timestamps and proper formatting.
•	Used the schedule library to run logging tasks periodically without manual intervention.
•	Enhanced usability by allowing custom folder name & interval input.
