
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2


my_device = Device(**srx2)
my_device.open()

my_device_cfg = Config(my_device)

print()
try:
    my_device_cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")
