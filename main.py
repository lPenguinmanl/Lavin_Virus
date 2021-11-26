from multiprocessing import Pool
import os
import pyAesCrypt
from stegano import exifHeader
import multiprocessing 
#----------------------------------------------------- шифрование файлов
#password = input('Enter key: ') # Вводим ключ шифрования
#bufferSize = 512*1024 #Размер буфера 512 килобайт, не нужно его делать очень большим
#pyAesCrypt.encryptFile("C:\\Users\\User\\Desktop\\прога\\test\\123.docx","C:\\Users\\User\\Desktop\\прога\\test\\123.docx"+".aes",password, bufferSize) # Собственно сама функция шифрования, создаст зашифрованный файл с расширение .aes
#print('[Crypted] '+str(dir)+'.aes')
#-----------------------------------------------------
"""
обход по файлам
login = os.getlogin()
for addreses, dirs, files in os.walk("."):
    for file in files:
        print(os.path.abspath(file))
#print(login)
"""
#secret = exifHeader.hide('wallpaper.jpg','WAIIPAPER.jpg', "testing...")

'''
res = exifHeader.reveal("images1.jpeg")
res = res.decode()
print(res)
'''

'''lock = exifHeader.reveal('mountain.jpg').decode()
buff = 512*1024
pyAesCrypt.encryptFile('mountain.jpg', 'mountain.jpg.lol',lock, buff)
os.remove('mountain.jpg')
'''
'''
passw = 'testing'
buff = 512*1024
pyAesCrypt.decryptFile('mountain.jpg.aes', 'mountain.jpg', passw, buff)
os.remove('mountain.jpg.aes')
'''
def print_6(num):
    f = open(f'text{num}', 'w+')
    f.write(num)
    f.close()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    with multiprocessing.Pool(6) as p:
        p.map(print_6, [str(1), str(2), str(3), str(4), str(5), str(6)])