from tkinter import *
from tkinter import messagebox
import random
import time;
import datetime
root = Tk()
root.geometry("950x525+0+0")
root.title("Billing Machine")
Tops = Frame(root, width=1350, height=750, bd=0, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width=900, height=525, bd=0, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=525, bd=1, relief="raise")
f2.pack(side=TOP)
f1a = Frame(f1, width=900, height=330, bd=0, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=0, relief="raise")
f2a.pack(side=BOTTOM)
f1aa = Frame(f1a, width=400, height=430, bd=0, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=0, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=450, height=330, bd=0, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=1, relief="raise")
f2ab.pack(side=RIGHT)
lblInfo=Label(Tops, font=('arial',60,'bold'), text=(" King Billing System "), bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
#====Calculator=====
text_Input = StringVar()
operator=""
PaymentRef = StringVar()
pizza = StringVar()
burger = StringVar()
drink = StringVar()
HomeDelivery = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Costofpizza = StringVar()
Costofburger = StringVar()
Costofdrink = StringVar()
CostofDelivery = StringVar()
DateofOrder = StringVar()
pizza.set(0)
burger.set(0)
drink.set(0)
HomeDelivery.set(0)
DateofOrder.set(time.strftime("%d/%m/%Y"))
def CostOfOrder():
    pizzaPrice = float(pizza.get())
    drinkPrice = float(drink.get())
    burgerPrice = float(burger.get())
    DeliveryCost = float(HomeDelivery.get())
    pizzaCost = "₹", str('%.2f'%((pizzaPrice * 15.50)))
    Costofpizza.set(pizzaCost)
    drinkCost = "₹", str('%.2f'%((drinkPrice * 7.49)))
    Costofdrink.set(drinkCost)
    burgerCost = "₹", str('%.2f'%((burgerPrice * 5.50)))
    Costofburger.set(burgerCost)
    Delivery = "₹", str('%.2f'%((DeliveryCost * 4.50)))
    CostofDelivery.set(Delivery)
    ToC = "₹", str('%.2f'%((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)))
    SubTotal.set(ToC)
    Tax = "₹", str('%.2f'%(((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)) * 0.2))
    PaidTax.set(Tax)
    TaxPay = (((pizzaPrice * 15.50)+(drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)) * 0.2)
    Cost = ((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50))
    CostofItems = "₹", str('%.2f'%(TaxPay + Cost))
    TotalCost.set(CostofItems)
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)
def PayReference():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)
def iExit():
    qExit = messagebox.askyesno("Billing System", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    PaymentRef.set("")
    pizza.set(0)
    burger.set(0)
    drink.set(0)
    HomeDelivery.set(0)
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Costofpizza.set("")
    Costofdrink.set("")
    Costofburger.set("")
    CostofDelivery.set("")
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""








