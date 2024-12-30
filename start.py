
import os
import time

def main():
    os.system('chcp 65001 > nul')  # Set the code page to UTF-8 (Windows-specific)
    print("Running the script...")    # Print message
    time.sleep(3)                 # Wait for 3 seconds
    os.system('python main.py')   # Run the Python script
    input("Press Enter to continue...")  # Wait for user input to pause

if __name__ == "__main__":
    main()
