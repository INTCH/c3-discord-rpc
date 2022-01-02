from pypresence import Presence
import time
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Construct 3 Discord RPC")
proje = input("Proje Adı: ")
os.system("cls")
print("Presence Başlatılıyor...")

def presence():
        rpc = Presence('APP ID') 
        rpc.connect()
        os.system("cls")
        print("Presence Başlatıldı!")
        ctypes.windll.kernel32.SetConsoleTitleW("Construct 3 - Working on "+proje)
        start_time = int(time.time())
        while True: 
            rpc.update(details="Working on "+proje, large_image="c3_logo", start=start_time)
            time.sleep(15)

presence()