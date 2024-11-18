import broadlink
import time

print("Discovering devices (10 second scan)...")
devices = broadlink.discover(timeout=10)
print(f"\nFound {len(devices)} devices:")
for device in devices:
    device.auth()
    print(f"\nDevice Type: {device.type}")
    print(f"IP: {device.host[0]}") 
    print(f"MAC: {device.mac}")
