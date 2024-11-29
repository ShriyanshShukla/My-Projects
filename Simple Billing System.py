from tkinter import *
from tkinter import messagebox
import random

# *****GENERATE RANDOM NUMBERS****
table_number = random.randint(1,20)
bill_number = random.randint(100,500)

# *****FUNCTIONS*****
def clear():
    paneer_tikka_entry.delete(0, END)
    honey_chilli_patato_entry.delete(0, END)
    hakka_noodles_entry.delete(0, END)
    crispy_corn_entry.delete(0, END)
    veg_kothe_entry.delete(0, END)

    jeera_masala_soda_entry.delete(0, END)
    virgin_mojito_entry.delete(0, END)
    blue_lemon_entry.delete(0, END)
    cold_coffee_entry.delete(0, END)
    oreo_shake_entry.delete(0, END)

    paneer_tikka_entry.insert(0, 0)
    honey_chilli_patato_entry.insert(0, 0)
    hakka_noodles_entry.insert(0, 0)
    crispy_corn_entry.insert(0, 0)
    veg_kothe_entry.insert(0, 0)

    jeera_masala_soda_entry.insert(0, 0)
    virgin_mojito_entry.insert(0, 0)
    blue_lemon_entry.insert(0, 0)
    cold_coffee_entry.insert(0, 0)
    oreo_shake_entry.insert(0, 0)

    snacks_price_entry.delete(0, END)
    beverages_price_entry.delete(0, END)
    snacks_tax_entry.delete(0, END)
    beverages_tax_entry.delete(0,END)

    name_entry.delete(0, END)

    text.delete(1.0, END)

def total():
    if name_entry.get()=='':
        return messagebox.showerror('Error', "Please Add Customer Name")

    # *****TOTAL SNACKS VALUE WITH TAXS*****
    pt_value = int(paneer_tikka_entry.get())*170
    hcp_value = int(honey_chilli_patato_entry.get())*150
    hn_value = int(hakka_noodles_entry.get())*130
    cc_value = int(crispy_corn_entry.get())*130
    vk_value = int(crispy_corn_entry.get())*140

    total_snacks_value = pt_value+hcp_value+hn_value+cc_value+vk_value
    snacks_price_entry.delete(0, END)
    snacks_price_entry.insert(0, f'{total_snacks_value} Rs')

    total_snacks_tax = total_snacks_value*0.05
    snacks_tax_entry.delete(0, END)
    snacks_tax_entry.insert(0, f'{total_snacks_tax} Rs')

    # *****TOTAL BEVERAGES VALUE WITH TAXS*****
    jms_value = int(jeera_masala_soda_entry.get())*110
    vm_value = int(virgin_mojito_entry.get())*150
    bl_value = int(blue_lemon_entry.get())*190
    cf_value = int(cold_coffee_entry.get())*110
    os_value = int(oreo_shake_entry.get())*170

    total_beverages_value = jms_value+vm_value+bl_value+cf_value+os_value
    beverages_price_entry.delete(0, END)
    beverages_price_entry.insert(0, f'{total_beverages_value} Rs')

    total_beverages_tax = total_beverages_value*0.05
    beverages_tax_entry.delete(0, END)
    beverages_tax_entry.insert(0, f'{total_beverages_tax} Rs')

    total_bill = total_snacks_value+total_beverages_value+total_snacks_tax+total_beverages_tax

    # *****BILL*****
    text.delete(1.0, END)

    text.insert(END, "     *****Vyanjan Restaurant*****\n\n")
    text.insert(END, f"Table Number: {table_number}\n")
    text.insert(END, f"Bill Number: {bill_number}\n")
    text.insert(END, f"Customer Name: {name_entry.get()}\n")

    text.insert(END, "------------------------------------\n")

    text.insert(END, "Items\t        QTY\t       Price\n")
    if int(paneer_tikka_entry.get())!=0:
        text.insert(END, f"Panner Tikka\t\t{paneer_tikka_entry.get()}\t   {pt_value} Rs\n")
    if int(honey_chilli_patato_entry.get())!=0:
        text.insert(END, f"Chilli Patato\t\t{honey_chilli_patato_entry.get()}\t   {hcp_value} Rs\n")
    if int(hakka_noodles_entry.get())!=0:
        text.insert(END, f"Hakka Noodels\t\t{hakka_noodles_entry.get()}\t   {hn_value} Rs\n")
    if int(crispy_corn_entry.get())!=0:
        text.insert(END, f"Crispy Corn\t\t{crispy_corn_entry.get()}\t   {cc_value} Rs\n")
    if int(veg_kothe_entry.get())!=0:
        text.insert(END, f"Veg Kothe\t\t{veg_kothe_entry.get()}\t   {vk_value} Rs\n")

    if int(jeera_masala_soda_entry.get())!=0:
        text.insert(END, f"Masala Soda\t\t{jeera_masala_soda_entry.get()}\t   {jms_value} Rs\n")
    if int(virgin_mojito_entry.get())!=0:
        text.insert(END, f"Virgin Mojito\t\t{virgin_mojito_entry.get()}\t   {vm_value} Rs\n")
    if int(blue_lemon_entry.get())!=0:
        text.insert(END, f"Blue Lemon\t\t{blue_lemon_entry.get()}\t   {bl_value} Rs\n")
    if int(cold_coffee_entry.get())!=0:
        text.insert(END, f"Cold Coffee\t\t{cold_coffee_entry.get()}\t   {cf_value} Rs\n")
    if int(oreo_shake_entry.get())!=0:
        text.insert(END, f"Oreo Shake\t\t{oreo_shake_entry.get()}\t   {os_value} Rs\n")

    text.insert(END, "------------------------------------\n")

    if snacks_tax_entry.get()!='0.0 Rs':
        text.insert(END, f"Snacks Tax\t\t\t   {total_snacks_tax} Rs\n")
    if beverages_tax_entry.get()!='0.0 Rs':
        text.insert(END, f"Beverages Tax\t\t\t   {total_beverages_tax} Rs\n")

    text.insert(END, "------------------------------------\n")

    text.insert(END, f"Total Net Amount\t\t\t   {total_bill} Rs")

