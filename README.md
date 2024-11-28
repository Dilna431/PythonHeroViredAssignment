
# PythonHeroViredAssignment

## Description

This repository contains three Python scripts:

1.Backup.py : Automates file backups with timestamp-based uniqueness for filenames

2.passwordcheck.py: Validates the strength of a password based on predefined criteria.

3.monitor_cpy.py: Monitors real-time CPU usage and provides alerts if usage exceeds a predefined threshold


## Scripts

1. Backup.py

Description : The backup.py script automates the process of backing up files from a source directory to a destination directory. It ensures that files are copied safely and avoids overwriting by appending timestamps to duplicate filenames in the destination directory.

Features :

- Copies all files from the source directory to the destination   directory.
- Ensures unique filenames by appending timestamps if a file with the same name already exists in the destination.
- Automatically creates the destination directory if it does not exist.
- Handles errors gracefully, such as missing directories or permission issues.

Installation : 

1. Clone the repository: git clone

 https://github.com/Dilna431/PythonHeroViredAssignment.git

2. Navigate to the directory:
   
cd PythonHeroViredAssignment

3. Run the script:

python Backup.py

## Usage/Examples

Run the script from the command line by providing the source and destination directories as arguments.

python backup.py /path/to/source /path/to/destination

Input:

The source directory contains:
file1.txt
file2.txt

Output:

The destination directory (./backup) will contain:

file1.txt
file2.txt

If a file with the same name already exists in the destination directory, a timestamp will be appended:

file1_20241128_153045.txt

Requirements
Python 3.x
Built-in libraries used: os, shutil, datetime.

2. passwordcheck.py

Description : This Python script checks the strength of a password based on length, character variety, and inclusion of special characters.

Features : Validates password strength based on:
- Minimum length.
- Uppercase and lowercase letters.
- Numbers.
- Special characters.
- Provides feedback for improving weak passwords.

Installation : 

1. Clone the repository: git clone

 https://github.com/Dilna431/PythonHeroViredAssignment.git

2. Navigate to the directory:
   
cd PythonHeroViredAssignment

3. Run the script:

python passwordcheck.py

Usage/Examples

Run the script and follow the on-screen prompts to input a password for validation

python passwordcheck.py

Input:

Enter your password: Hello123!

Output:

Strong password! ✅

Input (Weak Password):

Enter your password: weakpass

Your password is weak !! Ensure it meets the following criteria:
- At least 8 characters long
- Contains both uppercase and lowercase letters
- Contains at least one digit (0-9)
- Contains at least one special character (e.g., !, @, #, $)

Requirements

Python 3.x

Uses the built-in re module for regular expressions.

3. monitor_cpy.py

Description : The monitor_cpu.py script monitors the CPU usage of your system in real-time. It displays the current CPU usage as a percentage and can be customized to alert or log when the usage exceeds a predefined threshold. This is useful for DevOps tasks like monitoring server performance or identifying resource bottlenecks.

Features : 
- Real-time monitoring of CPU usage.
- Displays CPU usage as a percentage in the terminal.
- Logs excessive CPU usage for debugging and analysis 
- Special characters.
- Provides feedback for improving weak passwords.

Installation : 

1. Clone the repository: git clone

 https://github.com/Dilna431/PythonHeroViredAssignment.git

2. Navigate to the directory:
   
cd PythonHeroViredAssignment

3. Run the script:

python passwordcheck.py

4. Install Required Modules: The script uses psutil. Install it via pip

pip install psutil


Usage/Examples

Run the script from the command line. It will display real-time CPU usage information.

python monitor_cpu.py

Example Output:

CPU Usage: 15.2%
CPU Usage: 22.7%
CPU Usage: 78.5%
Warning: CPU usage exceeded threshold! Current usage: 78.5%

Requirements

Python 3.x
Modules:
psutil: For fetching CPU usage information.
time (built-in): For controlling the update frequency.

## Usage/Examples

Run the script from the command line by providing the source and destination directories as arguments.

python backup.py /path/to/source /path/to/destination

Input:

The source directory contains:
file1.txt
file2.txt

Output:

The destination directory (./backup) will contain:

file1.txt
file2.txt

If a file with the same name already exists in the destination directory, a timestamp will be appended:

file1_20241128_153045.txt


## Requirements

Python 3.x
Built-in libraries used: os, shutil, datetime.
