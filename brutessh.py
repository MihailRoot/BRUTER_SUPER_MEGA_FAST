import os

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
