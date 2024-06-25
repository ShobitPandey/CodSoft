import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, contact_number, email, address):
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added")

    def view_contacts(self):    
        return self.contacts

    def search_contacts(self, search_label):
        found_contacts = []
        for contact in self.contacts:
            if search_label.lower() in contact.name.lower() or search_label in contact.contact_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                print("Contact updated")
                return True
        print("Contact not found")
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted")
                return True
        print("Contact not found")
        return False

class ContactBookApp:
    def __init__(self, root):
        self.contact_book = ContactBook()
        self.root = root
        self.root.title("Contact Book")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.contact_number_label = tk.Label(root, text="Phone Number:")
        self.contact_number_label.grid(row=1, column=0)
        self.contact_number_entry = tk.Entry(root)
        self.contact_number_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contacts)
        self.search_button.grid(row=7, column=0, columnspan=2)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, contact_number, email, address)
        self.contact_book.add_contact(contact)
        messagebox.showinfo("Success", "Contact added")

    def view_contacts(self):
        contacts = self.contact_book.view_contacts()
        if contacts:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.contact_number}" for contact in contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts to display")

    def search_contacts(self):
        search_label = self.search_entry.get()
        found_contacts = self.contact_book.search_contacts(search_label)
        if found_contacts:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.contact_number}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Search Results", "No similar contacts found")

    def update_contact(self):
        name = self.name_entry.get()
        new_name = self.name_entry.get()
        new_contact_number = self.contact_number_entry.get()
        new_email = self.email_entry.get()
        new_address = self.address_entry.get()
        new_contact = Contact(new_name, new_contact_number, new_email, new_address)
        success = self.contact_book.update_contact(name, new_contact)
        if success:
            messagebox.showinfo("Success", "Contact updated")
        else:
            messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        name = self.name_entry.get()
        success = self.contact_book.delete_contact(name)
        if success:
            messagebox.showinfo("done", "Contact deleted")
        else:
            messagebox.showerror("Error", "Contact not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
