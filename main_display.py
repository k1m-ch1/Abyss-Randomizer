import time
import tkinter.ttk
from tkinter import *
from tkinter import ttk
import abyss_randomizer_main_system
from tkinter import messagebox
from tkinter import filedialog

display = Tk()
display.geometry("1280x720")
display.title("Abyss randomizer")

notebook = ttk.Notebook(display)

main_tab =Frame(notebook,bg='black')
char_tab =Frame(notebook)
file_tab =Frame(notebook)

notebook.add(main_tab,text="Main")
notebook.add(char_tab,text="Characters")
notebook.add(file_tab,text="File")

notebook.grid(row=0,column=0)

generate_image = PhotoImage(file='roll the dice.png')
setting_image = PhotoImage(file='setting icon.png')
save_image = PhotoImage(file='save icon.png')
picture_bg = PhotoImage(file='hutao_gan.png')

title = Label(main_tab,text="SCUFFED ABYSS RANDOMIZER", font=("Times new roman",35),fg='pink',bg='black')
title.grid(row=0,column=0)

picture = Label(main_tab,image=picture_bg,text='\nMAY THE GOD\nOF RNG\nBE WITH YOU',
                compound='top',font=("Times new roman",20),fg='pink',bg='black')
picture.grid(row=1,column=1,columnspan=3)

select_a = True
def select_options():
    global select_a
    global slider_state
    if r.get()==0:
        select_a = True
        settings_func()
    elif r.get()==1:
        select_a = False
        settings_func()

r = IntVar()
setting_window = list()

def submit_button_func():
    global percentage
    percentage = percentage_var.get()
    settings_func()

def settings_func():
    global slider_state
    global setting_window
    global percentage_var
    if len(setting_window) > 0:
        setting_window[len(setting_window) - 1].destroy()
    setting_window.append(Toplevel(bg='black'))
    setting_window[len(setting_window)-1].geometry("960x540")
    setting_window[len(setting_window)-1].title("GENERATION SETTINGS")
    Radiobutton(setting_window[len(setting_window)-1],variable=r, text="CREATE 2 TEAMS",value=0,command=select_options,font=("Times new roman",15),bg='black',fg='pink',activebackground='black',selectcolor='black').grid(row=2,column=0,columnspan=1)
    Radiobutton(setting_window[len(setting_window)-1],variable=r, text="FILTER YOUR CHARACTERS RANDOMLY", value=1, command=select_options,font=("Times new roman",15),bg='black',fg='pink',activebackground='black',selectcolor='black').grid(row=3,column=0,columnspan=3,padx=50)
    percentage_var = Entry(setting_window[len(setting_window)-1],width=5,fg='pink',bg='black')
    percentage_var.grid(row=5,column=0)
    submit_button = Button(setting_window[len(setting_window)-1],command=submit_button_func,text="SUBMIT",font=("Times new roman",7),bg='black',fg='pink')
    submit_button.grid(row=5,column=1)
def generate_char():
    global select_a
    global percentage_var
    global percentage
    if select_a == True:
        display_area.insert('1.0',abyss_randomizer_main_system.mode_one_random(abyss_randomizer_main_system.all_characters))
    elif select_a == False:
        try:
            display_area.insert('1.0',abyss_randomizer_main_system.mode_two_random(abyss_randomizer_main_system.all_characters,int(percentage)))
        except:
            messagebox.showerror(title="EXCEPTION ACTIVATED",message="Please input a number from 1 to 100 into the settings\nInvalid input to setting, please input integers from 1 to 100 only")


def save_to_file():
    text_to_save = display_area.get(1.0,END)
    filedialog.asksaveasfile(defaultextension=".txt",initialfile=f"RANDOMIZER {time.strftime('%d-%m-%Y-%H_%M_%S', time.localtime())}.txt").write(text_to_save)

generate_button = Button(main_tab, image=generate_image,borderwidth=0,command=generate_char,relief=FLAT)
setting_button = Button(main_tab, image=setting_image,borderwidth=0,command=settings_func,relief=FLAT)
save_button = Button(main_tab,image=save_image,borderwidth=0,command=save_to_file,relief=FLAT)
generate_button.grid(column=1,row=0)
setting_button.grid(column=3,row=0)
save_button.grid(column=2,row=0)

display_area = Text(main_tab,font=("Comic Sans",15),bg='#212121',width=72,borderwidth=5,fg='pink')
display_area.grid(column=0,row=1)

display.mainloop()