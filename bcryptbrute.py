import threading
import bcrypt
import os

#МАМА Я ДОЛБАЁБ

class Brutebcrypt():
    def __init__(self,file):

        self.file = file
        self.password = input('Input password: ')
        self.result = []

    def bcrypt(self):
        strtobytes = bytes(self.password,'utf-8')
        with open(self.file,'r') as file:
            for line in file:
                byte_line  = line.strip().encode("utf-8")
                if bcrypt.checkpw(byte_line, strtobytes):
                    self.result.append(f"Пароль '{line.strip()}' верный!")
                else:
                    self.result.append(f"Пароль '{line.strip()}' неверный!")
        return self.result  # Возвращаем все результаты
    
    def main(self):
        threads = []
        available_threads = os.cpu_count()
        # Создаем ВСЕ ПОТОКИ чтобы наверняка
        for i in range(available_threads):
            thread = threading.Thread(target=self.bcrypt)
            threads.append(thread)
            thread.start()  # Запускаем поток

        # Ждем завершения всех потоков
        for thread in threads:
            thread.join()

