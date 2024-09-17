#Libraries

from tkinter import *
import ctypes as ct
from tkinter.font import *
from PIL import Image,ImageTk

#Encrypt message
class CaesarCipher:

    def __init__(self,shift):
        self.shift = shift

    #Encrypt
    def encrypt(self,message):
        return self._encrypt_text(message, self.shift)
    
    #Decrypt with known shift
    def decrypt_with_known_shift(self,message):
        return self._encrypt_text(message,-self.shift)

    #Decrypt without known shift
    def decrypt_with_range_known_shift(self,message):
        return self.decrypt_message_without_know_shift(message,self.shift)
    

    def _encrypt_text(self,message,shift):
        encrypt_text = ""

        for char in message:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
            
                new_char = chr((ord(char)-base+shift) % 26 + base)
                encrypt_text += new_char
            else:
                encrypt_text += char
        return encrypt_text

    #Decrypt message without known shift (show all possible shifts in input range)
    def decrypt_message_without_know_shift(self,message,shift_range):
        decrypt_text=""
        shift=0
        for i in range(1,shift_range+1):
            i+=1
            shift-=1
            for char in message:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                
                    new_char = chr((ord(char)-base+shift) % 26 + base)
                    decrypt_text += new_char
                else:
                    decrypt_text += char
            decrypt_text+= " "
        return decrypt_text

#Tkinter GUI

