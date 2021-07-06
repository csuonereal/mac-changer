import subprocess
import time
import optparse
import re  # for regex101

def get_user_input():
    po = optparse.OptionParser()
    po.add_option("-i", "--interface", dest="interface", help="interface to change!")
    po.add_option("-m", "--mac", dest="mac_address", help="new mac address")

    return po.parse_args()

#print(po.parse_args())
#print(type(po.parse_args()))


def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def control_change(interface_name):
        ifconfig = subprocess.check_output(["ifconfig", interface_name])
        new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
        if new_mac:
            return new_mac.group(0)
        else:
            return None


print("mac changer is being started...")
time.sleep(3)

(user_inputs, arguments) = get_user_input()  # it gives us a tuple type

print("mac address is being changed...")
time.sleep(3)

change_mac_address(user_inputs.interface, user_inputs.mac_address)
final_mac = control_change(user_inputs.interface)


time.sleep(3)


if final_mac == user_inputs.mac_address:
    print("new mac address applied successfully : {0}".format(final_mac))
else:
    print("error")





