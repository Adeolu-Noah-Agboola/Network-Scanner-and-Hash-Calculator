import sys
import socket
import time
import os
import os.path
from filehash import FileHash



#Menu that allows the user to choose between the hash application or the port scan application
def program_menu():
   choice = 0
   while choice !=1 or choice!=2:
    choice=int(input("Which feature of the program would you like to execute? [Enter (1) for a Port Scan]  [Enter (2) for a File Hash Check]: "))
    if choice == 1:
            #choice 1 is ip and port scan
            target_ip=port_menu()
            port_scan(target_ip)
            break
            
    if choice == 2:
        #choice 2 is the  file hash check
        f_path=file_check()
        exp_hash=calculate_hash(f_path)
        compare_hash(exp_hash)
        break
    else:
        print("Please choose a valid option from the menu!!")
      


#captures how much time has passed
def run_time():
    timer=time.time()
    return timer


def port_scan(target_ip):
    start_time=run_time()
    try:
    #scanning every single port
        for port in range(1,65535):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #set default timeout for the socket in seconds
            socket.setdefaulttimeout(1)

            #setting up the connection for the socket
            result=s.connect_ex((target_ip,port))
            if result==0:
                #this means that the ports are open
                print("[*] Port {} is open".format(port))
                s.close()

#exiting the program
    except KeyboardInterrupt:
        print('\n exiting program')
        sys.close()

    except socket.error:
        print("could not reach host IP")
        sys.close()
    end_time=run_time()

    elapsed_time= (end_time-start_time)

    scan_complete=f'Scan Completed in {elapsed_time:.2f} seconds'

    print(scan_complete)


#menu to enter the target IP
def port_menu():
    print("_"*50)
    print("Welcome to Port Scan!!!")
    target_ip= str(input("Enter target IP address: "))
    print("Scanning the Target IP -> "+target_ip)
    print("_"*50)
    print('\n')
    return target_ip


def file_check():
     #path='/Users/1up/Downloads/VSCode-darwin-universal.zip'
    #this function checks if the file exists and calculates the hash 
    check=False
    while check == False:
        file_path=input("Enter full file path for the hash you would like to calculate: ")
        print('\n')
        check=os.path.isfile(file_path)
        if check== False:
            print("Sorry cannot find the specified file! Please Try again")
            print('\n')
            pass
        else:
            return file_path


    #check if the path and file exists

    #if the hash exists then save it and then we can use it for the next function

def calculate_hash(file_path):
       #creating md5 hash
       md5hasher=FileHash('md5')
       #Prints out the hash of the file
       calc_hash=md5hasher.hash_file(file_path)
       print("Calculating......\n")
       time.sleep(1)
       print ("The hash for "+ file_path+ " is: "+calc_hash)
       print('\n')
       return(calc_hash)

def compare_hash(exp_hash):
    #path= '/Users/1up/Documents/test folder/VSCode-darwin-universal.zip'
    #incorrect_path='/Users/1up/Downloads/Pierian-Data Complete-Python-3-Bootcamp master 16-Emailing-with-Python (1).zip'
    downloaded_file=input("Enter the file that you would like to verify the hash for: ")
    print('\n')
    result=calculate_hash(downloaded_file)
    if result == exp_hash:
        print("[+] Hash Verification Successful This file is original: "+' Expected Hash = '+ exp_hash+ ' Resulting Hash = '+result)
    else:
        print("[+] Hash Verification Unsuccessful This file is not original: "+' Expected Hash = '+ exp_hash+ ' Resulting Hash = '+result)




if __name__=='__main__':
    # target_ip=menu()
    # port_scan(target_ip)

    #This section checks and verifies the has of any specified file
    program_menu()




    # file_path=file_check()
    # exp_hash=calculate_hash(file_path)
    # compare_hash(exp_hash)