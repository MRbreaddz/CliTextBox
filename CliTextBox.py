themes_list = {
    "1":"═╔╗╚╝║",
    "2":"-****/",
    "3":"─┌┐└┘│",
    "4":"─╓╖╙╜║",
    "5":"█▄▄▀▀█",
    "6":"►●●●●▼",
    "7":"■■■■■■",
    "8":"□□□□□□",
    }
def show_text(text,theme):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = themes_list[theme][0] * (max_length + 4)
    
    print(themes_list[theme][1] + border + themes_list[theme][2])
    for line in lines:
        print(themes_list[theme][5] + line.ljust(max_length) + "    "+themes_list[theme][5])
    print(themes_list[theme][5] + " " * max_length + "    "+themes_list[theme][5])
    print(themes_list[theme][3] + border + themes_list[theme][4])
   
if __name__ == "__main__":
    show_text("""simple text inside a box
hello world!""","1")
    show_text("""simple text inside a box
hello world!""","2")
    show_text("""simple text inside a box
hello world!""","3")
    show_text("""simple text inside a box
hello world!""","4")
    show_text("""simple text inside a box
hello world!""","5")
    show_text("""simple text inside a box
hello world!""","6")
    show_text("""simple text inside a box
hello world!""","7")
    show_text("""simple text inside a box
hello world!""","8")
