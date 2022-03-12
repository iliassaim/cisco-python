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
        CMD_FILE = HOSTNAME  +'.txt'
        MYSSH.send_config_from_file(CMD_FILE)
        print(HOSTNAME + ' configured')
        
MYSSH.disconnect()

input("Exit")
