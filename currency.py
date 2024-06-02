import tkinter as tk
from tkinter import Frame, Label, Button, Entry, OptionMenu, StringVar, W, E
import tkinter.messagebox
from forex_python.converter import CurrencyRates

# GUI setup
root = tk.Tk()
root.title("Currency Converter: Power Project")
root.configure(background='#e6e5e5')
root.geometry("700x400")

# Top Frame
Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = Label(Tops, font=('lato black', 19, 'bold'), text='Currency Converter: Power Project', bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

# Variables
variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("currency")
variable2.set("currency")

# Function for real-time currency conversion
def RealTimeCurrencyConversion():
    c = CurrencyRates()
    from_currency = variable1.get()
    to_currency = variable2.get()

    if not Amount1_field.get():
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
        return

    if from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency from the menu.")
        return

    try:
        amount = float(Amount1_field.get())
        new_amt = c.convert(from_currency, to_currency, amount)
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, str(new_amount))
    except Exception as e:
        tkinter.messagebox.showinfo("Error !!", f"Failed to convert currency: {e}")

# Clear all fields
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

# Currency Code List
CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

# Labels and Entries
Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black").grid(row=1, column=0, sticky=W)

Label(root, font=('lato black', 15, 'bold'), text="    Amount  :  ", bg="#e6e5e5", fg="black").grid(row=2, column=0, sticky=W)
Amount1_field = Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Label(root, font=('lato black', 15, 'bold'), text="    From Currency  :  ", bg="#e6e5e5", fg="black").grid(row=3, column=0, sticky=W)
FromCurrency_option = OptionMenu(root, variable1, *CurrencyCode_list)
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)

Label(root, font=('lato black', 15, 'bold'), text="    To Currency  :  ", bg="#e6e5e5", fg="black").grid(row=4, column=0, sticky=W)
ToCurrency_option = OptionMenu(root, variable2, *CurrencyCode_list)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Label(root, font=('lato black', 15, 'bold'), text="    Converted Amount  :  ", bg="#e6e5e5", fg="black").grid(row=8, column=0, sticky=W)
Amount2_field = Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

# Buttons
Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white", command=RealTimeCurrencyConversion).grid(row=6, column=0)
Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white", command=clear_all).grid(row=10, column=0)

root.mainloop()
