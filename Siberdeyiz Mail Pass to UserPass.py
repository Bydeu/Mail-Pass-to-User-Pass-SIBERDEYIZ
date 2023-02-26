import tkinter as tk
from tkinter import filedialog
import re
import chardet
from collections import Counter
from colorama import init, Fore

init() # Colorama'yı başlatmak için

print(Fore.RED+"""     ██████╗██╗██████╗ ███████╗██████╗ ██████╗ ███████╗██╗   ██╗██╗███████╗
    ██╔════╝██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝██║╚════██║
    ╚█████╗ ██║██████╦╝█████╗  ██████╔╝██║  ██║█████╗   ╚████╔╝ ██║  ███╔═╝
     ╚═══██╗██║██╔══██╗██╔══╝  ██╔══██╗██║  ██║██╔══╝    ╚██╔╝  ██║██╔══╝  
    ██████╔╝██║███████╗███████╗██║  ██║██████╔╝███████╗   ██║   ██║███████╗
    ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚══════╝""")
print("Siberdeyiz Combolist Converter'a Hoş Geldiniz!")

input("Devam etmek için herhangi bir tuşa basınız.")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    f.seek(0)
    combolist = f.read().decode(encoding).splitlines()

clean_combolist = []
for combo in combolist:
    clean_combo = re.sub(r'@[A-Za-z0-9.-]+.[A-Za-z]{2,4}\b', '', combo)
    clean_combolist.append(clean_combo)

# Her bir elemanın kaç defa geçtiğini tutan bir Counter nesnesi oluşturuyoruz
combos_counter = Counter(clean_combolist)

# Sadece bir kere geçen elemanları ayırıyoruz
unique_combos = [combo for combo in clean_combolist if combos_counter[combo] == 1]

save_path = filedialog.asksaveasfilename(defaultextension=".txt")

with open(save_path, 'w', encoding=encoding) as f:
    for combo in unique_combos:
        f.write(combo + "\n")

print("İşlem Bitti.")
