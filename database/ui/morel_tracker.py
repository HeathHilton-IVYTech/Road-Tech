from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pandas as pd

#Overall declaration of global variables that the program uses
username = ""
password = ""
address = ""
city = ""
state = ""
notes = ""
date = ""
testFunction = False
lines = ""

#Create the initial project submittal screen with titles, labels, entry fields, and buttons
root = Tk()
root.geometry('500x600')
root.title("Morel Mushrooms")
root.iconbitmap("mushroom.ico")


titleLabel = Label(root, text="Morel Mushrooms Submitter", width=35, font=("bold", 20))
titleLabel.place(x=-30, y=53)

userLabel = Label(root, text="User Name:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
userLabel.place(x=28, y=130)
userName = Entry(root)
userName.place(x=200, y=130, width=200)

passLabel = Label(root, text="Password:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
passLabel.place(x=28, y=180)
passWord = Entry(root)
passWord.place(x=200, y=180, width=200)

lineLabel = Label(root, text="------------------------------------------------------------------------", width=30, anchor="e", fg='gray', justify=LEFT, font=("bold", 10))
lineLabel.place(x=150, y=210)

addressLabel = Label(root, text="Address:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
addressLabel.place(x=28, y=250)
addressField = Entry(root)
addressField.place(x=200, y=250, width=200)

cityLabel = Label(root, text="City:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
cityLabel.place(x=28, y=300)
cityField = Entry(root)
cityField.place(x=200, y=300, width=200)

stateLabel = Label(root, text="State:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
stateLabel.place(x=28, y=350)
stateField = Entry(root)
stateField.place(x=200, y=350, width=200)

noteLabel = Label(root, text="Notes:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
noteLabel.place(x=28, y=400)
noteField = Entry(root)
noteField.place(x=200, y=400, width=200)

dateLabel = Label(root, text="Date:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
dateLabel.place(x=28, y=450)
dateField = Entry(root)
dateField.place(x=200, y=450, width=200)


Button(root, text='Submit', command=lambda: (submit()), width=15, bg='brown', fg='white').place(x=50, y=525)
Button(root, text='Exit', command=lambda: (clear()), width=10, bg='brown', fg='white').place(x=200, y=525)
Button(root, text='Past Locations', command=lambda: (submittedLocations()), width=15, bg='brown', fg='white').place(x=310, y=525)

##########################################################

def clear():
    root.destroy()

def submit():

    username = userName.get()
    password = passWord.get()
    address = addressField.get()
    city = cityField.get()
    state = stateField.get()
    note = noteField.get()
    date = dateField.get()

    if(username == "" or password == "" or address == "" or city == "" or state == "" or note == "" or date == ""):
        messagebox.showerror('Error', 'All fields are required')
    else:
        data = {
            'Name': [username],
            'Password': [password],
            'Address': [address],
            'City': [city],
            'State': [state],
            'Note': [note],
            'Date': [date]
        }
        df = pd.DataFrame(data)
        df.to_csv('submissions.csv', mode='a', index=False, header=False)
        messagebox.showinfo('Submission Success', 'Your Morel location has been safely stored')
    
#The submission window to review the item submitted
def submittedLocations():

    #Pull all of the issues from the database
    f = open('submissions.csv', 'r')
    content = f.read()
    print(content)
    f.close()
    submittedIssueList = content
    d = submittedIssueList
    df = pd.read_csv('submissions.csv', sep=",")
    
    username = userName.get()
    password = passWord.get()

    df = df.loc[df['Name'] == username]
    df = df.loc[df['Password'] == password]
    df = df.drop(['Password'], axis=1)
    if len(df.index) == 0:
        messagebox.showerror("Viewing Error", "Your user name and password haven't been used to submit any locations.")
    else :
        window = tk.Tk()
        window.title("Submitted Locations")
        window.iconbitmap("mushroom.ico")
        
        #ScrollView window was chosen to accommodate how many issues are to be submitted since Indiana roads are salty garbage
        scrollViewBox = tk.Text(window, height=50, width=175)
        scroll = tk.Scrollbar(window)
        scrollViewBox.configure(yscrollcommand=scroll.set)
        scrollViewBox.pack(side=tk.LEFT)
        scroll.config(command=scrollViewBox.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scrollViewBox.insert(tk.END, df)
        scrollViewBox(df)
        
root.mainloop()



#git pull

#git add .
#git commit -m "some sort of message"
#git push