import threading
import hashlib
import os

#МАМА СМОТРИ Я ПИЗДАНУТЫЙ

class Brutemd5():
    
    def __init__(self,file):

        self.file = file
        self.password = input('Input password: ')
        self.result = []

    def md5(self):
        md5_hash = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        with open(self.file,'r') as file:
            for line in file:
                byte_line  = line.strip().encode("utf-8")
        # Сравниваем с хешем из файла
                if byte_line.decode('utf-8') == md5_hash:
                    self.result.append( f"Пароль '{byte_line.decode()}' верный!")
                    break
        return self.result 

 
     
    def main(self):
        threads = []
        available_threads = os.cpu_count()
        # Создаем ВСЕ ПОТОКИ чтобы наверняка
        for i in range(available_threads):
            thread = threading.Thread(target=self.md5)
            threads.append(thread)
            thread.start()  # Запускаем поток

        # Ждем завершения всех потоков
        for thread in threads:
            thread.join()