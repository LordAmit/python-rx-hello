import time
import random
time_in_seconds = int(input("Interval for writing in File: "))/100
count = int(input("Number of times for writing: "))


def write_in_file():
    randomizer = random.SystemRandom()

    random_file = open("random_file", mode="w")
    random_value = randomizer.randint(1, 20)
    random_file.write(str(random_value)+"\n")
    random_file.close()


def core():
    for i in range(0, count):
        write_in_file()


def main():
    core()


if __name__ == '__main__':
    main()
