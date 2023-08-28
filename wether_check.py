from tkinter import * 
from tkinter import ttk
import requests
def data_get():
    city= city_name.get()
    data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ed73a82b22dbd3f51205ba796adb5fdc").json()
    w_lable1.config(text = data["weather"][0]["main"])
    w1_lable2.config(text = data["weather"][0]["description"])
    temp_lable1.config(text = str(int(data["main"]["temp"]-273.15)))
    per_lable1.config(text = data["main"]["pressure"])

win = Tk()
win.title("Agro Tech")
win.config( bg = "pink")
win.geometry("500x570")
name_lable = Label(win,text="Agro Tech Weather App",
                   font =("Time New Roman",30,"bold"))
name_lable.place(x=25,y=50,height=50,width=450)
city_name = StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com =ttk.Combobox(win,text="Agro Tech Weather App",value=list_name,
                        font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)
w_lable = Label(win,text="weather climate",
                        font=("Time New Roman",15,))
w_lable.place(x=25,y=260,height=50,width=210)

w_lable1 = Label(win,text="",
                        font=("Time New Roman",15,))
w_lable1.place(x=250,y=260,height=50,width=210)


w1_lable = Label(win,text="weather Description",
                        font=("Time New Roman",15,))
w1_lable.place(x=25,y=330,height=50,width=210)

w1_lable2= Label(win,text="",
                        font=("Time New Roman",15,))
w1_lable2.place(x=250,y=330,height=50,width=210)

temp_lable = Label(win,text="Temperature",
                        font=("Time New Roman",18,))
temp_lable.place(x=25,y=400,height=50,width=210)

temp_lable1 = Label(win,text="",
                        font=("Time New Roman",18,))
temp_lable1.place(x=250,y=400,height=50,width=210)

per_lable = Label(win,text="Pressure",
                        font=("Time New Roman",15,))
per_lable.place(x=25,y=470,height=50,width=210)

per_lable1 = Label(win,text="",
                        font=("Time New Roman",15,))
per_lable1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",
                        font=("Time New Roman",15,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)
win.mainloop()