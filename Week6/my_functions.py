import yaml

def read_yaml (filename) :
    with open(filename, "r") as f:
        devices = yaml.load(f)
        return devices

def arp_results(host, results):
    
    print()
    print()
    print(f"Arp Table for {host}: ")
    for arp_entry in results[0]["result"]["ipV4Neighbors"]:
        print(f"{arp_entry['hwAddress']} : {arp_entry['address']}")

def iproute_results(host, results):

    route_destination_data = results[0]['result']['vrfs']['default']['routes']
    print()
    print(host)
    for route_destination, route_info in route_destination_data.items():
        if route_info['routeType'] == "static":
            nexthop = route_info['vias'][0]['nexthopAddr']
            print(f"{route_destination} : Route is Statically connected, the next hop address is {nexthop}")
        if route_info['routeType'] == "connected":
            print(f"{route_destination} : Route is Directly connected")
    print()
