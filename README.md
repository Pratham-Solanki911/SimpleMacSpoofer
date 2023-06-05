# Simple MAC Change in Python (Linux, with Root Privileges)

This Python script allows you to change the MAC address of a network interface on a Linux system, provided you have root privileges. It provides a simple and straightforward way to modify the MAC address of your network interface.

Please note that changing MAC addresses can have legal and ethical implications. Ensure that you have the necessary permissions and comply with the applicable laws and regulations before using this script.

## Prerequisites

To use this script, you need the following:

- Linux operating system
- Python 3.x installed on your system
- Root privileges to modify the network interface settings

## Installation

1. Clone this repository or download the script `mac_change.py` to your local machine.

```
git clone https://github.com/Pratham-Solanki911/SimpleMacSpoofer.git
```
2. Make sure you have the necessary permissions to execute the script.

```
chmod +x simplespoofer.py
```

PLEASE NOTE:	Modify the simplespoofer.py script by replacing the variables interface with your desired network interface and new_mac with the MAC address you want to change into.
## Usage

1. Open a terminal and navigate to the directory where you downloaded the `simplespoofer.py` script.

2. Run the script with root privileges.

```
sudo python simplespoofer.py
```

3. The script will prompt you to select the network interface for which you want to change the MAC address. Enter the appropriate number corresponding to the desired interface.

4. Next, enter the new MAC address you want to assign to the selected interface. The MAC address should be in the format `XX:XX:XX:XX:XX:XX`, where `X` represents a hexadecimal digit.

5. The script will attempt to change the MAC address of the specified network interface. If successful, it will display a success message. If any error occurs, it will provide an error message.

