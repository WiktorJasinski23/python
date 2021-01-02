from abc import ABC
import logging
import random

logger = logging.Logger(__name__)
file_handler = logging.FileHandler('car.log')
formatter = logging.Formatter('%(levelname)s\n %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)


def handle_error():
    logger.info("Something was wrong with your input. Please try again")
    return "Something was wrong with your input. Please try again"


def menu_info():
    logger.info("Currently supported acts: Accelerate, Slow_down, Stop, Turn_left, Turn_right, Get_car_info, "
                "Check_money, Menu_info, Quit\n"
                "Accelerate, Slow_down, Turn_left and Turn_right need an amount next to them to work.\n"
                " ")
    return "Currently supported acts: Accelerate, Slow_down, Stop, Turn_left, Turn_right, Get_car_info, " \
           "Check_money, Menu_info, Quit\n" \
           "Accelerate, Slow_down, Turn_left and Turn_right need an amount next to them to work.\n" \
           " "


def handle_speed(car):
    if car.speed == car.max_speed:
        logger.info("The car is going at its max speed of %d km/h! You sure are no slouch!" % car.speed)
        return "The car is going at its max speed of %d km/h! You sure are no slouch!" % car.speed
    elif car.speed > 150:
        logger.info("The car is going at a very high speed of %d! It's not a driveway!" % car.speed)
        return "The car is going at a very high speed of %d! It's not a driveway!" % car.speed
    else:
        logger.info("The car is going at the speed of %d km/h." % car.speed)
        return "The car is going at the speed of %d km/h." % car.speed


def handle_wheel_angle(car):
    if car.wheel_angle >= 0:
        logger.info("The current steering angle is %d degrees right." % car.wheel_angle)
        return "The current steering angle is %d degrees right." % car.wheel_angle
    elif car.wheel_angle < 0:
        logger.info("The current steering angle is %d degrees left." % abs(car.wheel_angle))
        return "The current steering angle is %d degrees left." % abs(car.wheel_angle)
    else:
        logger.info("The car is going straight.")
        return "The car is going straight."


def handle_input(obj):
    string = input()
    try:
        tab = ["", 0]
        tab[0], tab[1] = string.split()
        obj[0] = tab[0]
        obj[1] = float(tab[1])
    except ValueError:
        logger.error(handle_error())
        obj[0] = string


def clear_table(tab):
    tab[0] = ""
    tab[1] = 0


class CarModel:
    def __init__(self):
        logger.info('The program is creating a CarModel object.')
        self.brand = " "
        self.name = " "
        self.max_speed = 0

    def __str__(self):
        logger.info("Requested information about the car: \n"
                    "This one is a beauty! \n"
                    'Brand: %s, Model: %s, Max_Speed: %d' % (self.brand, self.name, self.max_speed))
        return 'This one is a beauty!\n' \
               'Brand: %s, Model: %s, Max_Speed: %d' % (self.brand, self.name, self.max_speed)

    def input_car_info(self):
        print("Please enter the brand name of the car:")
        self.brand = input()
        print("Please enter the car model:")
        self.name = input()
        print("Please enter the car's max speed:")
        self.max_speed = int(input())


class Car:
    def __init__(self, car_model: CarModel, id_number: int):
        logger.info('The program is creating a Car object')
        self.wheel_angle = 0
        self.speed = 0
        self.runs_idle = True
        self.car_model = car_model
        self.driver_is_alive = True
        self.ID = id_number
        self.max_speed = car_model.max_speed
        self.seats_left = 4
        self.money = 0
        self.options = {
            "accelerate": self.accelerate,
            "slow_down": self.slow_down,
            "turn_left": self.turn_left,
            "turn_right": self.turn_right,
            "stop": self.stop,
            "check_money": self.check_money,
            "get_car_info": self.get_car_info,
            "menu_info": menu_info,
            "quit": quit
        }
        self.task = ["", 0]

    def act(self):
        try:
            return self.options[self.task[0].lower()]()
        except KeyError:
            logger.error(handle_error())
            return handle_error()

    def quit(self):
        logger.info("The app is quitting...")
        self.driver_is_alive = False

    def accelerate(self):
        if self.task[1] > 0:
            self.speed += self.task[1]
            self.runs_idle = False
            logger.info("Accelerating the car..")
            if self.speed > self.max_speed:
                logger.info("The car can't go any faster!")
                print("Accelerating the car..")
                self.speed = self.max_speed
                return "The car can't go any faster!"
            return "Accelerating the car.."
        else:
            logger.error(handle_error())
            return handle_error()

    def slow_down(self):
        if self.task[1] > 0:
            self.speed -= self.task[1]
            if self.speed < 0:
                self.speed = 0
                self.runs_idle = True
            logger.info("Slowing down the car by %d km/h..." % self.task[1])
            return "Slowing down the car by %d km/h..." % self.task[1]
        else:
            logger.error(handle_error())
            return handle_error()

    def stop(self):
        self.speed = 0
        self.wheel_angle = 0
        self.runs_idle = True
        logger.info("Stopping the car...")
        return "Stopping the car..."

    def turn_left(self):
        if self.task[1] > 0:
            self.wheel_angle -= self.task[1]
            if self.wheel_angle < -450:
                self.wheel_angle = -450
            logger.info("The car is turning %d degrees left." % (self.task[1]))
            return "The car is turning %d degrees left." % (self.task[1])
        else:
            logger.error(handle_error())
            return handle_error()

    def turn_right(self):
        if self.task[1] > 0:
            self.wheel_angle += self.task[1]
            if self.wheel_angle > 450:
                self.wheel_angle = 450
            logger.info("The car is turning %d degrees right" % (self.task[1]))
            return "The car is turning %d degrees right" % (self.task[1])
        else:
            logger.error(handle_error())
            return handle_error()

    def get_car_info(self):
        return self.car_model

    def check_money(self):
        if self.money > 100:
            logger.info("You are doing great! You managed to gain %d dollars!" % self.money)
            return "You are doing great! You managed to gain %d dollars!" % self.money
        elif self.money > 50:
            logger.info("That's some good money you got there. %d dollars!" % self.money)
            return "That's some good money you got there. %d dollars!" % self.money
        elif self.money > 0:
            logger.info("Well, not bad. At least you got something. %d dollars!" % self.money)
            return "Well, not bad. At least you got something. %d dollars!" % self.money
        else:
            logger.info("You are broke! You better get some cash flowing in! 0 dollars, my friend!")
            return "You are broke! You better get some cash flowing in! 0 dollars, my friend!"

    def change_money(self, x):
        try:
            self.money += x
        except TypeError:
            logger.info("x = 0, No money was changed.")


class Event(ABC):
    def log_info(self, result):
        pass

    def execute(self, car):
        pass

    def check_event(self, token, car):
        pass


class Hitchhiker(Event):
    def check_event(self, token, car):
        if 1 <= token <= 5:
            self.execute(car)
        else:
            print("The road ahead is clear.")

    def execute(self, car):
        logger.info("Oh look! A hitchhiker! I think he's going in the same direction as you! He looks hopeful!")
        print("Oh look! A hitchhiker! I think he's going in the same direction as you! He looks hopeful!")
        result = self.take_hitchhiker(car)
        logger.info(self.log_info(result))

    def take_hitchhiker(self, car):
        if car.seats_left:
            logger.info("You may take another passenger with you! What's your decision? Yes/No")
            print("You may take another passenger with you! What's your decision? Yes/No")
            choice = input()
            if choice == "Yes":
                car.seats_left = car.seats_left - 1
                car.change_money(self.money_gained(car))
                print("You have taken on a new passenger!")
                return 1
            elif choice == "No":
                car.change_money(self.money_stolen(car))
                print("You decided not to give the hitchhiker a ride. He starts swearing at you.")
                return 2
            else:
                print("You blabbered some incomprehensible stuff at the passenger.\n"
                      "He probably thinks you are a weirdo.")
                return 3

        else:
            logger.info("Your car is full! You would need to kick out a passenger! What's your decision? Yes/No")
            print("Your car is full! You would need to kick out a passenger! What's your decision? Yes/No")
            choice = input()
            if choice == "Yes":
                car.seats_left -= 1
                print("You have kicked a passenger out!")
                car.change_money(self.money_stolen(car))
                return 4
            else:
                print("You have some morals. You decide to leave the passengers be.")
                return 5

    def money_stolen(self, car):
        if 0 <= random.randint(0, 10) <= 3:
            if car.money == 0:
                print("That person tried to steal your money. Thankfully, you have none.")
                return 0
            else:
                new_money = random.randint(1, car.money)
                logger.info("That person violently attacked you and stole %d dollars from you!" % new_money)
                print("That person violently attacked you and stole %d dollars from you!" % new_money)
                return new_money

    def money_gained(self, car):
        if 0 < random.randint(0, 10) <= 7:
            new_money = random.randint(1, 100)
            logger.info("That kind person gave you %d dollars!" % new_money)
            print("That kind person gave you %d dollars!" % new_money)
            return new_money
        else:
            return 0

    def log_info(self, result):
        if result == 1:
            logger.info("You have taken on a new passenger!")
        elif result == 2:
            logger.info("You decided not to give the hitchhiker a ride. He starts swearing at you.")
        elif result == 3:
            logger.info("You blabbered some incomprehensible stuff at the hitchhiker. "
                        "He probably thinks you are a weirdo. He leaves while muttering some words to himself.")
        elif result == 4:
            logger.info("You have kicked a passenger out!")
        elif result == 5:
            logger.info("You have some morals. You decide to leave the passengers be.")
        logger.info("// end of hitchhiker appearance //")


class Crash(Event):
    def check_event(self, token, car_obj):
        print("The car is about to crash! You need to act!")
        handle_input(car_obj.task)
        print(car_object.act())
        if token == "Rainfall" and car_obj.speed > 70:
            self.execute(car_obj)
        elif token == "Blizzard" and car_obj.speed > 50:
            self.execute(car_obj)
        elif token == "Sunshine" and car_obj.speed > 150:
            self.execute(car_obj)
        else:
            print("You just barely managed to avoid the crash!")
            self.log_info(1)

    def log_info(self, result):
        if result == 0:
            logger.info("The car has crashed! I don't think anyone has survived! What was the driver thinking?")
        else:
            logger.info("You just barely managed to avoid the crash!")

    def execute(self, car):
        car.driver_is_alive = False
        print("The car has crashed! I don't think anyone has survived! What was the driver thinking?")
        self.log_info(0)


class WeatherCondition(Event):
    def check_event(self, token, car, weather):
        if 4 <= token <= 8:
            print("The weather is changing....")
            result = self.execute(car)
            self.log_info(result)
            return result
        else:
            print("The weather is the same as before.")
            return weather

    def execute(self, car):
        new_weather = random.randint(0, 2)
        if new_weather == 0:
            return "Blizzard"
        elif new_weather == 1:
            return "Rainfall"
        elif new_weather == 2:
            return "Sunshine"

    def log_info(self, result):
        logger.info("The weather is changing...")
        if result == "Blizzard":
            logger.info("It is snowing heavily!")
        elif result == "Rainfall":
            logger.info("It is raining heavily!")
        else:
            logger.info("The sun is shining bright!")

    def display_weather(self, current_weather):
        self.log_info(current_weather)
        if current_weather == "Blizzard":
            print("It is snowing heavily now!\n")
        elif current_weather == "Rainfall":
            print("It is raining heavily now!\n")
        else:
            print("The sun is shining bright! You feel relaxed!\n")


class Environment:
    def __init__(self, car: Car):
        logger.info("Creating the environment...")
        self.car = car
        self.current_weather = " "
        self.weather_condition = WeatherCondition()
        self.crash = Crash()
        self.hitchhiker = Hitchhiker()
        self.token = 0

    def check_events(self):
        self.hitchhiker.check_event(self.token, self.car)
        self.current_weather = self.weather_condition.check_event(self.token, self.car, self.current_weather)
        self.weather_condition.display_weather(self.current_weather)
        if 6 < self.token <= 10:
            self.crash.check_event(self.current_weather, self.car)

    def begin(self):
        logger.info("Starting the environment...")
        while self.car.driver_is_alive:
            menu_info()
            clear_table(self.car.task)
            if self.car.runs_idle:
                print("The car runs idle. Input your command of choice: ")
            else:
                print(handle_wheel_angle(self.car))
                print(handle_speed(self.car))
            handle_input(self.car.task)
            print(self.car.act())
            self.token = random.randint(0, 10)
            print(" ")
            self.check_events()


if __name__ == "__main__":
    print("The general goal of this game is to get as much money as possible.")
    print(menu_info())
    random.seed()
    model = CarModel()
    model.input_car_info()
    car_object = Car(model, 1)
    environment = Environment(car_object)
    environment.begin()
