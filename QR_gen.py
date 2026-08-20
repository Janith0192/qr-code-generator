import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    messagebox.showinfo("Success", f"QR code saved as {filename}")

def create_personal_qr():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    data = f"Name: {name}\nAddress: {address}\nPhone: {phone}"
    filename = f"{name.replace(' ', '_')}_personal_qr.png"  # Replace spaces with underscores
    generate_qr(data, filename)

def create_business_qr():
    business_name = business_name_entry.get()
    business_address = business_address_entry.get()
    business_phone = business_phone_entry.get()
    owner_name = owner_name_entry.get()
    data = f"Business Name: {business_name}\nAddress: {business_address}\nPhone: {business_phone}\nOwner: {owner_name}"
    filename = f"{business_name.replace(' ', '_')}_business_qr.png"  # Replace spaces with underscores
    generate_qr(data, filename)

app = tk.Tk()
app.title("QR Code Generator")

# Personal QR Section
personal_button = tk.Button(app, text="Personal QR", command=lambda: show_personal_qr_fields())
personal_button.pack(pady=5)

# Business QR Section
business_button = tk.Button(app, text="Business QR", command=lambda: show_business_qr_fields())
business_button.pack(pady=5)

# Input fields for personal QR
name_entry = tk.Entry(app)
address_entry = tk.Entry(app)
phone_entry = tk.Entry(app)

# Input fields for business QR
business_name_entry = tk.Entry(app)
business_address_entry = tk.Entry(app)
business_phone_entry = tk.Entry(app)
owner_name_entry = tk.Entry(app)

def show_personal_qr_fields():
    for widget in app.winfo_children():
        widget.pack_forget()
    tk.Label(app, text="Name").pack()
    name_entry.pack()
    tk.Label(app, text="Address").pack()
    address_entry.pack()
    tk.Label(app, text="Phone").pack()
    phone_entry.pack()
    tk.Button(app, text="Generate Personal QR", command=create_personal_qr).pack()

def show_business_qr_fields():
    for widget in app.winfo_children():
        widget.pack_forget()
    tk.Label(app, text="Business Name").pack()
    business_name_entry.pack()
    tk.Label(app, text="Address").pack()
    business_address_entry.pack()
    tk.Label(app, text="Phone").pack()
    business_phone_entry.pack()
    tk.Label(app, text="Owner's Name").pack()
    owner_name_entry.pack()
    tk.Button(app, text="Generate Business QR", command=create_business_qr).pack()

app.mainloop()
