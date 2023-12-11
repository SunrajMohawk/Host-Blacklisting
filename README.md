# Host-Blacklisting
This script is designed to blacklist a user-specified host and supports file paths for Windows and Linux based machines only.
The operating system check (platform.system) only works on Windows as Linux uses different syntax. 
Therefore, I left it in my code but it would require some modifications to get it to work as intended using Linux machines.

The platform module is used to retrieve system information about the User's operating system.
Based on the operating system, the correct path and corresponding hosts file will be accessed to write changes to.
This script will use the computer's hosts file to direct a host, specified by the user, to IP address 0.0.0.0.
If an entry already exists in the hosts file, the user is asked if they would like to modify or delete the existing host entry.

Ensure that you are running this program as administrator.
The premise of this script is to add host addresses to the computer's host files. 
Therefore, you will need the authority to make changes to this file. Otherwise, access will be denied and the script won't run.

It may also be a good idea to open your hosts file and monitor it as you add entries and make changes.
This is good practice to ensure you are receving the desired results.

Created by: Sunraj Singh
