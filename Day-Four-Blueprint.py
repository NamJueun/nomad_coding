import requests
import os


def restart():
    answer = str(input("Do you want to start over? y/n")).lower()
    if answer == "y" or answer == "n":
        if answer == "n":
            print("ok. bye!")
            return
        elif answer == "y":
            check()
    else:
        print("That's not a valid answer()")
        restart()


def check():
    os.system("clear")
    print("Please write a URL or URLS you want to check. (separated by comma)")
    http_input = str(input()).lower().split(",")
    for inputs in http_input:
        inputs = inputs.strip()
        if "." not in inputs:
            print(inputs, "is not a valid URL.")
        else:
            if "http" not in inputs:
                inputs = f"http://{inputs}"
            try:
                request_input = requests.get(http_input)
                if request_input.status_code == 200:
                    print(inputs, "is up!")
                else:
                    print(inputs, "is down!")
            except:
                print(inputs, "is down!")\

    restart()


check()
