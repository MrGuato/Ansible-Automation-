import configparser

config = configparser.ConfigParser()

config['WindowsDesktop-1'] = {
'Ram' : '4096 MB' ,
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:4b:3c:0a:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' , 
'Replicate network connection states in Qemu' : 'Yes'
}

config['WindowsDesktop-2'] = {
'Ram' : '4096 MB' , 
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:59:fd:86:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' , 
'Replicate network connection states in Qemu' : 'Yes'
}

config['WindowsDesktop-3'] = {
'Ram' : '4096 MB' , 
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:e2:07:f3:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' , 
'Replicate network connection states in Qemu' : 'Yes'
}

config['WindowsDesktop-4'] = {
'Ram' : '4096 MB' ,
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:46:74:35:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' ,
'Replicate network connection states in Qemu' : 'Yes'
}

config['Test_Box_1'] ={
'Ram' : '4096 MB' ,
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:db:a8:90:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' ,
'Replicate network connection states in Qemu' : 'Yes'
}

config['Test_Box_2'] ={
'Ram' : '4096 MB' , 
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Send the shutdown signal (ACPI)' ,
'Console type' : 'vnc' ,
'Adapters' : '1' ,
'Base MAC' : '0c:50:a2:8a:00:00' ,
'Type' : 'Intel Gigabyte Ethernet (e1000)' ,
'Replicate network connection states in Qemu' : 'Yes'
}

with open('hostinventory.ini', 'w') as configfile:
	config.write(configfile)


