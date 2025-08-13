import customtkinter as ctk

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def caesar():
    clear(mainframe)

    plaintextlabel = ctk.CTkLabel(mainframe, text="Plain Text", font=ctk.CTkFont(weight="bold",size=12))
    plaintextlabel.place(x=100, y=100)
    plaintext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Plain Text")
    plaintext.place(x=200, y=100)

    keytextlabel = ctk.CTkLabel(mainframe, text="Key", font=ctk.CTkFont(weight="bold",size=12))
    keytextlabel.place(x=100, y=150)
    keytext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Key")
    keytext.place(x=200, y=150)

    chipertextlabel = ctk.CTkLabel(mainframe, text="Chiper Text", font=ctk.CTkFont(weight="bold",size=12))
    chipertextlabel.place(x=100, y=250)
    chipertextoutput = ctk.CTkEntry(mainframe, width=300)
    chipertextoutput.place(x=200, y=250)
    
    def show_text():
     plain = plaintext.get()
     key = keytext.get()
     chipertext = []

     try:
        shift = int(key)
     except ValueError:
        chipertextoutput = ctk.CTkEntry(mainframe, width=300, text_color="red")
        chipertextoutput.place(x=200, y=250)
        chipertextoutput.insert(0, "[ERROR] Please input a valid number")
        chipertextoutput.configure(state="readonly")
        return

     if 1 <= shift <= 26:
        for i in plain:
            if 65 <= ord(i) <= 90:  
                chipertext.append(chr(((ord(i) - 65 + shift) % 26) + 65))
            elif 97 <= ord(i) <= 122:  
                chipertext.append(chr(((ord(i) - 97 + shift) % 26) + 97))
            else:
                chipertext.append(i)  
        chipertextoutput = ctk.CTkEntry(mainframe, width=300)
        chipertextoutput.place(x=200, y=250)
        chipertextoutput.insert(0, ''.join(chipertext))
        chipertextoutput.configure(state="readonly")
     else:
        chipertextoutput = ctk.CTkEntry(mainframe, width=300, text_color="red")
        chipertextoutput.place(x=200, y=250)
        chipertextoutput.insert(0, "[ERROR] Please input a number from 1 to 26")
        chipertextoutput.configure(state="readonly")

    chipertextoutput = ctk.CTkEntry(mainframe, width=300)
    chipertextoutput.place(x=200, y=250)

    button = ctk.CTkButton(mainframe, text="Decode", command=show_text)
    button.place(x=355, y=200)

def vigenere():
    clear(mainframe)
    ctk.CTkLabel(mainframe, text="Ini halaman Vigenere", font=("Arial", 16)).pack(pady=20)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("800x500")
app.title("ClassicChiper")
app.resizable(False,False)

sidebar = ctk.CTkFrame(app, width= 200, corner_radius=0, fg_color="#303030")
sidebar.pack(side="left" ,fill ="y")

mainframe = ctk.CTkFrame(app,width= 700, height=500, corner_radius=0, fg_color="#202020")
mainframe.pack(fill ="y")

logo_label = ctk.CTkLabel(sidebar, text="CC", font=ctk.CTkFont(size=30, weight="bold"))
logo_label.pack(pady=(20, 20))

caesar = ctk.CTkButton(sidebar,
                     text="Caesar",
                     fg_color="#303030",
                     hover_color="#454545",
                     font= ctk.CTkFont(size= 12, weight="bold"),
                     corner_radius=0,
                     anchor="center",
                     height=40,
                     command=caesar)
caesar.pack()
vigenere = ctk.CTkButton(sidebar,
                     text="Vigenere",
                     fg_color="#303030",
                     hover_color="#454545",
                     font= ctk.CTkFont(size= 12, weight="bold"),
                     corner_radius=0,
                     anchor="center",
                     height=40,
                     command=vigenere)
vigenere.pack()



app.mainloop()