root = Tk()
root.title("Simple Billing System")
root.geometry('1025x600')

# *****HEADING*****
heading = Label(root, text="Vyanjan Restaurant", font=("Times New Roman",25,'bold'), bg='DodgerBlue4', fg='yellow2', bd=15, relief=RAISED)
heading.pack(fill=X, pady=2)

# *****CUSTOMER DETAILS*****
customer_details = LabelFrame(root, text="Customer Detail", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='yellow2', bd=15, relief=RAISED)
customer_details.pack(fill=X)

name = Label(customer_details, text='Name', font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
name.grid(row=0, column=0, padx=18, pady=3)
name_entry = Entry(customer_details, font=("Times New Roman",15), bd=8, width=18)
name_entry.grid(row=0, column=1, padx=18, pady=3)

bill = Label(customer_details, text='Bill No.', font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
bill.grid(row=0, column=2, padx=18, pady=3)
bill_entry = Entry(customer_details, font=("Times New Roman",15), bd=8, width=18)
bill_entry.grid(row=0, column=3, padx=18, pady=3)
bill_entry.insert(0, bill_number)

# *****ITEMS*****
items = Frame(root)
items.pack(pady=2)

# *****SNACKS*****
snacks = LabelFrame(items, text='Snacks', font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='yellow2', bd=15, relief=RAISED)
snacks.grid(row=0, column=0)

paneer_tikka = Label(snacks, text="Paneer Tikka (8 Pc.)", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
paneer_tikka.grid(row=0, column=0, padx=5, pady= 5)
paneer_tikka_entry = Entry(snacks, font=("Times New Roman",15), bd=8, width=10)
paneer_tikka_entry.grid(row=0, column=1, padx=5, pady= 5)
paneer_tikka_entry.insert(0, 0)

honey_chilli_patato = Label(snacks, text="Honey Chilli Patato", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
honey_chilli_patato.grid(row=1, column=0, padx=5, pady= 5)
honey_chilli_patato_entry = Entry(snacks, font=("Times New Roman",15), bd=8, width=10)
honey_chilli_patato_entry.grid(row=1, column=1, padx=5, pady= 5)
honey_chilli_patato_entry.insert(0, 0)

hakka_noodles = Label(snacks, text="Hakka Noodles", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
hakka_noodles.grid(row=2, column=0, padx=5, pady= 5)
hakka_noodles_entry = Entry(snacks, font=("Times New Roman",15), bd=8, width=10)
hakka_noodles_entry.grid(row=2, column=1, padx=5, pady= 5)
hakka_noodles_entry.insert(0, 0)

crispy_corn = Label(snacks, text="Crispy Corn", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
crispy_corn.grid(row=3, column=0, padx=5, pady= 5)
crispy_corn_entry = Entry(snacks, font=("Times New Roman",15), bd=8, width=10)
crispy_corn_entry.grid(row=3, column=1, padx=5, pady= 5)
crispy_corn_entry.insert(0, 0)

veg_kothe = Label(snacks, text="Veg Kothe", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
veg_kothe.grid(row=4, column=0, padx=5, pady= 5)
veg_kothe_entry = Entry(snacks, font=("Times New Roman",15), bd=8, width=10)
veg_kothe_entry.grid(row=4, column=1, padx=5, pady= 5)
veg_kothe_entry.insert(0, 0)

# *****BEVERAGES*****
beverages = LabelFrame(items, text='Beverages', font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='yellow2', bd=15, relief=RAISED)
beverages.grid(row=0, column=1)

jeera_masala_soda = Label(beverages, text="Jeera Masala Soda", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
jeera_masala_soda.grid(row=0, column=0, padx=5, pady= 5)
jeera_masala_soda_entry = Entry(beverages, font=("Times New Roman",15), bd=8, width=10)
jeera_masala_soda_entry.grid(row=0, column=1, padx=5, pady= 5)
jeera_masala_soda_entry.insert(0, 0)

virgin_mojito = Label(beverages, text="Virgin Mojito", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
virgin_mojito.grid(row=1, column=0, padx=5, pady= 5)
virgin_mojito_entry = Entry(beverages, font=("Times New Roman",15), bd=8, width=10)
virgin_mojito_entry.grid(row=1, column=1, padx=5, pady= 5)
virgin_mojito_entry.insert(0, 0)

blue_lemon = Label(beverages, text="Blue Lemon", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
blue_lemon.grid(row=2, column=0, padx=5, pady= 5)
blue_lemon_entry = Entry(beverages, font=("Times New Roman",15), bd=8, width=10)
blue_lemon_entry.grid(row=2, column=1, padx=5, pady= 5)
blue_lemon_entry.insert(0, 0)

cold_coffee = Label(beverages, text="Cold Coffee", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
cold_coffee.grid(row=3, column=0, padx=5, pady= 5)
cold_coffee_entry = Entry(beverages, font=("Times New Roman",15), bd=8, width=10)
cold_coffee_entry.grid(row=3, column=1, padx=5, pady= 5)
cold_coffee_entry.insert(0, 0)

oreo_shake = Label(beverages, text="Oreo Shake", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='snow')
oreo_shake.grid(row=4, column=0, padx=5, pady= 5)
oreo_shake_entry = Entry(beverages, font=("Times New Roman",15), bd=8, width=10)
oreo_shake_entry.grid(row=4, column=1, padx=5, pady= 5)
oreo_shake_entry.insert(0, 0)

# *****BILL*****
bill_area = Frame(items, bd=8, relief=RAISED)
bill_area.grid(row=0, column=3, pady=2)

bill = Label(bill_area, text="Bill", font=("Times New Romen",15,'bold'), bd=8, relief=RAISED)
bill.pack(fill=X)

text = Text(bill_area, height=14, width=36)
text.pack()

# *****PRICES*****
prices = LabelFrame(root, text="Prices", font=("Times New Romen",15,'bold'), bg='DodgerBlue4', fg='yellow2', bd=15, relief=RAISED)
prices.pack(fill=X)

snacks_price = Label(prices, text='Snacks Price', font=("Times New Romen",10,'bold'), bg='DodgerBlue4', fg='snow')
snacks_price.grid(row=0, column=0, padx=33, pady=1)
snacks_price_entry = Entry(prices, font=("Times New Roman",10), bd=8, width=18)
snacks_price_entry.grid(row=0, column=1, padx=33, pady=10)

beverages_price = Label(prices, text='Beverages Price', font=("Times New Romen",10,'bold'), bg='DodgerBlue4', fg='snow')
beverages_price.grid(row=1, column=0, padx=33, pady=1)
beverages_price_entry = Entry(prices, font=("Times New Roman",10), bd=8, width=18)
beverages_price_entry.grid(row=1, column=1, padx=33, pady=10)

snacks_tax = Label(prices, text='Snacks Tax(5%)', font=("Times New Romen",10,'bold'), bg='DodgerBlue4', fg='snow')
snacks_tax.grid(row=0, column=2, padx=28, pady=1)
snacks_tax_entry = Entry(prices, font=("Times New Roman",10), bd=8, width=18)
snacks_tax_entry.grid(row=0, column=3, padx=10, pady=10)

beverages_tax = Label(prices, text='Beverages Tax(5%)', font=("Times New Romen",10,'bold'), bg='DodgerBlue4', fg='snow')
beverages_tax.grid(row=1, column=2, padx=28, pady=1)
beverages_tax_entry = Entry(prices, font=("Times New Roman",10), bd=8, width=18)
beverages_tax_entry.grid(row=1, column=3, padx=10, pady=10)

# *****BUTTONS*****

buttons = Frame(prices, bd=8, relief=RAISED)
buttons.grid(row=0, column=4, rowspan=2, padx=10)

total_button = Button(buttons, text='Total', font=("Times New Roman",15,'bold'), bg='gray90', fg='gray10', bd=5, width=7, command=total)
total_button.grid(row=0, column=0, padx=17, pady=7)

clear_button = Button(buttons, text='Clear', font=("Times New Roman",15,'bold'), bg='gray90', fg='gray10', bd=5, width=7, command=clear)
clear_button.grid(row=0, column=1, padx=17, pady=7)
root.mainloop()