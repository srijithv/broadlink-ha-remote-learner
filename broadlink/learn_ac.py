import broadlink
import time
import json
from datetime import datetime

def find_rmpro():
    devices = broadlink.discover(timeout=5)
    for device in devices:
        if device.type == "RMPRO":
            device.auth()
            return device
    return None

def learn_code(device, wait_time=10):
    print("Please point your AC remote at the RM Pro device")
    print(f"You have {wait_time} seconds to prepare...")
    time.sleep(3)
    print("Learning...")
    device.enter_learning()
    start_time = time.time()
    while time.time() - start_time < wait_time:
        time.sleep(1)
        try:
            data = device.check_data()
            if data:
                return data.hex()
        except:
            continue
    return None

def save_code(code, filename):
    if code:
        with open(f"codes/{filename}.txt", "w") as f:
            f.write(code)
        print(f"Code saved to codes/{filename}.txt")
        return True
    else:
        print("No code received!")
        return False

# Main execution
if __name__ == "__main__":
    # Create codes directory
    import os
    if not os.path.exists("codes"):
        os.makedirs("codes")

    # Find RM Pro device
    print("Looking for RM Pro...")
    device = find_rmpro()
    
    if not device:
        print("No RM Pro found!")
        exit()

    print("RM Pro found! Starting learning process...")
    
    # List of commands to learn
    commands = [
        ("off", "Power Off"),
        ("cool_17", "Cool Mode 17°C"),
        ("cool_18", "Cool Mode 18°C"),
        ("cool_19", "Cool Mode 19°C"),
        ("cool_20", "Cool Mode 20°C"),
        ("cool_21", "Cool Mode 21°C"),
        ("cool_22", "Cool Mode 22°C"),
        ("cool_23", "Cool Mode 23°C"),
        ("cool_24", "Cool Mode 24°C"),
        ("cool_25", "Cool Mode 25°C"),
        ("cool_26", "Cool Mode 26°C"),
        ("cool_27", "Cool Mode 27°C"),
        ("cool_28", "Cool Mode 28°C")
    ]

    # Keep track of failed commands for retry
    failed_commands = []
    
    print("\nStarting to learn commands...")
    print("For each temperature:")
    print("1. Point your remote at the RM Pro")
    print("2. Set the temperature on your remote")
    print("3. Press the power/send button")
    print("4. Wait for confirmation before moving to next temperature")
    
    input("\nPress Enter when ready to start...")

    for filename, description in commands:
        print(f"\n{'='*50}")
        print(f"Learning: {description}")
        input("Press Enter when ready to learn this command...")
        code = learn_code(device)
        if not save_code(code, filename):
            failed_commands.append((filename, description))
        time.sleep(2)  # Wait between commands

    # Handle retry for failed commands
    if failed_commands:
        print("\n\nSome commands failed to learn. Would you like to retry them?")
        retry = input("Retry failed commands? (y/n): ").lower().strip() == 'y'
        
        if retry:
            print("\nRetrying failed commands...")
            retry_failed = []
            for filename, description in failed_commands:
                print(f"\n{'='*50}")
                print(f"Retrying: {description}")
                input("Press Enter when ready to learn this command...")
                code = learn_code(device)
                if not save_code(code, filename):
                    retry_failed.append((filename, description))
            
            if retry_failed:
                print("\nThe following commands still failed to learn:")
                for filename, description in retry_failed:
                    print(f"- {description}")
    
    print("\nLearning process completed!")
    print(f"Codes are saved in the 'codes' directory")