# qr-code-generator
A Tkinter-based desktop application written in Python to generate custom Personal and Business contact QR codes and save them as PNG images.

# Personal & Business QR Code Generator

A simple Python desktop application built using Tkinter and the `qrcode` library to quickly generate personal and business contact QR codes and save them as PNG files.

## Features

- **Personal QR Code:** Generates QR codes containing Name, Address, and Phone Number.
- **Business QR Code:** Generates QR codes containing Business Name, Address, Phone Number, and Owner's Name.
- Dynamic GUI switching between Personal and Business modes using Tkinter.
- Automatic file naming based on the entered name or business name.
- Instant success notification upon image saving.

## Prerequisites

Make sure you have Python installed on your system. You will also need the `qrcode` package along with `Pillow` for image creation[cite: 1].

You can install the required dependency using pip:

```bash
pip install qrcode pillow
