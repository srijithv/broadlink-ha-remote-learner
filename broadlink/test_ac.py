import broadlink
import os
import time

def find_rmpro():
    devices = broadlink.discover(timeout=5)
    for device in devices:
        if device.type == "RMPRO":
            device.auth()
            return device
    return None

def load_code(filename):
    try:
        with open(f"codes/{filename}.txt", "r") as f:
            return bytes.fromhex(f.read().strip())
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None

def send_code(device, code):
    if code:
        device.send_data(code)
        return True
    return False

if __name__ == "__main__":
    print("Looking for RM Pro...")
    device = find_rmpro()
    
    if not device:
        print("No RM Pro found!")
        exit()

    print("RM Pro found!")
    
    # Get list of all saved codes
    codes_dir = "codes"
    code_files = [f.replace('.txt', '') for f in os.listdir(codes_dir) if f.endswith('.txt')]
    code_files.sort()

    print("\nAvailable commands:")
    for i, code_name in enumerate(code_files, 1):
        print(f"{i}. {code_name}")

    while True:
        print("\nOptions:")
        print("1. Test specific temperature")
        print("2. Run temperature sequence")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == "1":
            temp = input("Enter temperature (17-28) or 'off': ")
            if temp == 'off':
                code_name = 'off'
            else:
                try:
                    temp = int(temp)
                    if 17 <= temp <= 28:
                        code_name = f'cool_{temp}'
                    else:
                        print("Invalid temperature!")
                        continue
                except:
                    print("Invalid input!")
                    continue
            
            code = load_code(code_name)
            if code:
                print(f"Sending command: {code_name}")
                send_code(device, code)
                print("Command sent!")
            
        elif choice == "2":
            print("\nWill test all temperatures from 17-28 with 5 second delay")
            input("Press Enter to start sequence...")
            
            for temp in range(17, 29):
                code_name = f'cool_{temp}'
                code = load_code(code_name)
                if code:
                    print(f"\nSending: {code_name}")
                    send_code(device, code)
                    time.sleep(5)  # Wait 5 seconds between commands
            
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")