import subprocess
import re

def change_mac(interface, new_mac):
    # Disable the interface
    subprocess.call(['ifconfig', interface, 'down'])

    # Change the MAC address
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])

    # Enable the interface
    subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
    iwconfig_result = subprocess.check_output(['iwconfig', interface]).decode('utf-8')
    mac_address_search_result = re.search(r'(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)', iwconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return None

# Change these values as per your requirements
interface = 'wlo1'
new_mac = '01:02:03:04:05:06'

# Get the current MAC address
current_mac = get_current_mac(interface)
print('Current MAC address:', current_mac)

# Change the MAC address
change_mac(interface, new_mac)

# Check if the MAC address has been changed successfully
current_mac = get_current_mac(interface)
if current_mac == new_mac:
    print('MAC address has been successfully changed to', current_mac)
else:
    print('Failed to change MAC address.')

