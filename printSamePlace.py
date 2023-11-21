from time import sleep

animation = ("/", "-", "\\", "|")

def example1():
        for char in animation:
            print(char+"\b", end="")
            sleep(0.2)
            
def example2():
        x = 0
        while x < 100:
            print(f"{x:2}\b\b", end="")
            sleep(0.1)
            x += 1

if __name__ == "__main__":
    while True:
        example1()
