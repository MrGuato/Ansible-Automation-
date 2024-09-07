<h1>Network Automation Project Using Python and Ansible</h1>
Overview of the Network Automation Project
Initial Setup
I began by setting up my environment, ensuring that essential tools like Python, Netmiko, and Ansible were installed and ready to use. This foundational step was crucial for the subsequent automation tasks.

Inventory Management with Python
I created a Python script to list switch inventory details, saving them into an .ini file. This script was essential for maintaining an organized record of my network devices. I overcame initial challenges with the configparser module by switching to python3, ensuring smooth script execution.

VLAN Management
Fetching VLANs: Using Netmiko and getpass, I wrote a script to retrieve existing VLANs. After resolving import issues and switching to python3, I successfully fetched the VLAN details.
Adding VLANs: I developed a script to add VLANs to network switches, using SSH RSA keys for secure authentication. This step involved generating key pairs and linking them to switch admin accounts.
Verifying VLANs: To confirm successful VLAN deployment, I logged into the switches and used the Show VLAN command, ensuring the VLANs were correctly assigned.

Finalizing VLAN Deployment
I verified installed applications and executed scripts to manage VLANs, using SSH RSA keys for authentication. This comprehensive approach ensured accurate VLAN deployment across my network.

Inventory Script
I wrote a script using configparser to generate an inventory details file in .ini format for both Windows desktops and Linux test boxes. This script facilitated organized inventory management.

Deploying User Accounts with Ansible
Initially, I faced challenges deploying user accounts on Windows desktops using Ansible. After extensive troubleshooting, including upgrading Ansible and Python, testing WinRM, and ensuring SSH functionality, I successfully deployed the automation script via WinRM across Windows, Linux, and Exos devices. The key was adapting Linux-specific commands for the Windows environment.

Overcoming Connection Issues
I encountered significant challenges connecting to the Windows network. After extensive testing and consultation, I identified incorrect parameters for the Windows environment. Simplifying the process by categorizing device groups (Windows/Linux/Exos) made the task more manageable, leading to successful project completion.

Conclusion
My project demonstrates a comprehensive approach to network automation, leveraging Python and Ansible to manage inventory, deploy VLANs, and automate user account provisioning. By overcoming various challenges and adapting my methods, I achieved a robust and efficient network automation solution.
