import os
import pyAesCrypt
from stegano import exifHeader
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
#secret = exifHeader.hide('images.jpeg','images1.jpeg', "testing...")

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
 
passw = 'testing'
buff = 512*1024
pyAesCrypt.decryptFile('mountain.jpg.aes', 'mountain.jpg', passw, buff)
os.remove('mountain.jpg.aes')