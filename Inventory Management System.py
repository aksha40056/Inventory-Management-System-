

              #############  #      INVENTORY MEANAGEMENT SYSTEM   #  ################


import tkinter as tk
from tkinter import messagebox
import sqlite3

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()

        # Create table
        self.c.execute("""CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            price REAL NOT NULL
                            )""")

        self.conn.commit()

        # Create main frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(fill="x")

        self.middle_frame = tk.Frame(self.main_frame)
        self.middle_frame.pack(fill="both", expand=True)

        self.bottom_frame = tk.Frame(self.main_frame)
        self.bottom_frame.pack(fill="x")

        # Create labels and entries
        self.name_label = tk.Label(self.top_frame, text="Product Name:")
        self.name_label.pack(side="left")

        self.name_entry = tk.Entry(self.top_frame)
        self.name_entry.pack(side="left")

        self.quantity_label = tk.Label(self.top_frame, text="Quantity:")
        self.quantity_label.pack(side="left")

        self.quantity_entry = tk.Entry(self.top_frame)
        self.quantity_entry.pack(side="left")

        self.price_label = tk.Label(self.top_frame, text="Price:")
        self.price_label.pack(side="left")

        self.price_entry = tk.Entry(self.top_frame)
        self.price_entry.pack(side="left")

        # Create buttons
        self.add_button = tk.Button(self.bottom_frame, text="Add Product", command=self.add_product)
        self.add_button.pack(side="left")

        self.edit_button = tk.Button(self.bottom_frame, text="Edit Product", command=self.edit_product)
        self.edit_button.pack(side="left")

        self.delete_button = tk.Button(self.bottom_frame, text="Delete Product", command=self.delete_product)
        self.delete_button.pack(side="left")

        self.report_button = tk.Button(self.bottom_frame, text="Generate Report", command=self.generate_report)
        self.report_button.pack(side="left")

        # Create text box
        self.text_box = tk.Text(self.middle_frame)
        self.text_box.pack(fill="both", expand=True)

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
    
    def about(self):
        messagebox.showinfo("About","Inventory Management System")    

    def add_product(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if name and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)

                self.c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
                self.conn.commit()
                self.text_box.insert("end", f"Product {name} added successfully.\n")
            except Exception as e:
                self.text_box.insert("end", f"Error: {e}\n")
        else:
            self.text_box.insert("end", "Please fill in all fields.\n")

    def edit_product(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if name and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)

                self.c.execute("UPDATE products SET quantity = ?, price = ? WHERE name = ?", (quantity, price, name))
                self.conn.commit()
                self.text_box.insert("end", f"Product {name} updated successfully.\n")
            except Exception as e:
                self.text_box.insert("end", f"Error: {e}\n")
        else:
            self.text_box.insert("end", "Please fill in all fields.\n")

    def delete_product(self):
        name = self.name_entry.get()

        if name:
            
                self.c.execute("DELETE FROM products WHERE name = ?", (name,))
                self.conn.commit()
                self.text_box.insert("end", f"Product {name} deleted successfully.\n")
                self.name_entry.delete(0,"end")
        else:
            self.text_box.insert("end", "Please fill in the product name.\n")

    def generate_report(self):
        self.text_box.delete(1.0, "end")
        self.c.execute("SELECT * FROM products")
        products = self.c.fetchall()
        self.text_box.insert("end"," Product Name \t    Quantity   \t   Price\n")
        self.text_box.insert("end","-------------------------------------------------------------------------------\n")
        self.text_box.insert("end","-------------------------------------------------------------------------------\n")
        for i, product in enumerate(products, start=1):
            self.text_box.insert("end",f"{i}. {product[1]}           \t{product[2]}            \t{product[3]}\n")
if __name__=="__main__":
      root = tk.Tk()
      app =InventoryManagementSystem(root)
      root.mainloop()
