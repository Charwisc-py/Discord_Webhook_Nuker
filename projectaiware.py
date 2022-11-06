'''
Developed completely by charwisc#6969. If you have any questions, feel free to DM me on Discord.

Youtube channel: Project AI  

If you want to use this code, please give me credit. Thanks!
'''
import os
import sys
import requests

def printFlooder():
    print('''
\033[38;5;43m    ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ███████╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
\033[38;5;42m    ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
\033[38;5;41m    ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  █████╗░░██║░░░░░██║░░██║██║░░██║██║░░██║█████╗░░██████╔╝
\033[38;5;40m    ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░░░░██║░░██║██║░░██║██║░░██║██╔══╝░░██╔══██╗
\033[38;5;41m    ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
\033[38;5;42m    ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝''')

def printDeleter():
    print('''
\033[38;5;213m░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ██████╗░███████╗██╗░░░░░███████╗████████╗███████╗██████╗░
\033[38;5;212m░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗
\033[38;5;211m░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░██████╔╝
\033[38;5;210m░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
\033[38;5;211m░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗██║░░██║
\033[38;5;212m░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝''')

def title():
    #set the title to the following text in red fading to pink and then center the text
    print("\033[38;5;196m\n /$$$$$$$                                               /$$            /$$$$$$  /$$$$$$       /$$      /$$                              ")
    print("\033[38;5;197m| $$__  $$                                             | $$           /$$__  $$|_  $$_/      | $$  /$ | $$                              ")
    print("\033[38;5;198m| $$  \ $$ /$$$$$$   /$$$$$$  /$$  /$$$$$$   /$$$$$$$ /$$$$$$        | $$  \ $$  | $$        | $$ /$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$ ")
    print("\033[38;5;199m| $$$$$$$//$$__  $$ /$$__  $$|__/ /$$__  $$ /$$_____/|_  $$_/        | $$$$$$$$  | $$        | $$/$$ $$ $$ |____  $$ /$$__  $$ /$$__  $$")
    print("\033[38;5;200m| $$____/| $$  \__/| $$  \ $$ /$$| $$$$$$$$| $$        | $$          | $$__  $$  | $$        | $$$$_  $$$$  /$$$$$$$| $$  \__/| $$$$$$$$")
    print("\033[38;5;201m| $$     | $$      | $$  | $$| $$| $$_____/| $$        | $$ /$$      | $$  | $$  | $$        | $$$/ \  $$$ /$$__  $$| $$      | $$_____/")
    print("\033[38;5;200m| $$     | $$      |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$  |  $$$$/      | $$  | $$ /$$$$$$      | $$/   \  $$|  $$$$$$$| $$      |  $$$$$$$")
    print("\033[38;5;199m|__/     |__/       \______/ | $$ \_______/ \_______/   \___/        |__/  |__/|______/      |__/     \__/ \_______/|__/       \_______/")
    print("\033[38;5;198m                        /$$  | $$                                                                                                       ")
    print("\033[38;5;197m                       |  $$$$$$/                                                                                                       ")
    print("\033[38;5;196m                        \______/                                                                                                        ")


#Defines a function to get the users option
def getOptions():

    print('''\033[38;5;200m\n
    █████████████████████████████████████████
    █─▄▄─█▄─▄▄─█─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█
    █─██─██─▄▄▄███─████─██─██─██─█▄▀─██▄▄▄▄─█ 
    ▀▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
    \n\n[1] Discord Webhook Flooder\n[2] Discord Webhook Deleter''')


    option = input("\033[38;5;15m\n\nEnter your option: ")
    
    if option == '1':
        #if the user chooses option 1, run the discord webhook flooder
        webhookFlooder()
    elif option == '2':
        #if the user chooses option 2, run the discord webhook deleter
        webhookDeleter()
    else:
        sys.exit("Error: Invalid option")

#Defines a function to run the discord webhook flooder using the requests module
def webhookFlooder():
    #clear the windows cmd window
    os.system('cls')
    #print the title of the cmd window
    printFlooder()

    #defaults setimage to false
    sendimage = False

    #set the color of the text to white
    print("\033[38;5;15m")
    #ask the user for the webhook url
    webhook = input("\nEnter the webhook url: ")
    #ask the user for the message to send
    message = input("\nEnter the message to send: ")
    #ask the user for the image link to send with the message
    if input("\nDo you want to send an image with the message? (y/n): ") == 'y':
        sendimage = True
        image = input("\nEnter the image link: ")


    #ask the user for the amount of times to send the message
    amount = int(input("Enter the amount of times to send the message: "))

    #clear the windows cmd window
    os.system('cls')
    #print the title of the cmd window
    printFlooder()

    print("\033[38;5;10m")
    #print that the message is being sent
    print("\nSending message...")

    #set the color of the text to grey
    print("\033[38;5;254m")
    #loop through the amount of times the user wants to send the message
    for i in range(amount):
        #send the message to the webhook url using the requests module
        requests.post(webhook, json={'content': message})
        #send the image to the webhook url using the requests module
        if sendimage == True:
            requests.post(webhook, json={"content": image})
        #print the amount of times the message has been sent
        print(f"Sent message {i + 1} times")

    #set the color of the text to green
    print("\033[38;5;10m")
    #print that the message has been sent
    print("Message sent")

    #set the color of the text to white
    print("\033[38;5;15m")
    #keep the window open until the user presses enter
    input("\n\nPress [Enter] to return to the main menu...")
    main()

#Defines a function to run the discord webhook deleter using requests module
def webhookDeleter():
    #clear the windows cmd window
    os.system('cls')
    #print the title of the cmd window
    printDeleter()

    #set the color of the text to white
    print("\033[38;5;15m")
    #ask the user for the webhook url
    webhook = input("\nEnter the webhook url: ")

    #clear the windows cmd window
    os.system('cls')
    #print the title of the cmd window
    printDeleter()

    print("\033[38;5;10m")
    #print that the webhook is being deleted
    print("\nDeleting webhook...")

    #delete the webhook using the requests module
    requests.delete(webhook)

    #set the color of the text to green
    print("\033[38;5;10m")
    #print that the webhook has been deleted
    print("Webhook deleted")

    #set the color of the text to white
    print("\033[38;5;15m")
    #keep the window open until the user presses enter
    input("\n\nPress [Enter] to return to the main menu...")
    main()



#main function
def main():
    #set the size of the cmd window to 150x35 lines
    os.system('mode con: cols=150 lines=35')
    #clear the windows cmd window
    os.system('cls')
    #print the title of the cmd window
    os.system('title Webhook Flooder and Deleter by Project AI') 

    title()
    
    #keep the window open until the user presses enter, make the color of the text white
    input("\033[38;5;15m\n\n\nPress Enter to continue...")

    #clear the windows cmd window and print the title again
    os.system('cls')
    title()

    getOptions() 

#run the main function
if __name__ == "__main__":
    main()








