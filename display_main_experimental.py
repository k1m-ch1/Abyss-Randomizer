import time
from tkinter import *
from tkinter import ttk
import abyss_randomizer_main_system
from tkinter import messagebox
from tkinter import filedialog
import os

path_dir = "C:\\Scuff abyss randomizer"
path = "C:\\Scuff abyss randomizer\\Character for input.txt"
all_char = """Nilou 

Kuki_Shinobu 

Kamisato_Ayato 

Kamisato_Ayaka 

Kaedehara_Kazuha 

Albedo 

Keqing 

Qiqi 

Jean 

Bennett 

Xingqiu 

Kaeya 

Dori 

Arataki_Itto 

Sayu 

Eula 

Xinyan 

Diluc 

Chongyun 

Noelle 

Beidou 

Razor 

Tighnari 

Collei 

Candace 

Shenhe 

Yun Jin 

Thoma 

Raiden_Shogun 

Rosaria 

Hu Tao 

Xiao 

Zhongli 

Xiangling 

Shikanoin_Heizou 

Yae Miko 

Sangonomi_Kokomi

Yelan

Gorou

Kujou_Sara

Aloy

Yoimiya

Ganyu

Tartaglia

Diona

Venti

Fischl

Amber

Cyno 

Yanfei 

Klee 

Mona 

Sucrose 

Ningguang 

Barbara 

Lisa"""

if os.path.isdir(path_dir) == False:
    os.mkdir(path_dir)

if os.path.exists(path) == False:
    with open(path,'x') as file:
        file.write(all_char)
    with open(path,'r') as file:
        character_input = file.read()
else:
    with open(path,'r') as file:
        character_input = file.read()

character_output = ""
for i in range(len(character_input)):
    if character_input[i] == " ":
        character_output = character_output + ""
    elif character_input[i] != '\n':
        character_output = character_output + character_input[i]
    elif character_input[i] == '\n':
        character_output = character_output + ','

character_formatted = list()
while character_output.count(',') != 0:
    character_formatted.append(character_output[0:character_output.find(',')])
    character_output = character_output[character_output.find(','):]
    if len(character_output) > 0:
        while character_output[0] == ',':
            character_output = character_output[1:]
            if len(character_output) == 0:
                break
if len(character_output) >0:
    character_formatted.append(character_output)

character_formatted.append("Traveler")

main_tab = Tk()
main_tab.geometry("1280x720")
main_tab.title("Abyss randomizer")
main_tab.config(bg='black')

generate_image = PhotoImage(file='roll the dice.png')
setting_image = PhotoImage(file='setting icon.png')
save_image = PhotoImage(file='save icon.png')
picture_bg = PhotoImage(file='hutao_gan.png')
info_image = PhotoImage(file='icon.png')
icon_bg = PhotoImage(file='teri_teri_nahida.png')
main_tab.iconphoto(True,icon_bg)

title = Label(main_tab,text="SCUFF ABYSS RANDOMIZER", font=("Times new roman",35),fg='pink',bg='black')
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
        main_tab_area.insert('1.0',abyss_randomizer_main_system.mode_one_random(character_formatted))

    elif select_a == False:
        try:
            main_tab_area.insert('1.0',abyss_randomizer_main_system.mode_two_random(character_formatted,int(percentage)))
        except:
            messagebox.showerror(title="EXCEPTION ACTIVATED",message="Please input a number from 1 to 100 into the settings\nInvalid input to setting, please input integers from 1 to 100 only")


def save_to_file():
    text_to_save = main_tab_area.get(1.0,END)
    filedialog.asksaveasfile(defaultextension=".txt",initialfile=f"RANDOMIZER {time.strftime('%d-%m-%Y-%H_%M_%S', time.localtime())}.txt").write(text_to_save)

