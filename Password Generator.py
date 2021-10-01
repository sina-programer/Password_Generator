from tkinter import *
from tkinter import messagebox
import webbrowser
import string
import random
import os

class App:
    def __init__(self, master):
        low_level = string.ascii_lowercase + string.ascii_uppercase
        medium_level = low_level + string.digits*2
        high_level = medium_level + string.punctuation + string.ascii_uppercase
        self.levels = {
            'Low': low_level ,
            'Medium': medium_level ,
            'High': high_level            
            }

        master.config(menu=self.init_menu(master))
        
        Label(master, text='Length: ').place(x=20, y=20)
        self.lengthVar = IntVar()
        self.lengthVar.set(8)
        Spinbox(master, from_=4, to=20, width=10, textvariable=self.lengthVar).place(x=70, y=22)
        
        Label(master, text='Level: ').place(x=170, y=20)
        options = ['Low', 'Medium', 'High']
        self.levelVar = StringVar()
        self.levelVar.set('Select a level')
        OptionMenu(master, self.levelVar, *options).place(x=210, y=15)
        
        Button(master, text='Generate', width=9, command=self.generate).place(x=20, y=65)
        
        Label(master, text='Password: ').place(x=100, y=67)
        self.passwordVar = StringVar()
        Entry(master, width=20, bd=2, textvariable=self.passwordVar, state='readonly').place(x=160, y=68)
        
        Button(master, text='Copy', width=5, command=lambda: self.copy(master)).place(x=290, y=65)
        
    def generate(self):
        length = self.lengthVar.get()
        level = self.levels.get(self.levelVar.get(), False)
        
        if level:
            password = ''.join(random.sample(level, length))
            self.passwordVar.set(password)
            
        else:
            messagebox.showwarning('ERROR', 'Please select a level')

    def copy(self, master):
        password = self.passwordVar.get()
        
        if password:
            master.clipboard_clear()
            master.clipboard_append(password)
            
        else:
            messagebox.showwarning('ERROR', 'Please first generate a password')
    
    def show_about(self):
        dialog = Tk()
        dialog.title('About us')
        dialog.geometry('300x100+550+350')
        dialog.resizable(False, False)
        dialog.iconbitmap(icon)
        dialog.focus_force()
        
        print('\a')
        Label(dialog, text='This program made by Sina.f').pack(pady=12)
        
        Button(dialog, text='GitHub', width=8, command=lambda: webbrowser.open('https://github.com/sina-programer')).place(x=30, y=50)
        Button(dialog, text='Instagram', width=8, command=lambda: webbrowser.open('https://www.instagram.com/sina.programer')).place(x=120, y=50)
        Button(dialog, text='Telegram', width=8, command=lambda: webbrowser.open('https://t.me/sina_programer')).place(x=210, y=50)
        
        dialog.mainloop()

    def init_menu(self, master):
        menu = Menu(master)
        
        menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', help_msg))
        menu.add_command(label='About us', command=self.show_about)
        
        return menu
    

help_msg = '''
1_ Select a length for the password
2_ Select a level of hardness for the password
3_ Click generate button to build the password
4_ Click copy button to copy the password on clipboard
'''

icon = r'Files\icon.ico'

if __name__ == "__main__":
    root = Tk()
    root.title('Password Generator')
    root.geometry('350x110+500+300')
    root.resizable(False, False)
    
    if os.path.exists(icon):
        root.geometry('350x130+500+300')
        root.iconbitmap(icon)
        
    app = App(root)
    
    root.mainloop()
