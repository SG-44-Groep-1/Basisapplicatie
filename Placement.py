from tkinter import *
import json

with open('steam.json') as jsondata:
    data = json.load(jsondata)

def place_alle(master1, master2):
    teller = 0
    for row in data:
        if teller < 5:
            spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
        if 5 <= teller < 10:
            spel_frame = LabelFrame(master2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1

def place_gratis(master1, master2):
    teller = 0
    for row in data:
        if teller < 5 and row['price'] == 0:
            spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
        if 5 <= teller < 10 and row['price'] == 0:
            spel_frame = LabelFrame(master2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1

def place_onder1(master1, master2):
    teller = 0
    for row in data:
        if teller < 5 and 0 < row['price'] < 1:
            spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
        if 5 <= teller < 10 and 0 < row['price'] < 1:
            spel_frame = LabelFrame(master2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
def place_onder5(master1, master2):
    teller = 0
    for row in data:
        if teller < 5 and 1 < row['price'] < 5:
            spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
        if 5 <= teller < 10 and 1 < row['price'] < 5:
            spel_frame = LabelFrame(master2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1

def place_onder10(master1, master2):
    teller = 0
    for row in data:
        if teller < 5 and 5 < row['price'] < 10:
            spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1
        if 5 <= teller < 10 and 5 < row['price'] < 10:
            spel_frame = LabelFrame(master2, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
            spel_frame.pack(pady=4, padx=4, side=LEFT)
            Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
            Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
            Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
            Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=6, column=0, pady=4, padx=5, sticky=W)
            tagframe = Frame(spel_frame, bg="#2a475e", highlightthickness=0, borderwidth=0)
            tagframe.grid(row=7, column=0, pady=2, padx=2, sticky=W)
            tagknop = row['steamspy_tags'].split(';')
            column = 1
            Label(tagframe, text='Tags: ', bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=7, column=0, padx=5, sticky=E)
            for tag in tagknop:
                knoppie = Button(tagframe, text=tag, cursor="hand2", borderwidth=0, highlightthickness=0, bg="#223c4b", activebackground="#67c1f5", fg="#67c1f5")
                knoppie.grid(row=7, column=column, padx=2, sticky=E)
                column += 1
            teller += 1

# def sort(search_list):
#     sorted_lst = []
#     maximum = -800000000000
#
#     while 1:
#         for i in search_list:
#             if i['positive_ratings'] > maximum:
#                 maximum = i['positive_ratings']               #dit was eenmalig voor het soorteren van de steam.json
#         for i in search_list:
#             if i['positive_ratings'] == maximum:
#                 search_list.pop(search_list.index(i))
#                 sorted_lst.append(i)
#         maximum = -800000000000
#         if len(search_list) == 0:
#             break
#     return sorted_lst
