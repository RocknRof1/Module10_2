import threading
from time import sleep

class Knight(threading.Thread):
    output_lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        total_enemies = 100
        days = 0
        with Knight.output_lock:
            print(f"{self.name}, аларм, на нас напали!")

        while total_enemies > 0:
            days += 1
            sleep(1)
            total_enemies -= self.power
            with Knight.output_lock:
                if total_enemies > 0:
                    print(f"{self.name} сражается {days} день..., осталось {total_enemies} солдат.")
                else:
                    print(f"{self.name} сражается {days} день..., осталось 0 солдат.")

        with Knight.output_lock:
            print(f"{self.name} победил спустя {days} дней!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Битва окончена!")
