from Placement_update import *
import json
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

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
frame3 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame3.pack(fill=BOTH, side=TOP)
frame4 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame4.pack(fill=BOTH, side=TOP)
frame5 = LabelFrame(padx=5, pady=5, width=250, height=80, bg="#171a21", highlightthickness=0, borderwidth=0)
frame5.pack(fill=BOTH, side=TOP)

def hoofdmenu():
    destroy_frames()
    zoekbalk()

    author_info = LabelFrame(frame1, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
    author_info.pack(pady=40, padx=4, side=LEFT)
    Label(author_info, text="Steam spellen ", font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e").grid(row=0, column=0, pady=2, padx=2, sticky=W)
    Label(author_info, text='Gemaakt door Tim Bolhoeve', font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
    Label(author_info, text='Geüpdatet door Jasper van der Post', font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)

def zoekbalk():
    Label(frame0, text="Zoeken: ", font=("Century Gothic", 10), fg='#c7d5e0', bg="#171a21").grid(row=0, column=0, pady=2, padx=2, sticky=W)
    balk = Entry(frame0, width=25, bg='#2a475e', fg='grey')
    balk.grid(row=0, column=1, pady=2, sticky=W)
    Button(frame0, text="Zoeken", image=foto, bg='#2a475e', activebackground='#66c0f4', bd=1, relief=GROOVE, command=lambda: search(frame1, balk)).grid(row=0, column=2, pady=2, sticky=W)
    balk.bind("<FocusIn>", lambda event: foc_in(event, balk))
    balk.bind("<FocusOut>", lambda event: foc_out(event, balk))
    balk.bind("<Return>", lambda event: search(frame1, balk))
    balk.insert(0, "Zoeken...")

def foc_in(event, balk):
    balk.delete(0, END)
    balk.configure(fg='#c7d5e0')

def foc_out(event, balk):
    balk.config({"foreground": 'grey'})
    balk.delete(0, END)
    balk.insert(0, "Zoeken...")

def search(master, entry):
    for widget in frame1.winfo_children():
        widget.destroy()
    naam_spel = entry.get()

    teller = 0
    search_results = []

    for row in data:
        if naam_spel.lower() in row['name'].lower() and teller < 5:
            search_results.append(row)
            teller += 1

    sorted_lst = sort(search_results)
    for row in sorted_lst:
        spel_frame = LabelFrame(master, bg="#2a475e", padx=5, pady=5, width=250, height=80, highlightthickness=0, borderwidth=0)
        spel_frame.pack(pady=4, padx=4, side=LEFT)
        Label(spel_frame, text="Naam: " + str(row['name']), font=("Century Gothic", 12, 'bold'), fg='#c7d5e0', bg="#2a475e", wraplength=400).grid(row=0, column=0, pady=2, padx=2, sticky=W)
        Label(spel_frame, text="--------------------------------------------------------------", bg="#2a475e", fg="#2a475e", justify="left").grid(row=1)
        Label(spel_frame, text='Prijs: €' + str(row['price']), font=("Arial", 8), bg="#2a475e", fg="#66c0f4").grid(row=1, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Positieve Reviews: ' + str(row['positive_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=2, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Negatieve Reviews: ' + str(row['negative_ratings']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=3, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Release Date: ' + str(row['release_date']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=4, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Developer: ' + str(row['developer']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Publisher: ' + str(row['publisher']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
        Label(spel_frame, text='Tags: ' + str(row['steamspy_tags']), bg="#2a475e", font=("Arial", 8), fg="#66c0f4").grid(row=5, column=0, pady=4, padx=5, sticky=W)
    if frame1.winfo_children() == []:
        showerror("No match found", message="Er zijn geen zoekresultaten gevonden. Controleer uw spelling en probeer het opnieuw.")

def destroy_frames():
    for widget in frame0.winfo_children():
        widget.destroy()
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

def alle():
    root.title('Overview - Alle Spellen')
    destroy_frames()
    place_alle(frame1, frame2, frame3, frame4, frame5)

def gratis():
    root.title('Overview - Gratis Spellen')
    destroy_frames()

    place_gratis(frame1, frame2, frame3, frame4, frame5)

def onder1():
    root.title('Overview - Spellen onder €1')
    destroy_frames()

    place_onder1(frame1, frame2, frame3, frame4, frame5)

def onder5():
    root.title('Overview - Spellen onder €5')
    destroy_frames()

    place_onder5(frame1, frame2, frame3, frame4, frame5)

def onder10():
    root.title('Overview - Spellen onder €10')
    destroy_frames()
    place_onder10(frame1, frame2, frame3, frame4, frame5)

#hoofdmenu
hoofdmenu()
zoekbalk()
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
