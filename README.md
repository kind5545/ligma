# sukbollz.exe
Oh no... another USELESS repo. This time: fake malware w/ tkinter!!
So, in this repo my friend and I made fake malware to run in python. So.
This works on all platforms; even tested on a raspberry pi (4).
Here's a little layout on how the "malware" goes:
1. A person runs the file. (disguised as a Word document or other file)
2. A command line window opens with the file.
3. The user is prompted if the want to call the police.
4. If they say no, a window pops up obstructing their screen.
   * They have to close it 20 times.
6. If they say yes, a fake antivirus window pops up.
7. They have to close a window 5 times.
8. The program ends.
## Run this on your friend's computer:
We reccomend you use Windows, but macOS and Linux should work too.  
### Section 1: Getting required files
#### Step 1: Install Python
On most computers, Python 3 should already be installed (along with pip).
###### If it isn't:
Go to [python.org](https://python.org/downloads) and download Python 3.11 for your operating system.  
#### Step 2: Install pip
Once that's done, get pip (Python's package library). To check if you have pip installed, run
```
pip3 -v
```
If you do, jump to **Step 3**.  
If you get nothing or an error, here's how to install pip:
###### Windows:
 - Open `cmd.exe`.
 - Type in the command `<https://bootstrap.pypa.io/>`
 - If that doesn't work, try:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
 - Go into the directory that pip was installed in with `cd <directory>`
 - To check if pip was installed there, run the command `dir` and you should see `get-pip.py`.
 - Type the command `python3 get-pip.py`
 - After that, make sure pip is installed with `pip3 --version`.
###### macOS:
 - If you have brew installed, run the command `brew install pip3`. (you can install brew [here](https://brew.sh).)
 - If not, download pip [here](https://bootstrap.pypa.io/)
 - Go to the directory that pip was installed using `cd <directory>`.
 - To check if pip was installed there, use the command `ls` and you should see `main.py`.
 - Run `sudo python3 get-pip.py`
 - Done! To double-check if pip was installed, run `pip3 --version`.
###### Debian-based systems:
 - Run `sudo apt update`
 - Install pip using `sudo apt install python3-pip`
 - or for older systems run `sudo apt-get install python3-pip`.
###### Fedora/RedHat-based systems:
 - Run `dnf install python3-pip`
 - Check if pip installed with `pip3 --version`.
#### Step 3: Install dependencies
Now that you have pip installed, run these commands:
```
pip3 install inquirer
pip3 install pillow
```
### Section 2: Setting up the prank
#### Step 4: Download files
 - Download `main.py` and `rick-roll-icegif-5.gif`.
 - Put the files somewhere hidden, like in their `Documents` folder.
#### Step 5: Disguise files
To disguise this file, it depends on your operating system (to make it seem legit).  
Follow the instructions for your operating system.
###### Windows:
 - Right-click on `main.py`.
 - Select `Create Shortcut`.
 - Move the shortcut to wherever you want (I **highly** recommend the desktop.)
 - Right-click on the shortcut and select `Properties`.
 - Select the `Shortcut` tab.
 - Change the name to something like `note.docx`.
 - This is probably the **most important part**. Change the icon.
   * Click the `Change Icon` button.
   * Choose from one of the preset icons or click `Browse`.
   * **If you want to disguise your file as a Word document, click [here](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/.docx_icon.svg/1200px-.docx_icon.svg.png) to download the file icon for Windows 11. Click [here](https://upload.wikimedia.org/wikipedia/commons/thumb/archive/f/fb/20130629081057%21.docx_icon.svg/120px-.docx_icon.svg.png) for Windows 10.**
 - Done.
###### macOS:
 - Right-click on `main.py`.
 - Select `Make Alias`.
 - Drag it to the place where you want (I **highly** recommend the desktop.)
 - Copy the image that you want.
 - Right-click and select `Get Info` (or click `⌘ + I`)
 - Click on the tiny alias icon.
 - Paste using `⌘ + V`
 - In the text box that *should* say `main.py alias`, write the name of the file.
 - Done!
###### Linux:
 - Select `main.py`
 - While holding `ctrl + shift`, drag it to your `Desktop` folder.
 - Right-click on your newly-made shortcut.
 - Unfortunately, you cannot change the icon for shortcut files on most Linux distros right now. But, the icon automatically adapts to the filename.
 -  For example: (you name the file `thing.docx`) and the icon updates to a Word document file.
 -  I recommend you set it to `for_you.md`. Right-click on the file and select `Properties`. Change it.
 -  Done!
#### Step 6: Run the file
 - Say to your friend something like
> Hey, can you look at this document I made for you?
---
Thanks for pranking your friend! Attribution is appreciated, but **not** required.  

Good luck!  
-kind22232
