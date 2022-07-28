import random
import time

class Remote_control():

    def __init__(self,tv_case = "Close", tv_sound = 0,tv_brightness = 5, channel_list = ["Disney Channel"],channel = "Disney Channel"):
        self.tv_case = tv_case
        self.tv_sound = tv_sound
        self.channel_list = channel_list
        self.channel = channel
        self.tv_brightness = tv_brightness

    def turn_on_the_Tv(self):
        if(self.tv_case == "Open"):
            print("TV is already on")
        else:
            print("TV is turning on")
            self.tv_case = "Open"

    def turn_off_the_Tv(self):
        if self.tv_case == "Close":
            print("TV is already off")
        else:
            print("TV is turning off")
            self.tv_case = "Close"

    def set_the_sound(self):
        if self.tv_sound == 0:
            print("TV is already mute")
        else:
            print("TV is turning mute")
            self.tv_sound = 0

        while True:
            answer = input("For turn down the volume : '<'\nFor turn up the volume : '>'\nExit : exit\n")

            if answer == "<":
                if self.tv_sound != 0:
                    self.tv_sound -= 1
                    print("Volume : ",self.tv_sound)

            elif answer == ">":
                if self.tv_sound != 40:
                    self.tv_sound +=1
                    print("Volume : ",self.tv_sound)
            else:
                print("The sound has been updated : ",self.tv_sound)
                break

    def mute(self,tv_sound):
            if self.tv_sound == 0:
                print("TV is alredy MUTE...")
            else:
                print("TV is turning mute")
                self.tv_sound = 0

    def set_the_brightness(self):
        while True:
            answer = input("For turn down the brightness : '-'\nFor turn up the brightness : '+'\nExit : exit\n")

            if answer == "-":
                if self.tv_brightness != 0:
                    self.tv_brightness -= 1
                    print("Brightness : ",self.tv_brightness)

            elif answer == "+":
                if self.tv_brightness != 20:
                    self.tv_brightness +=1
                    print("Brightness : ",self.tv_brightness)
            else:
                print("The brightness has been updated : ",self.tv_brightness)
                break


    def add_channel(self,chaneel_name):
        print("Channel is being added.....")
        time.sleep(1)
        self.channel_list.append(chaneel_name)
        print("Channel added.")
        print("Channel list : ",self.channel_list)

    def remove_channel(self,channel_name):
        print("Channel is being removed.....")
        time.sleep(1)
        self.channel_list.remove(channel_name)
        print("Channel removed.")
        print("Channel list : ",self.channel_list)

    def menu(self,channel_list):
        input("Press 'OK' for open channel list : ")
        for index,channel in enumerate(channel_list):
            print(index+1,channel)
        a = input("Enter the channel number : ")
        self.channel = channel_list[int(a)-1]
        print("Current channel : ",self.channel)
        input("Press 'OK' for close channel list : ")

    def random_channel(self): 
        random1 = random.randint(0,len(self.channel_list)-1)  
        self.channel = self.channel_list[random1]
        print("Current channel : ",self.channel)

    def __len__(self):

        return len(self.channel_list) 

    def __str__(self):

        return "TV case : {}\nTV sound : {}\nChannel list : {}\nCurrent channel : {}\nBrightness : {}".format(self.tv_case,self.tv_sound,self.channel_list,self.channel,self.tv_brightness)

remote_control = Remote_control()

print("""
Welcome to remote control app...

1. Turn on the TV

2. Turn off the TV

3. Set the sound

4.MUTE

5.Set the brightness

6. Add channel

7. Remove channel

8. Menu

9. Find out the number of channels

10. Random channel

11. TV information

12. Exit

""")

while True:
    option = input("Choose the option you want to do : ")

    if option == "12":
        print("Bye...")
        break
    
    if option == "1":
        remote_control.turn_on_the_Tv()
    elif option == "2":
        remote_control.turn_off_the_Tv()
        break
    elif option == "3":
        remote_control.set_the_sound()

    elif option == "4":
        remote_control.mute(remote_control.tv_sound)

    elif option == "5":
        remote_control.set_the_brightness()

    elif option == "6":
        channel_names = input("Enter channel names separated by ',' : ")

        channel_list = channel_names.split(",")

        for will_be_added in channel_list:
            remote_control.add_channel(will_be_added)
    elif option == "7":

        channel_names = input("Enter channel names separated by ',' : ")

        channel_list = channel_names.split(",")

        for will_be_removed in channel_list:
            remote_control.remove_channel(will_be_removed)

    elif option == "8":
        remote_control.menu(remote_control.channel_list)

    elif option == "9":
        print("Number of channels : ",len(remote_control))

    elif option == "10":
        remote_control.random_channel()
    elif option == "11":
        print(remote_control)

    else: 
        print("Wrong option...")