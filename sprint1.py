import json
from tkinter import *
root = Tk()

with open('steam.json') as jsondata:
    data = json.load(jsondata)

frame1 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame1.pack(fill=BOTH, side=TOP)
frame2 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame2.pack(fill=BOTH, side=TOP)
frame3 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame3.pack(fill=BOTH, side=TOP)
frame4 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame4.pack(fill=BOTH, side=TOP)
frame5 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame5.pack(fill=BOTH, side=TOP)

def hoofdmenu():
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()
    spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
    spel_frame.pack(pady=4, padx=4, side=LEFT)
    Label(spel_frame, text="Steam spellen ", font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
    Label(spel_frame, text='Gemaakt door Tim Bolhoeve', font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)

def alle():
    root.title('Overview - Alle Spellen')

    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()

    for row in data:
        if row['appid'] < 60:
            spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 50 and row['appid'] < 230:
            spel_frame = LabelFrame(frame2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 230 and row['appid'] < 350:
            spel_frame = LabelFrame(frame3, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 350 and row['appid'] < 500:
            spel_frame = LabelFrame(frame4, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 500 and row['appid'] < 1000:
            spel_frame = LabelFrame(frame5, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 1000:
            break

def gratis():
    root.title('Overview - Gratis Spellen')

    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()

    for row in data:
        if row['appid'] < 60 and row['price'] == 0:
            spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 50 and row['appid'] < 230 and row['price'] == 0:
            spel_frame = LabelFrame(frame2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 230 and row['appid'] < 350 and row['price'] == 0:
            spel_frame = LabelFrame(frame3, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 350 and row['appid'] < 500 and row['price'] == 0:
            spel_frame = LabelFrame(frame4, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 500 and row['appid'] < 1000 and row['price'] == 0:
            spel_frame = LabelFrame(frame5, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 1000:
            break

def onder1():
    root.title('Overview - Spellen onder €1')

    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()

    for row in data:
        if row['appid'] < 60 and row['price'] < 1:
            spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 50 and row['appid'] < 230 and row['price'] < 1:
            spel_frame = LabelFrame(frame2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 230 and row['appid'] < 350 and row['price'] < 1:
            spel_frame = LabelFrame(frame3, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 350 and row['appid'] < 500 and row['price'] < 1:
            spel_frame = LabelFrame(frame4, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 500 and row['appid'] < 1000 and row['price'] < 1:
            spel_frame = LabelFrame(frame5, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 1000:
            break

def onder5():
    root.title('Overview - Spellen onder €5')
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()

    for row in data:
        if row['appid'] < 60 and row['price'] < 5:
            spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 50 and row['appid'] < 230 and row['price'] < 5:
            spel_frame = LabelFrame(frame2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 230 and row['appid'] < 350 and row['price'] < 5:
            spel_frame = LabelFrame(frame3, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 350 and row['appid'] < 500 and row['price'] < 5:
            spel_frame = LabelFrame(frame4, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 500 and row['appid'] < 1000 and row['price'] < 5:
            spel_frame = LabelFrame(frame5, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 1000:
            break

def onder10():
    root.title('Overview - Spellen onder €10')
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame5.winfo_children():
        widget.destroy()

    for row in data:
        if row['appid'] < 60 and row['price'] < 10:
            spel_frame = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 50 and row['appid'] < 230 and row['price'] < 10:
            spel_frame = LabelFrame(frame2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 230 and row['appid'] < 350 and row['price'] < 10:
            spel_frame = LabelFrame(frame3, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 350 and row['appid'] < 500 and row['price'] < 10:
            spel_frame = LabelFrame(frame4, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 500 and row['appid'] < 1000 and row['price'] < 10:
            spel_frame = LabelFrame(frame5, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        if row['appid'] > 1000:
            break

#hoofdmenu
hoofdmenu()
#einde

#navbar menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Hoofdmenu", command=hoofdmenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Alle spellen", command=alle)
editmenu.add_command(label="Gratis spellen", command=gratis)
editmenu.add_command(label="Spellen onder €1", command=onder1)
editmenu.add_command(label="Spellen onder €5", command=onder5)
editmenu.add_command(label="Spellen onder €10", command=onder10)
menubar.add_cascade(label="Filter", menu=editmenu)
#einde navbar

root.title('Overview')
root.iconbitmap('Steam.ico')
root.configure(bg='#171a21')
root.config(menu=menubar)
root.mainloop()
