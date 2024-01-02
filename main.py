###NOTE: THIS IS NOT AN ACTUAL VIRUS THAT WILL HARM YOUR COMPUTER. THIS IS JUST A SATIRE.###
###NOTE: ANY DAMAGE DONE BY THIS IS NOT OUR FAULT. SUKBOLLS Inc. DIDN'T INSTALL ANYTHING  INTO THIS.###

# packages
from time import *
import inquirer as inq
import sys
import tkinter as tk
from PIL import ImageTk, Image
import os
import platform


# important stuff
def windefendClick():
    print("Protecting your mom... (this may take a while)")
    sleep(3)
    print(
        "Windows Defender could not identify the threat. Error 102: \"ligma has failed.\""
    )
    windefend.destroy()


def linuxClick():
    print("Protecting your mom... (this may take a while)")
    sleep(3)
    print(
        "Linux could not identify the threat. Error 102: \"ligma has failed.\""
    )
    linux.destroy()


def macClick():
    print("Protecting your mom... (this may take a while)")
    sleep(3)
    print(
        "Your Mac could not identify the threat. Error 102: \"ligma has failed.\""
    )
    mac.destroy()


def winSpam():
    for i in range(0, 10):
        print("HAHAHA SUCKER!!!!")
        bruh = tk.Tk()
        bruh.title("HAHAHA SUCKER!!!!")
        bruh.geometry("500x499")
        bruh.configure(bg="red")
        bruhText = tk.Label(
            bruh,
            text=
            "HAHAHA SUCKER!!!! YOU'LL NEVER GET OUT!!!! (close this window 10 more times)",
            font=("Arial", 20))
        bruh.mainloop()
        sleep(0.3)


def adwinSpam():
 for i in range(0, 10):
        print("HAHAHA SUCKER!!!!")
        bruh = tk.Tk()
        bruh.title("HAHAHA SUCKER!!!!")
        bruh.geometry("500x500")
        bruh.configure(bg="red")
        bruhText = tk.Label(
            bruh,
            text=
            "HAHAHA SUCKER!!!! YOU'LL NEVER GET OUT!!!! (close this window 10 more times)",
            font=("Arial", 20))
        bruh.mainloop()
        sleep(0.3)
        rickWin = tk.Tk()
        screenw = rickWin.winfo_screenwidth()
        screenh = rickWin.winfo_screenheight()
        rickWin.title("RICK ROLL!!!!")
        rickWin.geometry("%dx%d" % (screenw, screenh))
        # Open the image file
        image = Image.open("rick-roll-icegif-5.gif")
        # Resize the image to fit the window
        image = image.resize(
            (rickWin.winfo_screenwidth(), rickWin.winfo_screenheight()))
        # Convert the image to a Tkinter-compatible photo image
        tk_image = ImageTk.PhotoImage(image)
        # Create a label to display the image
        label = tk.Label(rickWin, image=tk_image)
        label.pack()
        rickWin.mainloop()
        sleep(2)
        rickWin.destroy()
        print("NEVER GONNA GIVE YOU UP!!!!")


opsys = platform.system()

