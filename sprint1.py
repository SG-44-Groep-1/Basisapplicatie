from Placement import *
import json
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk
import requests

root = Tk()

with open('steam.json') as jsondata:
    data = json.load(jsondata)

foto = PhotoImage(file="vgglas.png")
frame0 = LabelFrame(padx=5, pady=5, width=250, height=30, bg="#171a21", highlightthickness=0, borderwidth=0)
frame0.pack(fill=BOTH, side=TOP)
frame1 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame1.pack(fill=BOTH, side=TOP)
frame2 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame2.pack(fill=BOTH, side=TOP)

def zoekbalk():
    Label(frame0, text="Zoeken: ", font=("Century Gothic", 10), fg='#c7d5e0', bg="#171a21").grid(row=0, column=0, pady=2, padx=2, sticky=W)
    balk = Entry(frame0, width=25, bg='#2a475e', fg='grey')
    balk.grid(row=0, column=1, pady=2, sticky=W)
    Button(frame0, text="Zoeken", image=foto, bg='#2a475e', activebackground='#66c0f4', bd=1, relief=GROOVE, command=lambda: search(frame1, frame2, balk)).grid(row=0, column=2, pady=2, sticky=W)
    balk.bind("<FocusIn>", lambda event: foc_in(event, balk))
    balk.bind("<FocusOut>", lambda event: foc_out(event, balk))
    balk.bind("<Return>", lambda event: search(frame1, frame2, balk))
    balk.insert(0, "Zoeken...")

def foc_in(event, balk):
    balk.delete(0, END)
    balk.configure(fg='#c7d5e0')

def foc_out(event, balk):
    balk.config({"foreground": 'grey'})
    balk.delete(0, END)
    balk.insert(0, "Zoeken...")

def search(master, master2, entry):
    root.geometry('1781x550+70+200')
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    naam_spel = entry.get()


    teller = 0
    for row in data:
        if naam_spel.lower() in row['name'].lower() and teller < 5:
            spel_frame = LabelFrame(master, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
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
        if naam_spel.lower() in row['name'].lower() and 5 <= teller < 10:
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
    if frame1.winfo_children() == []:
        showerror("No match found", message="Er zijn geen zoekresultaten gevonden. Controleer uw spelling en probeer het opnieuw.")
    else:
        root.geometry('+100+200')
        root.title(f'Overview - {naam_spel}')

def destroy_frames():
    for widget in frame0.winfo_children():
        widget.destroy()
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()

def alle():
    root.title('Overview - Top 10 games')
    root.geometry('1781x550+70+200')
    destroy_frames()
    place_alle(frame1, frame2)
    zoekbalk()

def gratis():
    root.title('Overview - Top 10 free games')
    root.geometry('1781x550+70+200')
    destroy_frames()
    place_gratis(frame1, frame2)
    zoekbalk()

def onder1():
    root.title('Overview - Top 10 games under €1')
    root.geometry('1781x550+70+200')
    destroy_frames()
    place_onder1(frame1, frame2)
    zoekbalk()

def onder5():
    root.title('Overview - Top 10 games under €5')
    root.geometry('1781x550+70+200')
    destroy_frames()
    place_onder5(frame1, frame2)
    zoekbalk()

def onder10():
    root.title('Overview - Top 10 games under €10')
    root.geometry('1781x550+70+200')
    destroy_frames()
    place_onder10(frame1, frame2)
    zoekbalk()

lst = []

def tabel():

    def stati():
        listBox.delete(*listBox.get_children())
        global lst
        api = requests.get(f'https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=730&format=json')
        if api.status_code == 200:
            steam = api.json()
            for items in steam['achievementpercentages']['achievements']:
                lst.append(items)
                achiev = items['name']
                proc = items['percent']

                tempList = [[achiev, f'{proc}%']]

                for i, (achievement, procent) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(achievement, procent))

    def laaghoog():
        listBox.delete(*listBox.get_children())
        global lst
        lst_sort = []

        def sort(lst):
            if len(lst) <= 0:
                return lst
            min = {'percent': 1000}

            for i in lst:
                if i['percent'] <= min['percent']:
                    min = i
            lst_sort.append(min)
            lst.pop(lst.index(i))
            return sort(lst)
        sort(lst)
        for items in lst_sort:
            achiev = items['name']
            proc = items['percent']

            tempList = [[achiev, f'{proc}%']]

            for i, (achievement, procent) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(achievement, procent))

    statistiek = Toplevel(root)
    statistiek.geometry("500x600")
    statistiek.title("Overview - Statistieken - Counter-Strike: Global Offensive")

    cols = ('Achievement', 'Players with this achievement')
    listBox = ttk.Treeview(statistiek, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.pack(expand=TRUE, fill=BOTH)

    b2 = Button(statistiek, text="Hoog-Laag", command=stati)
    c2 = Button(statistiek, text="Laag-Hoog", command=laaghoog)
    b2.pack(side=LEFT, fill=X, expand=True)
    c2.pack(side=LEFT, fill=X, expand=True)

    stati()

#hoofdmenu
alle()
zoekbalk()
#einde

#navbar menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Top 10 games", command=alle)
editmenu.add_command(label="Top 10 free games", command=gratis)
editmenu.add_command(label="Top 10 games under €1", command=onder1)
editmenu.add_command(label="Top 10 games under €5", command=onder5)
editmenu.add_command(label="Top 10 games under €10", command=onder10)
menubar.add_cascade(label="Filter", menu=editmenu)

statisticmenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Statistieken", command=tabel)
#einde navbar

root.title('Overview')
root.iconbitmap('Steam.ico')
root.configure(bg='#171a21')
root.config(menu=menubar)
root.mainloop()