def info_button_func():
    info_display = Toplevel()
    info_display.geometry("1150x700")
    info_display.config(bg='black')
    info_display_notebook = ttk.Notebook(info_display)
    tab_1 = Frame(info_display_notebook,bg='black',borderwidth=0)
    tab_2 = Frame(info_display_notebook,bg='black',borderwidth=0)
    tab_3 = Frame(info_display_notebook,bg='black',borderwidth=0)
    tab_4 = Frame(info_display_notebook,bg='black',borderwidth=0)
    info_display_notebook.add(tab_1,text="Save_instructions")
    info_display_notebook.add(tab_2, text="Settings_instructions")
    info_display_notebook.add(tab_3, text="Location of inputted Chars")
    info_display_notebook.add(tab_4, text="Custom character input")
    pg_1 = PhotoImage(file='tab_1.png')
    pg_2_part_1 = PhotoImage(file='tab_2.png')
    pg_2_part_2 = PhotoImage(file ='tab_2_part_2.png')
    pg_3 = PhotoImage(file='tab_3.png')
    pg_4_part_1 = PhotoImage(file='tab_4.png')
    pg_4_part_2 = PhotoImage(file='tab_4_part_2.png')
    pg_1_label = Label(tab_1, image=pg_1, bg='black')
    pg_1_text = Label(tab_1, text="Click save to save anywhere.\n", font=("Arial", 15), bg='black', fg='light blue')
    pg_1_label.grid(row=1,column=1)
    pg_1_text.grid(row=2,column=1)
    pg_2_label_part_1 = Label(tab_2,image=pg_2_part_1)
    pg_2_label_part_2 = Label(tab_2,image=pg_2_part_2)
    pg_2_part_1_text = Label(tab_2, text="The default setting.\nWill create 2 teams randomly.", font=("Arial", 15),bg='black', fg='light blue')
    pg_2_part_2_text = Label(tab_2, text="Enter the percentage of characters\nfrom 1 to 99\nWill encounter error if there's no input",font=("Arial", 15), bg='black', fg='light blue')
    pg_2_part_1_text.grid(row=2,column=1)
    pg_2_part_2_text.grid(row=2,column=2)
    pg_2_label_part_1.grid(row=1,column=1)
    pg_2_label_part_2.grid(row=1,column=2)
    pg_3_label = Label(tab_3,image=pg_3)
    pg_3_text = Label(tab_3,text='Go to this directory: C:\ \nYou should then see a directory named "Scuff abyss randomizer"\nIn it will contain a .txt file which contains all of the characters that will be chosen',font=("Arial", 15), bg='black', fg='light blue')
    pg_3_label.grid(row=1,column=1)
    pg_3_text.grid(row=2,column=1)
    pg_4_part_1_label = Label(tab_4,image=pg_4_part_1)
    pg_4_part_1_text = Label(tab_4,text="Crop the image\nand scan it using google lens\nselect the\ncharacters' names and\npaste it in a notepad",font=("Arial",15),fg='light blue',bg='black')
    pg_4_part_2_label = Label(tab_4,image=pg_4_part_2)
    pg_4_part_2_text = Label(tab_4,text="After you're done scanning your characters,\nYou can reformat some character's name and remove any weird shit\nMake sure that there are ONLY enters between each character's name\nThe format is like the example shown above",font=("Arial",15),bg='black',fg='light blue')
    pg_4_part_1_label.grid(row=1,column=1)
    pg_4_part_1_text.grid(row=2,column=1)
    pg_4_part_2_label.grid(row=1,column=2)
    pg_4_part_2_text.grid(row=2,column=2)

    info_display_notebook.place(x=0,y=0)
    info_display.mainloop()


generate_button = Button(main_tab, image=generate_image,borderwidth=0,command=generate_char,relief=FLAT)
setting_button = Button(main_tab, image=setting_image,borderwidth=0,command=settings_func,relief=FLAT)
save_button = Button(main_tab,image=save_image,borderwidth=0,command=save_to_file,relief=FLAT)
info_button = Button(image=info_image,compound='right',borderwidth=0,relief=FLAT,activebackground='black',bg='black',command=info_button_func)
info_button.place(x=950,y=10)
generate_button.grid(column=1,row=0)
setting_button.grid(column=3,row=0)
save_button.grid(column=2,row=0)



main_tab_area = Text(main_tab,font=("Comic Sans",15),bg='#212121',width=72,borderwidth=5,fg='pink')
main_tab_area.grid(column=0,row=1)

main_tab.mainloop()