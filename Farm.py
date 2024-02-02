import tkinter as tk
from tkinter import messagebox

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        item = item.lower()
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        item = item.lower()
        if item in self.inventory:
            if quantity < self.inventory[item]:
                self.inventory[item] -= quantity
            else:
                del self.inventory[item]
                print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

class InventoryManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.master.geometry("1920x1080")

        self.inventory_system = InventoryManagementSystem()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Inventory Management System")
        self.label.pack()

        self.add_button = tk.Button(self.master, text="Add Item", command=self.show_add_item_dialog)
        self.add_button.pack()

        self.remove_button = tk.Button(self.master, text="Remove Item", command=self.show_remove_item_dialog)
        self.remove_button.pack()

        self.display_button = tk.Button(self.master, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def show_add_item_dialog(self):
        add_dialog = AddItemDialog(self.master, self.inventory_system)

    def show_remove_item_dialog(self):
        remove_dialog = RemoveItemDialog(self.master, self.inventory_system)

    def display_inventory(self):
        inventory_dialog = InventoryDialog(self.master, self.inventory_system)

class AddItemDialog:
    def __init__(self, master, inventory_system):
        self.master = master
        self.inventory_system = inventory_system

        self.dialog = tk.Toplevel(self.master)
        self.dialog.title("Add Item")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.dialog, text="Enter item details:")
        self.label.pack()

        self.item_label = tk.Label(self.dialog, text="Item name:")
        self.item_label.pack()

        self.item_entry = tk.Entry(self.dialog)
        self.item_entry.pack()

        self.quantity_label = tk.Label(self.dialog, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self.dialog)
        self.quantity_entry.pack()

        self.add_button = tk.Button(self.dialog, text="Add", command=self.add_item)
        self.add_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        self.inventory_system.add_item(item, quantity)
        messagebox.showinfo("Success", f"Added {quantity} {item}(s) to inventory.")
        self.dialog.destroy()

class RemoveItemDialog:
    def __init__(self, master, inventory_system):
        self.master = master
        self.inventory_system = inventory_system

        self.dialog = tk.Toplevel(self.master)
        self.dialog.title("Remove Item")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.dialog, text="Enter item details:")
        self.label.pack()

        self.item_label = tk.Label(self.dialog, text="Item name:")
        self.item_label.pack()

        self.item_entry = tk.Entry(self.dialog)
        self.item_entry.pack()

        self.quantity_label = tk.Label(self.dialog, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self.dialog)
        self.quantity_entry.pack()

        self.remove_button = tk.Button(self.dialog, text="Remove", command=self.remove_item)
        self.remove_button.pack()

    def remove_item(self):
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        self.inventory_system.remove_item(item, quantity)
        self.dialog.destroy()

class InventoryDialog:
    def __init__(self, master, inventory_system):
        self.master = master
        self.inventory_system = inventory_system

        self.dialog = tk.Toplevel(self.master)
        self.dialog.title("Display Inventory")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.dialog, text="Current Inventory:")
        self.label.pack()

        for item, quantity in self.inventory_system.inventory.items():
            item_label = tk.Label(self.dialog, text=f"{item}: {quantity}")
            item_label.pack()

def main():
    root = tk.Tk()
    app = InventoryManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
