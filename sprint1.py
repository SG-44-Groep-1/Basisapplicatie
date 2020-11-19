import json
from tkinter import *
root = Tk()

with open('steam.json') as jsondata:
    data = json.load(jsondata)

def steamjsondata():
    # for i in data:
    #     if i['price'] == 0.99:
    #         print('AppID:', i['appid'], 'Naam:', i['name'], '---', 'Prijs:', i['price'])
    #dit hierboven laat alle spellen zien met bijv. prijs 0.99

    frame = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
    frame.pack(fill=BOTH)
    for row in data:
        spel_frame = LabelFrame(frame, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
        spel_frame.pack(padx=10, pady=5, side=TOP)
        Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
        Label(spel_frame, text="-------------------------------------------", bg="#2a475e", fg="#2a475e", wraplength=260, justify="left").grid(row=1)
        Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        break

steamjsondata()
root.title('Overview')
root.iconbitmap('Steam.ico')
root.configure(bg='#171a21')
root.resizable(False, False)
root.mainloop()
