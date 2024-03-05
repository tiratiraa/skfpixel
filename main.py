# PIXELSTATE: NON-ROOT METHOD OF CLEANSTATE KERNEL FLASHING ON PIXELS
# Data Wipe required on phone.

#pixel 6 and below stuff will be used later when i feel like doing so
#yall can do PRs n stuff and help me with the code lol

import subprocess
import os
import webbrowser

#var
# SET THIS AS YOUR PLATFORM-TOOLS FOLDER PATH
adbpath = r"C:\Users\benbo\OneDrive\Desktop\platform-tools"

#initialize
os.chdir(adbpath)

print("""░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  """)
print("This tool WILL wipe your device to be able to flash the custom kernel. Backup your device's content otherwise it will be gone in a matter of seconds.")
print(""""Be cautious.
""")

#input
print("""Welcome to PixelState!
This is something i wrote in my free time as a beginner python user. It's a non-root method to flash CleanState custom kernel on Pixel devices.

 To start, please specify your Pixel:
Pixel 7/7 Pro (7/7p)       Pixel 6 (6) [SOON]""")

command =""
while command != "break":
    modelinput = input("Option: ")
    if modelinput == "7":
        print("""Google Pixel 7 Chosen!
          """)
        break
    elif modelinput == "7p":
        print("""Google Pixel 7 Pro Chosen!
          """)
        break
    #elif modelinput == "6":
        #print("""Google Pixel 6 Chosen!
        #  """)
        #break
    elif modelinput == "hahafunnystupidthingyoushouldntdobecauseyeslolaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
        print("wha-??????")
        quit()
    else:
        print("Not a valid option")

    

print("""Now, we need to disable verity and we will need the vbmeta.img from your stock firmware. For this, a page will open with the list of your phone's firmware and you will need to download the one corresponding to your phone's current security patch.
IF you're using a custom rom, extrack vbmeta.img from your rom zip. If it's a recovery-flashable rom, use payload-dumper-go to extract the images from payload.bin and if its a fastboot-flashable rom then just extract the file from it.
      
If you chose the first option, after your browser opens with Google's firmware page, rerun PixelState and answer with 'n' to input your vbmeta file path.""")

command =""
while command != "break":
    webconfirm = input("Open web page? (y/n)")
    if webconfirm == "y":
        if modelinput == "7":
            link = "https://developers.google.com/android/images#panther"
            webbrowser.open(link)
            quit()
        elif modelinput == "7p":
            link = "https://developers.google.com/android/images#cheetah"
            webbrowser.open(link)
            quit()
        #elif modelinput == "6":
            #link = "https://developers.google.com/android/images#oriole"
            #webbrowser.open(link)
            #quit()
        elif modelinput == "hahafunnystupidthingyoushouldntdobecauseyeslolaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
            quit()
        else:
            print("Not a valid option")
    elif webconfirm == "n":
        print("skipping...")
        break
    else:
        print("Not a valid option")

fpmeta = input("File path: ")

#vbmeta file path check
sanitycheckvbmeta = input("""!!DOUBLE CHECK!!

Are you sure your vbmeta image is located at """ + fpmeta + " ? (y/n)")

if sanitycheckvbmeta == "y":
    print("Do NOT touch your device unless you're told to. Let adb do its thing before the next step.")
    f = "adb reboot bootloader"
    subprocess.Popen(f, shell=True)

    vbmeta = "fastboot flash vbmeta" + fpmeta + " --disable-verity --disable-verification"
    subprocess.Popen(vbmeta, shell=True)

    print("Wiping device so it doesnt corrupt...")
    wipe = "fastboot -w"
    subprocess.Popen(wipe, shell=True)

    print("Please provide your boot, dtbo and vendor_kernel_boot provided by CleanState.")
    boot = input("cleanslate-pantah-boot-xxxxxx.yyy--ZZZ.img: ")
    dtbo = input("cleanslate-pantah-dtbo-xxxxxx.yyy--ZZZ.img: ")
    vkb = input("cleanslate-pantah-vendor_kernel_boot-xxxxxx.yyy--ZZZ.img: ")

    print("Flashing " + boot + "to boot.")
    fboot = "fastboot flash boot" + boot
    subprocess.Popen(fboot, shell=True)

    print("Flashing " + dtbo + "to dtbo.")
    fdtbo = "fastboot flash dtbo" + dtbo
    subprocess.Popen(fdtbo, shell=True)

    print("Flashing " + vkb + "to vendor_kernel_boot.")
    fvkb = "fastboot flash vendor_kernel_boot" + vkb
    subprocess.Popen(fvkb, shell=True)

    print("Rebooting to fastbootd...")
    fd = "fastboot reboot fastboot"
    subprocess.Popen(fd, shell=True)

    print("Please provide your vendor_dlkm file provided by CleanState.")
    vdlkm = input("cleanslate-pantah-vendor_dlkm-xxxxxx.yyy--ZZZ.img: ")

    print("Flashing " + vdlkm + "to vendor_dlkm.")
    fvkb = "fastboot flash vendor_dlkm" + vkb
    subprocess.Popen(fvkb, shell=True)

    print("""CleanState Kernel should be flashed onto the device!
          
Thank you for using my (badly made) tool for flashing CleanState.
This meant to be a general purpose kernel flasher but i just couldnt do it with the amount of knowledge I have in python lol.
          
Enjoy CleanState on your device :)""")
    quit()

elif sanitycheckvbmeta == "n":
    print("Rerun PixelState to double check file path.")