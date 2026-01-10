from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def pass_generator():
    letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    return password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as f:
        s = web_entry.get() + " | " + mail_entry.get() + " | " + pass_entry.get() + "\n"
        web_entry.delete(0, "end")
        pass_entry.delete(0, "end")
        f.write(s)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#FFFFFF")

canvas = Canvas(width = 200, height = 200, bg= "#FFFFFF", highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row=0, column=1)
web_label = Label(text="Website", fg="#000000", bg="#FFFFFF")
web_label.grid(column=0, row=1)
web_entry = Entry(window, width = 35, bg="#FFFFFF",fg="#000000")
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

mail_label = Label(text="Email/Username", fg="#000000", bg="#FFFFFF")
mail_label.grid(column=0, row=2)
mail_entry = Entry(window, width = 35, bg="#FFFFFF", fg="#000000")
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "reyankhan@gmail.com")

pass_label = Label(text="Password", fg="#000000", bg="#FFFFFF")
pass_label.grid(column=0, row=3)
pass_entry = Entry(window, width = 18, bg="#FFFFFF", fg="#000000")
pass_entry.grid(row=3, column=1)
pword = pass_generator()
pass_entry.insert(0, pword)

pass_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="#FFFFFF")
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, highlightbackground="#FFFFFF", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()