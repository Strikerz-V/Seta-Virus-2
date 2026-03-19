"""
CRITICAL WARNING:
This script is for FILE SIMULATION purposes only.
It may cause STORAGE FULL errors and system LAG.
The author is NOT responsible for any damage
caused to your device or data loss.

AGREEMENT:
1. Do not distribute this script as actual malware.
2. Run only in a safe, isolated environment.
3. Take full responsibility for any consequences.
4. Use this knowledge for ETHICAL purposes only.
"""

import shutil
import sys
import os

def display_contract():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("                CRITICAL WARNING")
    print("="*50)
    print("This script is for FILE SIMULATION purposes only.")
    print("It may cause STORAGE FULL errors and system LAG.")
    print("The author is NOT responsible for any damage")
    print("caused to your device or data loss.")
    print("-" * 50)
    print("                   AGREEMENT")
    print("-" * 50)
    print("1. Do not distribute this script as actual malware.")
    print("2. Run only in a safe, isolated environment.")
    print("3. Take full responsibility for any consequences.")
    print("4. Use this knowledge for ETHICAL purposes only.")
    print("="*50)
    
    consent = input("\nType 'AGREE' to initiate the wave: ")
    return consent.upper() == "AGREE"

def start_wave(copy_count):
    original_file = sys.argv[0]
    target_dir = "Clone"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    print("\n[!] Initializing Wave...")
    
    for i in range(copy_count):
        new_name = os.path.join(target_dir, f"clone_{i}.py")
        try:
            shutil.copy(original_file, new_name)
            print(f"Cloning progress: {i+1}/{copy_count}", end='\r')
        except Exception as e:
            print(f"\n[!] Wave Interrupted: {e}")
            break
            
    print(f"\n\n[✓] Wave Complete. {copy_count} files generated.")
    print(f"Location: {os.path.abspath(target_dir)}")

if __name__ == "__main__":
    if display_contract():
        start_wave(1000000000)
    else:
        print("\n[!] Operation Aborted. Agreement not accepted.")
