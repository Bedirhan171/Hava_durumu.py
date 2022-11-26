# Kütüphanler.
# =====================================================================
import tkinter as tk
import requests
import time
import webbrowser
from PIL import Image, ImageTk

# url
# ========================================================================
url = 'https://github.com/Bedirhan171'



def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    selam = 'Bedirhan Ekinci'
    # =====================================================================

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Basınç: " + str(pressure) + "\n" + "Nem: " + str(humidity) + "\n" + "Rüzgar Hızı: " + str(wind) + "\n" + "Gün doğumu: " + sunrise + "\n" + "Gün batımı: " + sunset
    # =====================================================================
    if (city == 'konya'):
        print('KONYALI!!')
        final_info = 'KONYAlı'
        final_data = 'KONYa'
        label2.config(text = final_data)

    # dataları arayüze atıyoruz.
    # ========================================================================
    label1.config(text = final_info)
    label2.config(text = final_data)
    label3.config(text = selam)
    # ========================================================================

    
def komut():
    webbrowser.open(url)
    # Github sayfası acmak icin def.
    # ========================================================================


# dataları arayüze atıyoruz.
# ========================================================================
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.configure(background="lightblue")
canvas.title("Hava durumu tahmin")
# =====================================================================

# Font oluşturuyoz.
# ========================================================================
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# buton
# ========================================================================
resim1 = ImageTk.PhotoImage(Image.open('github_logo3.png'))
Button1 = tk.Button(canvas, image=resim1 , width=128, height=128, command=komut)
Button1.place(x=165, y=365)

label3 = tk.Label(canvas, text="github.com/Bedirhan171",fg="blue",font="Times 20 italic")
label3.place(x= 310, y = 450)

# hava durumlarını input ediyoruz.
# ========================================================================
textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

# label cıktıları.
# ========================================================================
label1 = tk.Label(canvas, font = t)
label1.pack()
label1.configure(background="lightblue")
label2 = tk.Label(canvas, font = f)
label2.pack()
label2.configure(background="lightblue")

# cansav döngüsünü bitiroyruz.
# ========================================================================
canvas.mainloop()
