"""
REFACTORED REPORT: THE CLEAN CODE BOT
Analysis based on SOLID principles and Clean Code standards.
"""

# --- STEP 1: ANALYZE (Chain of Thought) ---
# 1. Global Variables: Found 'l' and 'd'. These break encapsulation.
# 2. Cryptic Naming: 'fn', 'l', 'd', 'a', 'b' are non-descriptive.
# 3. SRP Violation: 'fn' handles adding, showing, and saving data.
# 4. Error Handling: No try-except blocks for file operations.
# 5. Security: Credentials stored in a plain dictionary.

# --- STEP 2: PLAN ---
# 1. Create a 'UserSession' class for authentication.
# 2. Create a 'DataManager' class for list operations and persistence.
# 3. Implement a main loop with clear control flow.
# 4. Use descriptive names and type hinting.

# --- STEP 3: REFACTOR ---

import datetime
import sys

class UserSession:
    """Handles authentication logic."""
    def __init__(self):
        # In a real app, these would be hashed or stored in environment variables
        self._credentials = {"admin": "12345"}

    def is_authenticated(self, username, password):
        return self._credentials.get(username) == password

class DataManager:
    """Manages data storage and file operations following SRP."""
    def __init__(self):
        self.data_store = []

    def add_entry(self, value):
        """Validates and adds a new entry with a timestamp."""
        if not value:
            print("Error: Value cannot be empty.")
            return
            
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'id': len(self.data_store) + 1,
            'val': value,
            'date': timestamp
        }
        self.data_store.append(entry)
        print(f"Successfully added entry #{len(self.data_store)}.")

    def display_all(self):
        """Formats and prints the data store."""
        if not self.data_store:
            print("The list is currently empty.")
            return
            
        print("\n--- Current Entries ---")
        for item in self.data_store:
            print(f"ID: {item['id']} | Value: {item['val']} | Created: {item['date']}")

    def save_to_disk(self, filename="data.txt"):
        """Saves data using a context manager with error handling."""
        try:
            with open(filename, "w") as f:
                f.write(str(self.data_store))
            print(f"Data successfully persisted to {filename}.")
        except IOError as e:
            print(f"Critical Error: Could not save data. {e}")

def run_application():
    """Main execution flow."""
    session = UserSession()
    manager = DataManager()

    print("--- Secure Data System ---")
    user = input("User: ")
    password = input("Pass: ")

    if not session.is_authenticated(user, password):
        print("Access Denied: Invalid credentials.")
        return

    print(f"Welcome, {user}!")
    
    actions = {
        "add": lambda: manager.add_entry(input("Enter Value: ")),
        "show": manager.display_all,
        "save": manager.save_to_disk,
    }

    while True:
        cmd = input("\nOptions (add/show/save/exit): ").lower()
        
        if cmd == "exit":
            print("Exiting system...")
            break
        
        if cmd in actions:
            actions[cmd]()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    run_application()