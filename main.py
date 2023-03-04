from tkinter import *
from tkinter.simpledialog import askfloat
from  tkinter import messagebox
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO:

# TODO: Make Coffee
def make_coffee(data):
    resources["milk"] = resources["milk"] - data["milk"]
    resources["water"] = resources["water"] - data["water"]
    resources["coffee"] = resources["coffee"] - data["coffee"]
    canvas.itemconfig(text2, text="you coffee is ready")

    return resources
#TODO: prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def promt(user):
    def product_resource(data,data2):
        if data["water"] <= resources["water"]:
            if data["milk"] <= resources["milk"]:
                if data["coffee"] <= resources["coffee"]:
                    return transaction(data2, data)
                else:
                    messagebox.showinfo("Coffee Resources","no coffee to make your drink")
                    return resources
            else:
                messagebox.showinfo("Coffee Resources","no milk for make your drink.")
                return resources
        else:
            messagebox.showinfo("Coffee Resources","no water to make your drink.")
            return resources
    def check():
        if user_input == "latte":
            data = MENU["latte"]["ingredients"]
            data2 = MENU["latte"]["cost"]
            return product_resource(data,data2)
        elif user_input == "espresso":
            data = MENU["espresso"]["ingredients"]
            data2 = MENU["espresso"]["cost"]
            return product_resource(data,data2)
        elif user_input == "cappuccino":
            data = MENU["cappuccino"]["ingredients"]
            data2 = MENU["cappuccino"]["cost"]
            return product_resource(data,data2)
        elif user_input == "off":
            off()
        elif user_input == "report":
            return resources_of_machine()

    # TODO:Check transaction successful?
    def transaction(amount,data):
        total_amount = money()
        if total_amount >= amount:
            canvas.itemconfig(text, text=f"your change is \n${round(total_amount-amount,2)}")
            return make_coffee(data)
        else:
            canvas.itemconfig(text, text=f"Sorry that's not \nenough money. Money .\nrefunded. ${round(total_amount,2)}")
    user_input = user
    return check()

#TODO: Turn off the Coffee Machine by entering “off” to the prompt.
def off():
    exit()


# TODO: Check resources sufficient?
def resources_of_machine():
    canvas.itemconfig(text, text=f"Water: {resources['water']}\n\n\nMilk: {resources['milk']}\n\n\nCoffee: {resources['coffee']}")
    return resources

#TODO : Process coins.
def money():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    quarters_user = askfloat("Quarters","How many quarters?: ")
    dimes_user = askfloat("Dimes","How many dimes?: ")
    nickles_user = askfloat("Nickles","How many nickles?: ")
    pennies_user = askfloat("Pennies","How many pennies?: ")
    return (quarters*quarters_user)+(dimes*dimes_user)+(nickles*nickles_user)+(pennies*pennies_user)



def lt_function():
    canvas.itemconfig(text2, text="")
    resources = promt("latte")
    return resources


def cp_function():
    canvas.itemconfig(text2, text="")
    resources = promt("cappuccino")
    return resources


def ep_function():
    canvas.itemconfig(text2, text="")
    resources = promt("espresso")
    return resources


def rep_function():
    canvas.itemconfig(text2, text="")
    resources = promt("report")
    return resources




# #TODO: RUN
# while True:
#     resources = promt()

#TODO: GUI
def coffer_page():
    global text,text2
    canvas.delete("all")
    canvas.create_image(275, 170, image=background)
    canvas.create_image(150, 162, image=on_coffee_machine)
    canvas.create_image(412, 162, image=screen)
    text = canvas.create_text(440,149, text="", font=("Copperplate Gothic Bold", 9), fill="#ffffff")
    text2 = canvas.create_text(445,189, text="", font=("Copperplate Gothic Bold", 9), fill="#ffffff")

    lt = Button(image=latte, border=0, bg="#00557b", command=lt_function)
    lt.place(x=302, y=66)
    cp = Button(image=cappuccino, border=0, bg="#00557b", command=cp_function)
    cp.place(x=302, y=106)
    ep = Button(image=espresso, border=0, bg="#00557b", command=ep_function)
    ep.place(x=302, y=146)
    rep = Button(image=report, border=0, bg="#00557b", command=rep_function)
    rep.place(x=302, y=186)
    ext = Button(image=extt, border=0, bg="#00557b", command=off)
    ext.place(x=302, y=226)
    pass
def loading_page():
    canvas.create_image(275,170, image=background)
    canvas.create_image(150,162, image=off_coffee_machine)
    canvas.create_text(412,152,text="COFFEE \n      MACHINE", font=("Copperplate Gothic Bold", 28), fill="#ffffff")
    canvas.after(3000, coffer_page)


home = Tk()
home.title("Coffee Machine")
home.geometry("550x340")
off_coffee_machine = PhotoImage(file="image/coffee_machine.png")
on_coffee_machine = PhotoImage(file="image/coffee_machine_on.png")
latte = PhotoImage(file="image/latte.png")
cappuccino = PhotoImage(file="image/cappuccino.png")
espresso = PhotoImage(file="image/espresso.png")
background = PhotoImage(file="image/background.png")
screen = PhotoImage(file="image/Screen.png")
report = PhotoImage(file="image/report.png")
extt = PhotoImage(file="image/exit.png")
canvas = Canvas(width=560, height=350)
canvas.place(x=-2,y=-2)
loading_page()
home.mainloop()