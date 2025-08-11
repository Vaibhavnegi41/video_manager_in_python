import sqlite3
import os
from colorama import Fore, Style, init


init(autoreset=True)


connection = sqlite3.connect("database_contact.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               phone TEXT NOT NULL
            )
''')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")

def list_contacts():
    clear_screen()
    print(Fore.CYAN + "=" * 40)
    print(Fore.CYAN + "📇 CONTACT LIST")
    print(Fore.CYAN + "=" * 40)

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print(Fore.WHITE + f"{row[0]}. {row[1]} - {row[2]}")
    else:
        print(Fore.RED + "No contacts found.")
        
    pause()

def add_contact(name, phone):
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    connection.commit()
    print(Fore.GREEN + f"✅ Contact '{name}' added successfully!")

def update_contact(serial_id, name, phone):
    cursor.execute("UPDATE contacts SET name=?, phone=? WHERE id=?", (name, phone, serial_id))
    connection.commit()
    print(Fore.GREEN + f"✅ Contact ID {serial_id} updated successfully!")

def delete_contact(serial_id):
    cursor.execute("DELETE FROM contacts WHERE id=?", (serial_id,))
    connection.commit()
    print(Fore.GREEN + f"✅ Contact ID {serial_id} deleted successfully!")

def main():
    while True:
        clear_screen()
        print(Fore.MAGENTA + "=" * 40)
        print(Fore.MAGENTA + "📞 CALL LOG CONTACT INFORMATION")
        print(Fore.MAGENTA + "=" * 40)
        print(Fore.CYAN + "1. List all contacts")
        print("2. Add new contact")
        print("3. Update existing contact")
        print("4. Delete contact")
        print("5. Exit")
        print(Fore.MAGENTA + "=" * 40)

        try:
            choice = int(input(Fore.YELLOW + "Enter your choice: "))
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number!")
            pause()
            continue

        if choice == 1:
            list_contacts()

        elif choice == 2:
            name = input("Enter new contact name: ")
            phone = input("Enter new contact phone: ")
            add_contact(name, phone)
            pause()

        elif choice == 3:
            serial_id = input("Enter the contact ID to update: ")
            name = input("Enter updated name: ")
            phone = input("Enter updated phone: ")
            update_contact(serial_id, name, phone)
            pause()

        elif choice == 4:
            serial_id = input("Enter the contact ID to delete: ")
            delete_contact(serial_id)
            pause()

        elif choice == 5:
            print(Fore.YELLOW + "👋 Goodbye!")
            break

        else:
            print(Fore.RED + "❌ Invalid choice!")
            pause()

    connection.close()

if __name__ == "__main__":
    main()
