import customtkinter as ctk

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def caesar():
    clear(mainframe)

    ctk.CTkLabel(mainframe, text="Caesar Chiper", font=ctk.CTkFont(weight="bold", size=18)).place(x=250, y=100)
    
    ctk.CTkLabel(mainframe, text="Plain Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=150)
    plaintext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Plain Text")
    plaintext.place(x=200, y=150)

    ctk.CTkLabel(mainframe, text="Key", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=200)
    keytext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Key")
    keytext.place(x=200, y=200)

    ctk.CTkLabel(mainframe, text="Chiper Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=300)
    chipertextoutput = ctk.CTkEntry(mainframe, width=300)
    chipertextoutput.place(x=200, y=300)

    def show_text():
        plain = plaintext.get()
        key = keytext.get()
        chipertext = []

        try:
            shift = int(key)
        except ValueError:
            chipertextoutput.configure(text_color="red", state="normal")
            chipertextoutput.delete(0, "end")
            chipertextoutput.insert(0, "[ERROR] Please input a valid number")
            chipertextoutput.configure(state="readonly")
            return

        if not 1 <= shift <= 26:
            chipertextoutput.configure(text_color="red", state="normal")
            chipertextoutput.delete(0, "end")
            chipertextoutput.insert(0, "[ERROR] Please input number from 1 to 26")
            chipertextoutput.configure(state="readonly")
            return

        for i in plain:
            if 65 <= ord(i) <= 90: 
                chipertext.append(chr(((ord(i) - 65 + shift) % 26) + 65))
            elif 97 <= ord(i) <= 122:  
                chipertext.append(chr(((ord(i) - 97 + shift) % 26) + 97))
            else:
                chipertext.append(i)

        chipertextoutput.configure(text_color="white", state="normal")
        chipertextoutput.delete(0, "end")
        chipertextoutput.insert(0, ''.join(chipertext))
        chipertextoutput.configure(state="readonly")

    ctk.CTkButton(mainframe, text="Decode", font=ctk.CTkFont(weight="bold"), command=show_text).place(x=355, y=250)



def atbash():
    clear(mainframe)
    
    ctk.CTkLabel(mainframe, text="Atbash Cipher", font=ctk.CTkFont(weight="bold", size=18)).place(x=250, y=100)

    ctk.CTkLabel(mainframe, text="Plain Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=150)
    plaintext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Plain Text")
    plaintext.place(x=200, y=150)

    ctk.CTkLabel(mainframe, text="Cipher Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=250)
    chipertextoutput = ctk.CTkEntry(mainframe, width=300)
    chipertextoutput.place(x=200, y=250)

    def show_text():
        plain = plaintext.get()
        atbash_result = []

        if not plain.isalpha():
            chipertextoutput.configure(text_color="red", state="normal") 
            chipertextoutput.place(x=200, y=250)
            chipertextoutput.delete(0, "end")
            chipertextoutput.insert(0, "[ERROR] Please input words only")
            return

        for i in plain:
            if 'A' <= i <= 'Z':
                atbash_result.append(chr(90 - (ord(i) - 65)))
            elif 'a' <= i <= 'z':
                atbash_result.append(chr(122 - (ord(i) - 97)))

        chipertextoutput.configure(text_color ="white",state="normal")
        chipertextoutput.delete(0, "end")
        chipertextoutput.insert(0, ''.join(atbash_result))
        chipertextoutput.configure(state="readonly")

    ctk.CTkButton(mainframe, text="Decode", font=ctk.CTkFont(weight="bold"), command=show_text).place(x=355, y=200)


def subtitution():
    clear(mainframe)

    ctk.CTkLabel(mainframe, text="Substitution Cipher", font=ctk.CTkFont(weight="bold", size=18)).place(x=250, y=100)
    
    ctk.CTkLabel(mainframe, text="Plain Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=150)
    plaintext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Plain Text")
    plaintext.place(x=200, y=150)

    ctk.CTkLabel(mainframe, text="Key", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=200)
    keytext = ctk.CTkEntry(mainframe, width=300, placeholder_text="Key")
    keytext.place(x=200, y=200)

    ctk.CTkLabel(mainframe, text="Cipher Text", font=ctk.CTkFont(weight="bold", size=12)).place(x=100, y=300)
    chipertextoutput = ctk.CTkEntry(mainframe, width=300)
    chipertextoutput.place(x=200, y=300)

    def show_text(mode):
        plain = plaintext.get()
        key = keytext.get()

        if not plain.isalpha():
            plaintext.configure(text_color="red", state="normal") 
            plaintext.delete(0, "end")
            plaintext.insert(0, "[ERROR] Please input alphabet text")
            return
        else:
            plaintext.configure(text_color="white", state="normal")
            plain = plain.lower()

        if len(key) != 26 or not key.isalpha():
            keytext.configure(text_color="red", state="normal") 
            keytext.delete(0, "end")
            keytext.insert(0, "[ERROR] Please input 26 alphabet letters")
            return
        else:
            keytext.configure(text_color="white", state="normal")
            key = key.lower()

        alphabetlower = list("abcdefghijklmnopqrstuvwxyz")
        keylist = list(key)
        mapping_lower_case_encode = {alphabetlower[i]: keylist[i] for i in range(26)}
        mapping_lower_case_decode = {keylist[i]: alphabetlower[i]  for i in range(26)}
        substitute = ""
        if mode == "encode":
            for char in plain:
                substitute += mapping_lower_case_encode.get(char, char)
        elif mode == "decode":
            for char in plain:
                substitute += mapping_lower_case_decode.get(char, char)

        chipertextoutput.configure(text_color="white", state="normal")
        chipertextoutput.delete(0, "end")
        chipertextoutput.insert(0, substitute)
        chipertextoutput.configure(state="readonly")

    ctk.CTkButton(mainframe, text="Encode", font=ctk.CTkFont(weight="bold"), command=lambda: show_text("encode")).place(x=200, y=250)
    ctk.CTkButton(mainframe, text="Decode", font=ctk.CTkFont(weight="bold"), command=lambda: show_text("decode")).place(x=355, y=250)

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
atbash = ctk.CTkButton(sidebar,
                     text="Atbash",
                     fg_color="#303030",
                     hover_color="#454545",
                     font= ctk.CTkFont(size= 12, weight="bold"),
                     corner_radius=0,
                     anchor="center",
                     height=40,
                     command=atbash)
atbash.pack()

subtitution = ctk.CTkButton(sidebar,
                     text="Subtitution",
                     fg_color="#303030",
                     hover_color="#454545",
                     font= ctk.CTkFont(size= 12, weight="bold"),
                     corner_radius=0,
                     anchor="center",
                     height=40,
                     command=subtitution)
subtitution.pack()



app.mainloop()