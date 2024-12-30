
import os
import time

def main():
    print("Running the script...")    # Print message
    time.sleep(3)                 # Wait for 3 seconds
    os.system('python main.py')   # Run the Python script
    input("Press Enter to continue...")  # Wait for user input to pause

if __name__ == "__main__":
    main()
