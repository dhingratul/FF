import json
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

with open('ca.json') as json_data:
    Data = json.load(json_data)

def FindChoices():
    name_list=[]
    for i in Data:
        name_list.append(i['name'])
    return name_list

def FindDetails(input_name):
    for i in Data:
        if input_name==i['name']:
            county=i['county_name']
            lat=i['primary_latitude']
            longi=i['primary_longitude']
    return (county,lat,longi)

def onClick(event):
    global T1,T2,T3, var
    var.get()
    (county,lat,longi) =FindDetails(var.get())
    T1.delete("1.0",tk.END)
    T1.insert(tk.END,county)
    T2.delete("1.0",tk.END)
    T2.insert(tk.END,lat)
    T3.delete("1.0",tk.END)
    T3.insert(tk.END,longi)

#Main Program
choices=FindChoices()
root = tk.Tk()
label_1=tk.Label(root,text="City")
label_1.grid(row=0)
label_2=tk.Label(root,text="County")
label_2.grid(row=1)
label_3=tk.Label(root,text="Latitude")
label_3.grid(row=2)
label_4=tk.Label(root,text="Longitude")
label_4.grid(row=3)
#Geometry 
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("City Information")
var = tk.StringVar(root)
# initial value
var.set('Gardena')
option = tk.OptionMenu(root, var, *choices, command=onClick)
option.grid(row=0,column=1)
T1 = tk.Text(root, height=1, width=30)
T1.grid(row=1,column=1)
T2 = tk.Text(root, height=1, width=30)
T2.grid(row=2,column=1)
T3 = tk.Text(root, height=1, width=30)
T3.grid(row=3,column=1)
county,lat,longi=FindDetails(var.get())
T1.insert(tk.END,"%s" %county)
T2.insert(tk.END,"%s" %lat)
T3.insert(tk.END,"%s" %longi)
root.mainloop()







