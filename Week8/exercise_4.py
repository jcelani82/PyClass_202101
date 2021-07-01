from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from exercise_2b import Gather_Routes


my_device = Device(**srx2)
my_device.open()


routes = Gather_Routes(my_device)

print()

for r in routes.items():
    pprint(r)

my_device_cfg = Config(my_device)

print()
try:
    my_device_cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")

my_device_cfg(path="jnpr_config_4.conf", format="text", merge="True")

routes

