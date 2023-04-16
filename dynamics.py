from os import get_terminal_size, system, name

def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def printEquals(textlen):
    try:
        textlen = int(textlen)
    except Exception as e:
        return -1
    totalwidth = get_terminal_size().columns-textlen
    totalwidth = totalwidth/2
    if (totalwidth*2)+textlen >= get_terminal_size().columns:
        totalwidth-=1
        print(end=" ")
    eq = ""
    x = 0
    while x<totalwidth:
        eq+=" "
        x+=1
    print(eq, end="")
    return 0

if __name__ == "__main__":
    print("Run Encrypter from main.py")
