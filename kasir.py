import tkinter as tk
from tkinter import messagebox
import os

class MallCashierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mall Cashier System")
        self.root.geometry("500x600")

        # Variables
        self.item_name = tk.StringVar()
        self.item_price = tk.DoubleVar()
        self.item_quantity = tk.IntVar()
        self.total_amount = 0
        self.receipt = []

        # Title Label
        title_label = tk.Label(root, text="Mall Cashier System", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Item Entry Frame
        frame = tk.Frame(root)
        frame.pack(pady=20)

        # Item Name
        item_name_label = tk.Label(frame, text="Item Name")
        item_name_label.grid(row=0, column=0, padx=10, pady=5)
        item_name_entry = tk.Entry(frame, textvariable=self.item_name)
        item_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Item Price
        item_price_label = tk.Label(frame, text="Item Price")
        item_price_label.grid(row=1, column=0, padx=10, pady=5)
        item_price_entry = tk.Entry(frame, textvariable=self.item_price)
        item_price_entry.grid(row=1, column=1, padx=10, pady=5)

        # Item Quantity
        item_quantity_label = tk.Label(frame, text="Quantity")
        item_quantity_label.grid(row=2, column=0, padx=10, pady=5)
        item_quantity_entry = tk.Entry(frame, textvariable=self.item_quantity)
        item_quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add to Cart Button
        add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack(pady=10)

        # Receipt Text Box
        self.receipt_text = tk.Text(root, height=15, width=50)
        self.receipt_text.pack(pady=10)

        # Total Label
        self.total_label = tk.Label(root, text=f"Total: Rp {self.total_amount}", font=("Arial", 14, "bold"))
        self.total_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        reset_button.grid(row=0, column=0, padx=10)

        checkout_button = tk.Button(button_frame, text="Checkout", command=self.checkout)
        checkout_button.grid(row=0, column=1, padx=10)

        print_button = tk.Button(button_frame, text="Print Receipt", command=self.print_receipt)
        print_button.grid(row=0, column=2, padx=10)

    def add_to_cart(self):
        item_name = self.item_name.get()
        item_price = self.item_price.get()
        item_quantity = self.item_quantity.get()

        if item_name == "" or item_price == 0 or item_quantity == 0:
            messagebox.showwarning("Input Error", "Please fill all fields correctly.")
            return

        total_item_price = item_price * item_quantity
        self.total_amount += total_item_price
        self.receipt.append(f"{item_name}\t{item_quantity}x\tRp {total_item_price}\n")

        # Update receipt display
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, "".join(self.receipt))

        # Update total display
        self.total_label.config(text=f"Total: Rp {self.total_amount}")

        # Clear inputs
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.set(0)

    def reset(self):
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.set(0)
        self.receipt.clear()
        self.receipt_text.delete(1.0, tk.END)
        self.total_amount = 0
        self.total_label.config(text=f"Total: Rp {self.total_amount}")

    def checkout(self):
        if self.total_amount == 0:
            messagebox.showinfo("Checkout", "No items in the cart.")
        else:
            messagebox.showinfo("Checkout", f"Total payment: Rp {self.total_amount}\nThank you for shopping!")
            self.reset()

    def print_receipt(self):
        if self.total_amount == 0:
            messagebox.showinfo("Print Error", "No items to print.")
            return

        # Create a receipt file
        receipt_file = "receipt.txt"
        with open(receipt_file, "w") as file:
            file.write("Mall Cashier System\n")
            file.write("====================================\n")
            for item in self.receipt:
                file.write(item)
            file.write("====================================\n")
            file.write(f"Total: Rp {self.total_amount}\n")
            file.write("Thank you for shopping!\n")

        # Display message
        messagebox.showinfo("Print Receipt", f"Receipt saved as {receipt_file}")

        # Optionally: Automatically open the file (only works on some systems)
        os.startfile(receipt_file)  # This is for Windows. On Linux/Mac, you can use subprocess to open the file.

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = MallCashierApp(root)
    root.mainloop()