from bluetooth import *
from PyOBEX.client import Client
import sys

addr = "94:8B:C1:85:B5:9F"
uuid = "00001105-0000-1000-8000-00805f9b34fb"
print("Searching for OBEX service on %s" % addr)

service_matches = find_service( uuid = uuid, address = addr )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put("test.txt", "Hello world\n")
client.disconnect()
