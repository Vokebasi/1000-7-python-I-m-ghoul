from playsound import playsound 
import time




def GHOUL():
    playsound( 'ghoul.mp3' ) 
    for i in range(1000, 0, -7):
        if i <= 7:
            break
        print(f"{i} - 7 = {i - 7}")
        time.sleep(0.03)
    print("I'm Ghoul")


if __name__ == "__main__":
    GHOUL()

