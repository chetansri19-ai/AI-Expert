import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Stationery Order Management App")
root.geometry("900x600")

canvas = tk.Canvas(root, width=900, height=600, bg="white")
canvas.pack(fill="both", expand=True)

frame = ttk.Frame(canvas)
canvas.create_window(450, 300, window=frame)

items = ["Pens", "Pencils", "Erasers", "Markers", "Notebooks"]
prices_usd = [1, 0.5, 0.2, 1.5, 3]
prices_inr = [80, 40, 16, 120, 240]

currency = tk.StringVar(value="USD")

def switch_currency():
    for i, row in enumerate(rows):
        row["price"].config(text=str(prices_usd[i]) if currency.get() == "USD" else str(prices_inr[i]))

def calculate_total():
    total = 0
    for i, row in enumerate(rows):
        qty = row["qty"].get()
        if qty.isdigit():
            qty = int(qty)
            price = prices_usd[i] if currency.get() == "USD" else prices_inr[i]
            total += qty * price
    total_label.config(text=str(total))

rows = []

for i, item in enumerate(items):
    lbl = ttk.Label(frame, text=item)
    lbl.grid(row=i, column=0, padx=10, pady=10)
    price_lbl = ttk.Label(frame, text=str(prices_usd[i]))
    price_lbl.grid(row=i, column=1, padx=10, pady=10)
    qty_entry = ttk.Entry(frame, width=10)
    qty_entry.grid(row=i, column=2, padx=10, pady=10)
    rows.append({"price": price_lbl, "qty": qty_entry})

currency_menu = ttk.OptionMenu(frame, currency, "USD", "USD", "INR", command=lambda x: switch_currency())
currency_menu.grid(row=len(items), column=0, pady=20)

calc_btn = ttk.Button(frame, text="Calculate Total", command=calculate_total)
calc_btn.grid(row=len(items), column=1, pady=20)

total_label = ttk.Label(frame, text="0")
total_label.grid(row=len(items), column=2, pady=20)

root.mainloop()