# code
print(
    '''Hello. This is SUKBOLLZ.exe. You can play games on this website!!! It's a MARIO!!!!! \n
Legal: SUKBOLLZ inc. is not responsible for any damages caused by this program. (CHECK THE SOURCE CODE!!) '''
)
ynquestions = [
    inq.List('yn', message="Do you want to continue?", choices=['Yes', 'No'])
]
yn = inq.prompt(ynquestions)
if yn['yn'] == 'Yes':
    print('''\n
 ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄     ▄     ▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄      
█  █ █  █       █  █ █  █  █  █ █  █      █  █ █  █       █  █  █▄█  █      █   █   █ █ ▄ █ █      █   ▄  █ █       █     
█  █▄█  █   ▄   █  █ █  █  █  █▄█  █  ▄   █  █▄█  █    ▄▄▄█  █       █  ▄   █   █   █ ██ ██ █  ▄   █  █ █ █ █    ▄▄▄█     
█       █  █ █  █  █▄█  █  █       █ █▄█  █       █   █▄▄▄   █       █ █▄█  █   █   █       █ █▄█  █   █▄▄█▄█   █▄▄▄      
█▄     ▄█  █▄█  █       █  █   ▄   █      █       █    ▄▄▄█  █       █      █   █▄▄▄█       █      █    ▄▄  █    ▄▄▄█▄▄▄  
  █   █ █       █       █  █  █ █  █  ▄   ██     ██   █▄▄▄   █ ██▄██ █  ▄   █       █   ▄   █  ▄   █   █  █ █   █▄▄▄█   █ 
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄█ █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█  █▄█   █▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄▄█ 

HAHA SCREW YOU. GOODBYE.''')
polquestions = [
    inq.List('yn',
             message="Do you want to call the police?",
             choices=['Yes', 'No'])
]
pol = inq.prompt(polquestions)
if pol['yn'] == 'No':
    print('''\n HAHAHA wrong answer''')
	print("psst! (you can close the window 20 times and it will stop).")
    for i in range(0, 20):
        arghwin = tk.Tk()
        arghwin.title("HAHAHAHA")
        arghwin.mainloop()
if pol['yn'] == 'Yes':
    print('''Installing notavirus.exe...''')
    sleep(0.2)
    # security window
    if opsys == "Linux":
        linux = tk.Tk()
        linux.title("amogus@sukbollz:~$")
        linux.geometry("")
        linux.configure(bg="red")
        lLabel = tk.Label(
            linux,
            text=
            "Linux vscan has found a threat to your computer in \n /usr/bin/home/amogus/Documents/sukbollz/sukbollz.tar.gz",
            bg="red",
            fg="white")
        lButton = tk.Button(linux,
                            text="Take Action NOW",
                            command=linuxClick,
                            bg="black",
                            fg="red",
                            activebackground="red",
                            activeforeground="black")

        lButton.pack()
        lLabel.pack()
        linux.mainloop()
    elif opsys == "Windows":
        windefend = tk.Tk()
        windefend.title("Windows Defender")
        windefend.geometry("")
        windefend.configure(bg="red")
        wdLabel = tk.Label(
            windefend,
            text=
            "Windows Defender has found a threat to your computer in \n C:/Users/rickroll/Documents/SUKBOLLZ/SUKBOLLZ.exe",
            bg="red",
            fg="white")
        wdButton = tk.Button(windefend,
                             text="Take Action NOW",
                             command=windefendClick,
                             bg="black",
                             fg="red",
                             activebackground="red",
                             activeforeground="black")

        wdButton.pack()
        wdLabel.pack()
        windefend.mainloop()
    elif opsys == "Darwin":
        mac = tk.Tk()
        mac.title("Security")
        mac.geometry("")
        mac.configure(bg="red")
        macLabel = tk.Label(
            mac,
            text=
            "Your Mac has found a threat to your computer in \n /Users/amogus/Documents/SUKBOLLZ/sukbollz.app",
            bg="red",
            fg="white")
        macButton = tk.Button(mac,
                              text="Take Action NOW",
                              command=macClick,
                              bg="black",
                              fg="red",
                              activebackground="red",
                              activeforeground="black")

        macButton.pack()
        macLabel.pack()
        mac.mainloop()
    # end of windefend
    ad = tk.Tk()
    ad.title("TOTALLY LEGITIMATE AD")
    ad.geometry("500x500")
    ad.configure(bg="yellow")
    adText = tk.Label(
        ad,
        text="notavirus.exe has been successfully downloaded and installed.")
    adButton = tk.Button(ad,
                         text="CLIKC HERE 4 FFEREE $MONEY$",
                         command=adwinSpam)
    adText.pack()
    adButton.pack()
    ad.mainloop()
else:
    sys.exit()
