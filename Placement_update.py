from tkinter import *
import json

with open('steam.json') as jsondata:
    data = json.load(jsondata)

def sort(search_list):
    sorted_lst = []
    maximum = -800000000000

    while 1:
        for i in search_list:
            if i['positive_ratings'] > maximum:
                maximum = i['positive_ratings']
        for i in search_list:
            if i['positive_ratings'] == maximum:
                search_list.pop(search_list.index(i))
                sorted_lst.append(i)
        maximum = -800000000000
        if len(search_list) == 0:
            break
    return sorted_lst

def place_alle(master1, master2, master3, master4, master5):
    teller = 0
    search_results = []

    for row in data:
        if teller < 5:
            search_results.append(row)
            teller += 1
    sorted_lst = sort(search_results)

    for row in sorted_lst:
        spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
        spel_frame.pack(pady=4, padx=4, side=LEFT)
        Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
        Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
        Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid( row=1, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)


def place_gratis(master1, master2, master3, master4, master5):
    teller = 0
    search_results = []

    for row in data:
        if teller < 5 and row['price'] == 0:
            search_results.append(row)
            teller += 1
    sorted_lst = sort(search_results)

    for row in sorted_lst:
        spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
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

def place_onder1(master1, master2, master3, master4, master5):
    teller = 0
    search_results = []

    for row in data:
        if teller < 5 and 0 < row['price'] < 1:
            search_results.append(row)
            teller += 1
    sorted_lst = sort(search_results)

    for row in sorted_lst:
        spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
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

def place_onder5(master1, master2, master3, master4, master5):
    teller = 0
    search_results = []

    for row in data:
        if teller < 5 and row['price'] > 1 and row['price'] < 5:
            search_results.append(row)
            teller += 1
    sorted_lst = sort(search_results)

    for row in sorted_lst:
        spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
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

def place_onder10(master1, master2, master3, master4, master5):
    teller = 0
    search_results = []

    for row in data:
        if teller < 5 and 5 < row['price'] < 10:
            search_results.append(row)
            teller += 1
    sorted_lst = sort(search_results)

    for row in sorted_lst:
        spel_frame = LabelFrame(master1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
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
