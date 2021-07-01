
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2


a_device = Device(**srx2)
a_device.open()


print()
print(f"The Hostname is: {a_device.hostname}")

