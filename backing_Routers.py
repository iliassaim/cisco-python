from netmiko import ConnectHandler
from getpass import getpass

USER = input('Username : ')
PASS = getpass()
with open ('devices.txt') as HOSTS:
    for HOST in HOSTS:

        Routers = {
             'device_type': 'cisco_ios',
             'host': HOST,
             'username': USER,
             'password': PASS
}

        MYSSH = ConnectHandler(**Routers)
        h_name = MYSSH.send_command('sho run | in hostname')
        X = h_name.split()
        HOSTNAME = X[1]
        print('Backing ' + HOSTNAME)
        FILE_Name = HOSTNAME + '-Backup.txt'
        B_FIle = open(FILE_Name , "w")
        B_FIle.write(MYSSH.send_command("Sho run"))
        B_FIle.write ("/n")
MYSSH.disconnect()

input("Exit")
