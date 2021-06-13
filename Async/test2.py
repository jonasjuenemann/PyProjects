import time


def sleepIt():
    time.sleep(2)
    return 1

def test():
    return sleepIt()


if __name__ == "__main__":
    value = test()
    print(value)
