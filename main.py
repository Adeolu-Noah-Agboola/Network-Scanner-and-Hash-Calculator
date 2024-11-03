import port_scan
import os
from filehash import FileHash

if __name__=='__main__':
   port_scan.program_menu()
    # target_ip=port_scan.port_menu()
    # port_scan.port_scan(target_ip)
   


   #in this program we will be computing the hash for any specified filespecified

   #specifying the path name for the file we cant to calculate the hash on

   path='/Users/1up/Downloads/VSCode-darwin-universal.zip'

   md5hasher=FileHash('md5')
   #Prints out the hash of the file
   print(md5hasher.hash_file("/Users/1up/Downloads/VSCode-darwin-universal.zip"))
