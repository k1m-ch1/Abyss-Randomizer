import random
import time
all_characters = ["Dori","Collei","Shikanoin","Yun_Jin","Gorou","Thoma",
                  "KujouSara","Aloy","Sayu","Kaedehara","Yanfei","Rosaria",
                  "Hu_Tao","Xiao","Zhongli","Xinyan","Tartaglia","Diona","Keqing",
                  "Qiqi","Diluc","Jean","Sucrose","Chongyun","Noelle","Bennett","Fischl",
                  "Ningguang","Xingqiu","Beidou","Xiangling","Razor","Barbara","Lisa",
                  "Kaeya","Amber"]

def mode_one_random(characters):
    """To create two teams.\n
    first argument is characters uses list\n
    returns a string"""
    chosen_characters = set()
    while len(chosen_characters) < 8:
        chosen_characters.add(random.choice(characters))
    chosen_characters = list(chosen_characters)
    return "2 TEAMS GENERATED: \n"\
        f"TEAM 1: {chosen_characters[0]}, {chosen_characters[1]}, {chosen_characters[2]}, {chosen_characters[3]}\n" \
           f"TEAM 2: {chosen_characters[4]}, {chosen_characters[5]}, {chosen_characters[6]}, {chosen_characters[7]}\nGenerated on {time.asctime()}\n\n"

def mode_two_random(characters,percentage):
    """To create a series of characters. \n
    first argument is characters uses list, \n
    second argument is percentage uses 0 to 100 \n
    returns a string"""
    chosen_characters = set()
    formatted_output = "FILTERED {}% OF ALL CHARACTERS\n\n".format(percentage)
    a = 0
    while len(chosen_characters) < len(characters)*(percentage/100):
        chosen_characters.add(random.choice(characters))
    chosen_characters = list(chosen_characters)
    for i in range(len(chosen_characters)-1):
        a = a + 1
        formatted_output = formatted_output + str(chosen_characters[i]) + ", "
        if a % 7 == 0.0:
            formatted_output = formatted_output + "\n"
    formatted_output = formatted_output + chosen_characters[len(chosen_characters)-1] + "\n\n" + f"A TOTAL OF {len(chosen_characters)} CHARACTERS SELECTED"\
    f"\nGenerated on {time.asctime()}\n\n\n"
    return formatted_output

