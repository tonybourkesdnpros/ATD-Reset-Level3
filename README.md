# ATD-Lab-Reset (Level 3)

This is a collection of Ansible playbooks/configs, configlets (in the form of .cfg text files), and YAML files to configure the Arista ATD lab envioronment 
for the Arista ACE Level 3 ertification course lab topology (as of Feb 2022). 

This will **only** work on the ATD Level 3 labs but you can modidfy the YAML files and playbooks to suit other environments. 

The playbooks/configs/YAML files will set the Level 3 lab environment into one of three configurations (more comming later): 

* Default (the way the lab originally comes)
* EVPN VXLAN underlay and overlay

The playbooks will set the configlets, upload any that need to be uploaded, and attach them to devices. 

This does **not** create the change control or execute the change control. At this time, that must be done manually by an administrator. 

## Getting Started

The installed version of Arista.cvp (3.3.1) needs to be downgraded to 3.3.0, so run the following command to do so: 

    > ansible-galaxy collection install arista.cvp:==3.2.0

Now that the environment is ready, clone the ATD-Lab-Reset repo to the ATD VS-Code environment (Terminal). 

    > git clone https://github.com/tonybourkesdnpros/ATD-Reset-Level3.git
    
This will create a new directory called ATD-Reset-Level3.

Edit the inventory.yml file to reflect the password for your particular enviroment: 

<code>           ansible_password: aristaXXXX</code>

### CVP-default.yml

This playbook resets the lab to the default container topology and all devices to the default configlets. It **does not** delete any configlets that have been uploaded or added in other ways. 

To run this playbook, use the following command: 

     > ansible-playbook playbooks/CVP-lab-reset.yml


    
