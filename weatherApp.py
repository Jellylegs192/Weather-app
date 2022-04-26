from dis import Instruction
import tkinter as tk
import requests

#Api details
API_KEY = '34aa731f6b37de5aac6d1bbd442cdb3f'
Base_URL = 'https://api.openweathermap.org/data/2.5/weather'

root = tk.Tk() #Making parent
#Building window
canvas = tk.Canvas(root, width=450, height=600)
canvas.grid(columnspan=3)
canvas.grid(rowspan=5)
canvas.configure(bg='light blue')

#Search for city
def CitySearch():
    Request_URL = f'{Base_URL}?appid={API_KEY}&q={city.get()}'
    response = requests.get(Request_URL)
    data = response.json()
    temp = data['main']['temp']
    x = (temp - 273.15) * 9/5 + 32
    farenheit = (format(x,',.2f'))
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    text_box = tk.Text(root, height=10, width= 50, padx= 15, pady = 15)
    text_box.insert(1.0,f'The Temperature is {farenheit}°')
    text_box.insert(2.0,f'\nThe humidity is {humidity}')
    text_box.insert(3.0,f'\n{description}')
    text_box.grid(columnspan = 1,column=1,row=3)
    

#Instrctions
Instructions=tk.Label(root, text='Enter City', bg='light blue',font=('Arial',20))
Instructions.grid(columnspan=1,column=1,row=0)

#input
city = tk.Entry()
city.grid(columnspan=1,column=1,row=1)

#button
search_text = tk.StringVar()
search_btn = tk.Button(root,textvariable=search_text, command=lambda:CitySearch())
search_text.set('Search')
search_btn.grid(columnspan=1, column=1, row=2)


root.mainloop()