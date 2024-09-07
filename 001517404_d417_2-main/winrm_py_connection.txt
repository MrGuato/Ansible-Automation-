import winrm

session = winrm.Session('http://10.10.1.35:5985/wsman', auth=
('Student', 'P@ssw0rd'))
result = session.run_cmd('hostname')
print(result.std_out.decode())
