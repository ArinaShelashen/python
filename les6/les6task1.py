from time import sleep


class TrafficLight:

    __color = "Red"

    def running(self):
        print(f'\r{self.__color}', end='')
        sleep(7)
        self.__color = 'Yellow'
        print(f'\r{self.__color}', end='')
        sleep(2)
        self.__color = 'Green'
        print(f'\r{self.__color}', end='')


a = TrafficLight()
a.running()
