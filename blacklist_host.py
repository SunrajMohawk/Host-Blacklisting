#Created by Sunraj Singh, Student Number 000841154
#The platform module is imported and used to retrieve system information about the User's operating system.
import platform

#This line uses the platform library to display the operating system that is being used.
system_os = platform.system() 
print("Your current operating system is {}.".format(system_os))

#This function is created to accept a "host" value in the form of a string.
def blacklist_host(host):

    #If the user's operating system is Windows, then the hosts file will be edited in this location.
    if system_os == 'Windows':
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

    #If the user's operating system is Linux, then the hosts file will be edited in this location.
    elif system_os == 'Linux':
        hosts_path = '/etc/hosts'

    #The script will not run using any other operating system and the following print statement will be displayed.
    else:
        print ("This program supports file paths for Windows and Linux machines only")
        return
    
    try:
        #The hosts file will be opened based on the operating system being used and the lines of the file will be read.
        hosts_file = open(hosts_path, 'r')
        lines = hosts_file.readlines()
        hosts_file.close()

        #The hosts file will be opened again and this time, data will be appended based on the following conditions.
        hosts_file = open(hosts_path, 'a')
        
        #If the host already exists in the file, the following code will be used:
        for line in lines:
            if host in line:
                print("The host '{}' already exists.".format(host))
                user_decision = input("Would you like to modify of delete the existing host entry?\n"
                                      "Enter [modify] [delete] or [no]: ")
                
                #The user may choose to modify the existing host entry.
                #The existing entry is supposed to be removed and the new entry takes its place.
                if user_decision == 'modify':
                    #This line should delete the existing entry, but I couldn't get it to work as intended.
                    lines.remove(line)
                    new_address = input("Enter a new IP address for host '{}': ".format(host))
                    #A new entry is created based on the IP Address and host value that the user provided previously.
                    line = "\n{} {}\n".format(new_address, host)
                    #It is then written to the hosts file and closed.
                    hosts_file.write(line)
                    hosts_file.close()
                    return

                #The user may choose to delete the existing host entry.
                elif user_decision == 'delete':
                    #This line should delete the existing entry, but I couldn't get it to work as intended.
                    lines.remove(line)
                    print("The previous record/records have been removed.")

                #The user may choose to make no changes at all. 
                elif user_decision == 'no':
                    hosts_file.close()
                    return
                
                #If the user does not provide one of the outlined responses, the script will end.
                else:
                    print("Invalid response.")
                    hosts_file.close()
                    return 
                
        #This will create a new entry into the hosts file to blacklist the user-specified host.
        #The hosts file is then closed.
        hosts_file.write("0.0.0.0 {}\n".format(host))
        print("The host '{}' has been blacklisted.".format(host))
        hosts_file.close()

    #This print statement will be displayed when the blacklist_host function comes to an end.
    finally:
        print("Script finished executing.")

#User will be prompted to enter a Domain Name to add to the blacklist.
#The string will be stored in the "host" variable then passed to the "blacklist_host" function.
if __name__ == "__main__":
    host = input("Enter the Name of the host you would like to blacklist: ")
    blacklist_host(host)