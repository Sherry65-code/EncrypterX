from os import system,name
from sys import exit
if name == "nt":
    print("This installer is not avaliable for windows. Coming to you soon.")
    exit(1)
system("echo \"$(pwd)\" > cwd.txt")
f = open("cwd.txt", "r")
fdata = f.read().strip()
f.close()
f = open("binary.c", "w")
f.write(f"""#include <stdlib.h>

int main() {
	system("python3 {fdata}/main.py");
}
""")
f.close()
system("cc binary.c -o encx")
print("Now follow the instruction given on our official Webpage")
exit(0)