class Window:
    
    def __init__(self,root):
        #Window settings
        self.root = root
        self.root.title("Cipher Caesar")
        self.root.resizable(False,False)
        self.root.geometry("1200x800")
        self.root.config(bg="#26242f")
        self.root.iconbitmap("icocipher.ico")

        #Dark border frame window
        self.root.update()
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(root.winfo_id())
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, 20, ct.byref(value),4)

        self.gui_start()

    #First welcome page
    def gui_start(self):
        #Clear page
        self.clear_window()
        #Welcome message
        self.Welcome_msg = Label(self.root, 
                                 text="Caesar Decoder-Encoder", 
                                 font=("Courier New",43), 
                                 bg="#26242f", 
                                 fg="white")
        
        self.Welcome_msg.place(relx=0.5,
                               rely=0.1,
                               anchor="center")
        #Logo
        self.path = Image.open("favpng_logo-font-brand-removebg-preview.png")
        self.resized_image = self.path.resize((160,160))
        self.show_logo = ImageTk.PhotoImage(self.resized_image)
        
        self.Logo = Label(self.root, 
                          image=self.show_logo)
        self.Logo.place(relx=0.5,
                        rely=0.27,
                        anchor="center")



        #Button encoder
        self.Encrypt_option = Button(self.root, 
                                     text="Encrypt Text", 
                                     font=("Courier New",30), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.gui_encrypt)
        
        self.Encrypt_option.place(relx=0.5,
                                  rely=0.45,
                                  anchor="center")
        
        #Button decoder with known shift
        self.Decrypt_shift_option = Button(self.root, 
                                     text="Decrypt message \n with known shift", 
                                     font=("Courier New",28), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.gui_decrypt_with_shift)
        
        self.Decrypt_shift_option.place(relx=0.5,
                                        rely=0.58,
                                        anchor="center")
        
        #Button decoder without known shift
        self.Decrypt_with_shift_range_option = Button(self.root, 
                                     text="Decrypt message \n with range shift", 
                                     font=("Courier New",28), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.gui_decrypt_without_shift)
        
        self.Decrypt_with_shift_range_option.place(relx=0.5,
                                                   rely=0.73,
                                                   anchor="center")

    #Encrypt page
    def gui_encrypt(self):
        #Clear page
        self.clear_window()

        # Title page
        self.encrypt_page_title = Label(self.root, 
                                 text="Encode Text", 
                                 font=("Courier New",43), 
                                 bg="#26242f", 
                                 fg="white")
        
        self.encrypt_page_title.place(relx=0.5,
                                      rely=0.1,
                                      anchor="center")
        
        #Info text
        self.info_text = Label(self.root, 
                                 text="Put your message here:", 
                                 font=("Courier New",27), 
                                 bg="#26242f", fg="white")
        
        self.info_text.place(relx=0.5,
                            rely=0.27,
                            anchor="center")
        
        #Input text
        self.input_text = Text(self.root,
                                height=6,
                                width=40, 
                                bg="#14131a",fg="white", 
                                font=("Courier New",17),
                                border=3)
        
        self.input_text.place(relx=0.5,
                              rely=0.42,
                              anchor="center")
        

        #Shift Choice
        self.shift_choice = IntVar()
        self.shift_choice = Scale(self.root, 
                                  label="Shift Choice", 
                                  from_=0, to=25, 
                                  orient=HORIZONTAL, 
                                  cursor="hand1",
                                  bg="#494659", fg="#cccccc",
                                  bd=10, 
                                  font=("Courier New",17),
                                  variable=self.shift_choice)
        
        self.shift_choice.place(relx=0.5,
                                rely=0.6,
                                relwidth=0.35,
                                anchor="center")

        #Buttons of encrypt and back to menu (first page)

        #Encrypt button
        self.encrypt_button = Button(self.root, 
                                     text="Encrypt", 
                                     font=("Courier New",16), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.encrypt)
        self.encrypt_button.place(relx=0.5,
                                  rely=0.71,
                                  anchor="center")
        
        #Back to menu button
        self.back_button = Button(self.root,
                                  text="<-",
                                  font=("Courier New",15),
                                  bg="black", fg="white",
                                  border = 5,
                                  cursor="hand1",
                                  activebackground="black",
                                  activeforeground="gray",
                                  highlightbackground="white",
                                  command=self.gui_start)
        self.back_button.place(relx=0.1,
                               rely=0.1,
                               anchor="center")

        #Result of encrypt
        self.result = Label(self.root, 
                            text="",
                            font=("Courier New",16),
                            bg="black", fg="green")
        self.result.place(relx=0.5,
                          rely=0.81,
                          anchor="center")


    #Decrypt with known shift
    def gui_decrypt_with_shift(self):
        #Clear page
        self.clear_window()

        # Title page
        self.decrypt_page_title = Label(self.root, 
                                        text="Decode Text with \n known shift", 
                                        font=("Courier New",41), 
                                        bg="#26242f", 
                                        fg="white")
        
        self.decrypt_page_title.place(relx=0.5,
                                      rely=0.1,
                                      anchor="center")
        
        #Info text
        self.info_text = Label(self.root, 
                                 text="Put your message here:", 
                                 font=("Courier New",27), 
                                 bg="#26242f", fg="white")
        
        self.info_text.place(relx=0.5,
                            rely=0.27,
                            anchor="center")
        
        #Input text
        self.input_text = Text(self.root,
                                height=6,
                                width=40, 
                                bg="#14131a",fg="white", 
                                font=("Courier New",17),
                                border=3)
        
        self.input_text.place(relx=0.5,
                              rely=0.42,
                              anchor="center")
        

        #Shift Choice
        self.shift_choice = IntVar()
        self.shift_choice = Scale(self.root, 
                                  label="Shift Choice", 
                                  from_=0, to=25, 
                                  orient=HORIZONTAL, 
                                  cursor="hand1",
                                  bg="#494659", fg="#cccccc",
                                  bd=10, 
                                  font=("Courier New",17),
                                  variable=self.shift_choice)
        
        self.shift_choice.place(relx=0.5,
                                rely=0.6,
                                relwidth=0.35,
                                anchor="center")

        #Buttons of decrypt and back to menu (first page)

        #Decrypt button
        self.decrypt_button = Button(self.root, 
                                     text="Decrypt", 
                                     font=("Courier New",16), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.decrypt_with_known_shift)
        self.decrypt_button.place(relx=0.5,
                                  rely=0.71,
                                  anchor="center")
        
        #Back to menu button
        self.back_button = Button(self.root,
                                  text="<-",
                                  font=("Courier New",15),
                                  bg="black", fg="white",
                                  border = 5,
                                  cursor="hand1",
                                  activebackground="black",
                                  activeforeground="gray",
                                  highlightbackground="white",
                                  command=self.gui_start)
        self.back_button.place(relx=0.1,
                               rely=0.1,
                               anchor="center")

        #Result of decrypt
        self.result = Label(self.root, 
                            text="",
                            font=("Courier New",16),
                            bg="black", fg="green")
        self.result.place(relx=0.5,
                          rely=0.81,
                          anchor="center")


    #Decrypt with range shift
    def gui_decrypt_without_shift(self):
        #Clear page
        self.clear_window()

        # Title page
        self.decryptw_page_title = Label(self.root, 
                                        text="Decode Text without \n known shift", 
                                        font=("Courier New",41), 
                                        bg="#26242f", 
                                        fg="white")
        
        self.decryptw_page_title.place(relx=0.5,
                                      rely=0.1,
                                      anchor="center")
        
        #Info text
        self.info_text = Label(self.root, 
                                 text="Put your message here:", 
                                 font=("Courier New",27), 
                                 bg="#26242f", fg="white")
        
        self.info_text.place(relx=0.5,
                            rely=0.27,
                            anchor="center")
        
        #Input text
        self.input_text = Text(self.root,
                                height=6,
                                width=40, 
                                bg="#14131a",fg="white", 
                                font=("Courier New",17),
                                border=3)
        
        self.input_text.place(relx=0.5,
                              rely=0.42,
                              anchor="center")
        

        #Shift Choice (in range)
        self.shift_choice = IntVar()
        self.shift_choice = Scale(self.root, 
                                  label="Shift Range Choice", 
                                  from_=0, to=25, 
                                  orient=HORIZONTAL, 
                                  cursor="hand1",
                                  bg="#494659", fg="#cccccc",
                                  bd=10, 
                                  font=("Courier New",17),
                                  variable=self.shift_choice)
        
        self.shift_choice.place(relx=0.5,
                                rely=0.6,
                                relwidth=0.35,
                                anchor="center")

        #Buttons of decrypt and back to menu (first page)

        #Decrypt button
        self.decryptw_button = Button(self.root, 
                                     text="Decrypt", 
                                     font=("Courier New",16), 
                                     bg="#26242f", fg="white", 
                                     cursor="hand2", 
                                     border=3,
                                     activebackground="black", 
                                     activeforeground="gray", 
                                     highlightbackground="white",
                                     command=self.decrypt_without_known_shift)
        self.decryptw_button.place(relx=0.5,
                                  rely=0.71,
                                  anchor="center")
        
        #Back to menu button
        self.back_button = Button(self.root,
                                  text="<-",
                                  font=("Courier New",15),
                                  bg="black", fg="white",
                                  border = 5,
                                  cursor="hand1",
                                  activebackground="black",
                                  activeforeground="gray",
                                  highlightbackground="white",
                                  command=self.gui_start)
        self.back_button.place(relx=0.1,
                               rely=0.1,
                               anchor="center")

        #Result of decrypt
        self.result = Text(self.root, 
                            font=("Courier New", 12),
                            height=10, width=50, 
                            bg="black", fg="green", wrap="word")
        self.result.place(relx=0.5,
                          rely=0.86, 
                          anchor="center")

        # Dodajemy również pasek przewijania, jeśli wyników jest dużo
        scrollbar = Scrollbar(self.root, 
                              command=self.result.yview)
        self.result.config(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.72, 
                        rely=0.86, 
                        anchor="center", 
                        height=200)



    #Clear window for pages
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #Get variables for operation of encrypt
    def encrypt(self):
        text1 = self.input_text.get("1.0", END).strip()
        shift1 = self.shift_choice.get()
        cipher1 = CaesarCipher(shift1)
        encrypt_txt = cipher1.encrypt(text1)
        self.result.config(text="Your encrypted message: {}".format(encrypt_txt))

    #Get variables for operation of decrypt with known shift
    def decrypt_with_known_shift(self):
        text2 = self.input_text.get("1.0", END).strip()
        shift2 = self.shift_choice.get()
        cipher2 = CaesarCipher(shift2)
        decrypt_txt = cipher2.decrypt_with_known_shift(text2)
        self.result.config(text="Your encrypted message: {}".format(decrypt_txt))
    
    #Get variables for operation of decrypt without known shift
    def decrypt_without_known_shift(self):
        text3 = self.input_text.get("1.0", END).strip()
        shift3 = self.shift_choice.get()
        cipher3 = CaesarCipher(shift3)
        decrypt_range_txt = cipher3.decrypt_with_range_known_shift(text3)
        self.result.delete("1.0", END)
        self.result.insert(END, decrypt_range_txt)

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
