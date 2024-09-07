import configparser

config = configparser.ConfigParser()

config['Local_Switch'] = {
'Ram' : '4096 MB' ,
'vCPUs' : '2' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'HDD' ,
'On Close' : 'Power off the VM' ,
'Console Type' :  'vnc' ,
'Adapters' : '1' ,
'Base Mac' : '0c:57:7e:50:00:00' ,
'Type' : 'Intel Gigabit Ethernet (e1000)' ,
'Replicate Network Connection States in Qemu' : 'yes'
}

config['User_Network'] = {
'Ram' : '512 MB' ,
'vCPUs' : '1' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'CD/DVD-ROM or HDD' ,
'On Close' : 'Power off the VM' ,
'Console Type' :  'telnet' ,
'Adapters' : '13' ,
'Base Mac' : '0c:e0:f2:0b:00:00' ,
'Type' : 'Realtek 8139 Ethernet (rtl8139)' ,
'Replicate Network Connection States in Qemu' : 'yes'
}

config['ACCT_Network'] = {
'Ram' : '512 MB' ,
'vCPUs' : '1' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'CD/DVD-ROM or HDD' ,
'On Close' : 'Power off the VM' ,
'Console Type' :  'telnet' , 
'Adapters' : '13' ,
'Base Mac' : '0c:40:34:07:00:00' ,
'Type' : 'Realtek 8139 Ethernet (rtl8139)' ,
'Replicate Network Connection States in Qemu' : 'yes'
}

config['MGMT_Network'] = {
'Ram' : '512 MB' ,
'vCPUs' : '1' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'CD/DVD-ROM or HDD' ,
'On Close' : 'Power off the VM' ,
'Console Type' :  'telnet' , 
'Adapters' : '13' ,
'Base Mac' : '0c:cc:78:5d:00:00' ,
'Type' : 'Realtek 8139 Ethernet (rtl8139)' ,
'Replicate Network Connection States in Qemu' : 'yes'
}

config['IT_Network'] = {
'Ram' : '512 MB' ,
'vCPUs' : '1' ,
'Qemu Binary' : '/bin/qemu-system-x86_64 (v4.2.1)' ,
'Boot Priority' : 'CD/DVD-ROM or HDD' ,
'On Close' : 'Power off the VM' ,
'Console Type' :  'telnet' ,
'Adapters' : '13' ,
'Base Mac' : '0c:1c:b2:85:00:00' ,
'Type' : 'Realtek 8139 Ethernet (rtl8139)' ,
'Replicate Network Connection States in Qemu' : 'yes'
}

with open('switchinventory.ini', 'w') as configfile:
	config.write(configfile)


