from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")

alphalist =
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

label1 = Label(root)

def randomword():
    random_no1 = random.randint(0,25)
    random_no2 = random.randint(0,25)
    random_no3 = random.randint(0,25)
    random_no4 = random.randint(0,25)
    random_no5 = random.randint(0,25)
    random_alpha1 = alphalist[random_no1]
    random_alpha2 = alphalist[random_no2]
    random_alpha3 = alphalist[random_no3]
    random_alpha4 = alphalist[random_no4]
    random_alpha5 = alphalist[random_no5]
    label1['text'] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5

btn = Button(root, text="Generate Random Words", command=randomword)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)

label1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()