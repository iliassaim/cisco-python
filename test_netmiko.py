from netmiko import ConnectHandler
from getpass import getpass


USER = input('Username : ')
PASS = getpass()
COMMAND = input("enter the command :")
with open ('devices.txt') as HOSTS:
    for HOST in HOSTS:

        Router = {
             'device_type': 'cisco_ios',
             'host': HOST,
             'username': USER,
             'password': PASS
}
        print("-" * 100)
        print('connecting to '+ HOST)
        MY_SSH = ConnectHandler(**Router)
        config_commands = [ 'line con 0',
                    ' log sync',
                    COMMAND

                          ] 
        MY_SSH.send_config_set(config_commands)
        
        output = MY_SSH.send_command(COMMAND)
        print(output )
        print("-" * 100)
MY_SSH.disconnect()

input(' Exit')