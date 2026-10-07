import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

data = []


def add_data():
    try:
        ID = id_entry.get()
        volt = float(volt_entry.get())
        amp = float(amp_entry.get())

        if ID == "":
            messagebox.showerror("Error", "กรุณากรอก ID")
            return

        data.append((ID, volt, amp))

        table.insert(
            "",
            tk.END,
            values=(ID, volt, amp)
        )

        id_entry.delete(0, tk.END)
        volt_entry.delete(0, tk.END)
        amp_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Volt และ Amp ต้องเป็นตัวเลข"
        )


def plot_graph():
    if len(data) == 0:
        messagebox.showwarning(
            "ไม่มีข้อมูล",
            "กรุณาเพิ่มข้อมูลก่อน"
        )
        return

    volt = [x[1] for x in data]
    amp = [x[2] for x in data]
    labels = [x[0] for x in data]

    plt.figure(figsize=(8, 5))

    plt.plot(
        volt,
        amp,
        "o-"
    )

    for x, y, label in zip(volt, amp, labels):
        plt.annotate(
            label,
            (x, y),
            xytext=(5, 5),
            textcoords="offset points"
        )

    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Voltage vs Current")
    plt.grid(True)

    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Plot Graph - Data Analytics")
root.geometry("600x450")

title = ttk.Label(
    root,
    text="Data Analytics - Plot Graph",
    font=("Arial", 18)
)
title.pack(pady=10)

form = ttk.Frame(root)
form.pack(pady=10)

ttk.Label(form, text="ID").grid(
    row=0, column=0, padx=5
)

ttk.Label(form, text="Volt").grid(
    row=0, column=1, padx=5
)

ttk.Label(form, text="Amp").grid(
    row=0, column=2, padx=5
)

id_entry = ttk.Entry(form, width=15)
volt_entry = ttk.Entry(form, width=15)
amp_entry = ttk.Entry(form, width=15)

id_entry.grid(row=1, column=0, padx=5)
volt_entry.grid(row=1, column=1, padx=5)
amp_entry.grid(row=1, column=2, padx=5)

ttk.Button(
    root,
    text="เพิ่มข้อมูล",
    command=add_data
).pack(pady=5)

ttk.Button(
    root,
    text="Plot Graph",
    command=plot_graph
).pack(pady=5)

# ตาราง
table = ttk.Treeview(
    root,
    columns=("ID", "Volt", "Amp"),
    show="headings"
)

table.heading("ID", text="ID")
table.heading("Volt", text="Volt (V)")
table.heading("Amp", text="Amp (A)")

table.column("ID", width=150)
table.column("Volt", width=150)
table.column("Amp", width=150)

table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

root.mainloop()
