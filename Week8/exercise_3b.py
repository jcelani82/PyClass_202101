
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


my_device_cfg.load("set system host-name python4life", format="set", merge=True)
print()
print(my_device_cfg.diff())
print()

my_device_cfg.rollback(0)
print()
print(my_device_cfg.diff())
print()



