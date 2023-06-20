
import os
def port_scanner():
    import socket, time, threading, concurrent.futures
import os                 
import socket             
import threading          
import concurrent.futures 


grey_bold = '\033[1;90m'
grey = '\033[0;90m'
yello_ish = '\033[1;93m'
yello_ish_not_bold = '\033[0;93m'
white = '\033[0;37m'
white_bold = '\033[1;37m'

green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'

def port_scanner():
    print_lock = threading.Lock() 
    
    ips = input(f"\n {grey_bold}[{green}+{grey_bold}]" + f"{yello_ish} Enter IPs " + f"{grey_bold}(split by {yello_ish_not_bold},{grey_bold}) {grey}>" + f"{white} ") # We are asking user to input ips
    
    ports = int(input(f" {grey_bold}[{green}+{grey_bold}]" + f"{yello_ish} Scan To Port " + f"{grey_bold}({yello_ish_not_bold}0{grey_bold} for all ports) {grey}>" + f"{white} ")) # We are asking user to input number of port when scan will end

    work = 100 
    
    if ports == 0: ports = 65535 
    if ports >= 32767: work = 200

    def scan(ip, port): 
        
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        scanner.settimeout(1) 
        
        try: 
            
            scanner.connect((ip, port)) 

            scanner.close() 
            
            with print_lock: 
                if mode != 1:
                    print('\033[1;32m' + "\r Opened" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}    ")
                else:
                    print('\033[1;32m' + "\r   Opened" + '\033[0;90m' + " > " + '\033[0;37m' + f"{port}    ")

        except: 
            pass

    if ',' in ips: 
        
        for ip in ips.split(','): 
            
            mode = 1 
            
            ip = ip.strip() 
            
            print(f"\n\n  {grey_bold}[{blue}+{grey_bold}]" + f"{yello_ish_not_bold} Scanning {white_bold}{ip}{grey}:") 
            try: 
                with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor: 
                    
                    for port in range(ports):
                        
                        executor.submit(scan, ip, port) 
                        
            except KeyboardInterrupt: 
                print('\033[1;31m' + ' Stopping')
                pass
    else:
        
        ips.strip() 
        
        print("\n") 
        
        try:
            
            mode = 0 
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:  
                
                for port in range(ports):  
                    
                    executor.submit(scan, ips, port) 
                    
        except KeyboardInterrupt: 
            print('\033[1;31m' + ' Stopping')
            pass


if os.name == 'nt': os.system("cls") 

c=0 

while 1: 
    
    if c == 0: 

        port_scanner(); c+=1

    else:
        
        cho = input(f"\n\n {grey_bold}[{red}?{grey_bold}]" + f"{yello_ish_not_bold} Do you want to continue? {grey}(y/n){white} ").lower()
        
        if cho == "y": 
            print("\n")
            port_scanner() 
        
        else: quit()
