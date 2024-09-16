import pygame
from time import sleep
import sys
from datetime import datetime
from threading import Thread


class Timer:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.all_time = hours * 3600 + minutes * 60 + seconds
        self.stop=True

    def __str__(self):
        all = self.all_time
        return datetime(1990, 11, 1, hour=all // 3600, minute=all % 3600 // 60, second=all % 3600 % 60).strftime(
            '%H:%M:%S')


    # Проверка на корректность данных
    def time_correctness(self) -> bool:
        if 0 <= self.hours <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59:
            return True
        return False


    # Запуск аудио
    def ringtone(self):
        pygame.init()
        pygame.mixer.music.load('timer.mp3')
        pygame.mixer.music.play(-1)
        input()
        pygame.mixer.music.stop()
        return

    # Показ оставшегося времени
    def start(self):
        while self.all_time != 0:
            message = f'\r{self.__str__()}'
            sys.stdout.write(message)
            sys.stdout.flush()
            sleep(1)
            self.all_time -= 1


# Общее
def main():
    while True:
        print('Напишите время, на которое хотите поставить таймер, в формате 00:00:00')
        time = list(map(int, input().split(':')))
        timer = Timer(*time)

        while not timer.time_correctness():
            print('Некорректное время. Повторите попытку')
            time = list(map(int, input().split(':')))
            timer = Timer(*time)

        print('Нажмите "enter", чтобы запустить таймер')
        input()
        timer.start()
        print('\rВремя вышло')
        th = Thread(target=timer.ringtone, args=()) #Создаем поток
        th.start()
        print('Нажмите "enter", чтобы остановить таймер')
        th.join()

if __name__ == '__main__':

        main()
