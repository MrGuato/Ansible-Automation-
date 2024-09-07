from netmiko import ConnectHandler
from getpass import getpass

User_Network = {
	"device_type": "extreme_exos",
	"host": "10.10.1.22",
	"username": "admin",
	"password": ''
}

ACCT_Network = {
        "device_type": "extreme_exos", 
        "host": "10.10.1.32",
        "username": "admin",
        "password": ''
}

MGMT_Network = {
        "device_type": "extreme_exos", 
        "host": "10.10.1.31",
        "username": "admin",
        "password": ''
}

IT_Network = {
        "device_type": "extreme_exos", 
        "host": "10.10.1.30",
        "username": "admin",
        "password": ''
}

createacct_vlan = "create vlan ACCT_Network tag 20"

createuser_vlan = "create vlan User_Network tag 30"

createmgmt_vlan = "create vlan MGMT_Network tag 10"

createit_vlan = "create vlan IT_Network tag 40"

with ConnectHandler(**User_Network) as net_connect:
	output = net_connect.send_command(createuser_vlan)
	output += net_connect.save_config()

print(output)

with ConnectHandler(**ACCT_Network) as net_connect:
	output = net_connect.send_command(createacct_vlan)
	output += net_connect.save_config()

print(output)

with ConnectHandler(**MGMT_Network) as net_connect:
        output = net_connect.send_command(createmgmt_vlan)
        output += net_connect.save_config()

print(output)

with ConnectHandler(**IT_Network) as net_connect:
        output = net_connect.send_command(createit_vlan)
        output += net_connect.save_config()

print(output)

