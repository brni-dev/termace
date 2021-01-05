import colorama, os, subprocess, time, threading, sys, ctypes, base64
from dotenv import load_dotenv  
from colorama import init, Fore, Style, Back, AnsiToWin32, ansi
colorama.init(convert=True)
load_dotenv()

# Color variables for colorama
c_reset = Fore.RESET
c_resetall = Style.RESET_ALL
c_bright = Style.BRIGHT
c_normal = Style.NORMAL
c_green = Fore.GREEN
c_yellow = Fore.YELLOW
c_magenta = Fore.MAGENTA
c_blue = Fore.BLUE
c_red = Fore.RED
c_cyan = Fore.CYAN
c_white = Fore.WHITE
c_black = Fore.BLACK
c_lightmagenta = Fore.LIGHTMAGENTA_EX
c_lightred = Fore.LIGHTRED_EX
c_lightcyan = Fore.LIGHTCYAN_EX
c_lightgreen = Fore.LIGHTGREEN_EX
c_lightyellow = Fore.LIGHTYELLOW_EX
c_lightblue = Fore.LIGHTBLUE_EX
c_lightwhite = Fore.LIGHTWHITE_EX
c_lightblack = Fore.LIGHTBLACK_EX
#c_bold = colorama.Cursor

# Loads username from the actual user variable in Windows and a password from the .env file (Edit the .env file to change/delete your password)
usr_os = os.getenv("OS")
usrname = os.getenv("USERNAME")
pswrd = os.getenv("PASSWORD")

# Terminal strings
terminalgreen = f"{c_reset}[{c_green}TERMINAL{c_reset}]{c_yellow} "
terminalred = f"{c_reset}[{c_red}TERMINAL{c_reset}]{c_yellow} "
shellgreen = f"{c_reset}[{c_green}SHELL{c_reset}]{c_yellow} "
shellred = f"{c_reset}[{c_red}SHELL{c_reset}]{c_yellow} "

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Termace")
    print(colorama.ansi.clear_screen())
    print(f"{Back.MAGENTA}{c_black}Termace made by {c_white}brni-dev{c_normal}{c_white}{Back.RESET}\n")
    print(f"{terminalgreen}{c_reset}{shellred}Loading...{c_reset}")
    time.sleep(2)
    if usr_os != "Windows_NT":
        sys.exit(f"{terminalred}{c_reset}{shellred}This is currently only supported on Windows, or your OS environment variable was set wrong!{c_resetall}")
    if pswrd == None or pswrd == "":
        newpswrd = input(f"{terminalgreen}{c_reset}{shellred}New Password: {c_reset}")
        print(colorama.ansi.clear_line())
        verifnewpswrd = input(f"{terminalgreen}{c_reset}{shellred}Confirm new password: {c_reset}")
        while newpswrd != verifnewpswrd:
            print(f"\n{terminalred}{c_reset}{shellred}Error! Entered wrong password!{c_reset}\n")
            verifnewpswrd = input(f"{terminalgreen}{c_reset}{shellred}Confirm new password: {c_reset}")
        verifncoded = verifnewpswrd.encode("ascii") 
        base64_bytes = base64.b64encode(verifncoded) 
        base64_string = base64_bytes.decode("ascii")
        f = open(".env","w+")
        f.write(f"PASSWORD='{base64_string}'")
        f.close()
    else:
        print(colorama.ansi.clear_screen())
        entpasd = input(f"{terminalgreen}{c_reset}{shellred}Password to login: {c_reset}")
        base64_strin = os.getenv("PASSWORD")
        base64_byt = base64_strin.encode("ascii") 
        sample_string_bytes = base64.b64decode(base64_byt) 
        sample_string = sample_string_bytes.decode("ascii") 
        while entpasd != sample_string:
            print(f"\n{terminalred}{c_reset}{shellred}Error! Entered wrong password!{c_reset}\n")
            entpasd = input(f"{terminalgreen}{c_reset}{shellred}Password to login: {c_reset}")
    print(colorama.ansi.clear_screen())
    print(f"{terminalgreen}{c_reset}{shellred}Initializing...{c_reset}")
    time.sleep(1.5)
    print(f"{terminalgreen}{c_reset}{shellred}Initialized! Running...{c_reset}")
    time.sleep(0.6)
    print(f"{terminalgreen}{c_reset}{shellred}Logged in as {c_bright}{usrname}{c_normal}!{c_reset}")
    time.sleep(0.7)
    while True:
        onterm = False
        error = False
        """
        cmde = subprocess.check_output("cd", shell=True)
        direc = str(cmde.decode("utf-8"))"""
        cmd = input(f"{terminalgreen}{c_reset}{shellgreen}{c_magenta}{c_lightmagenta}~{c_reset} {c_blue}")
        #cmdex = str(cmd.decode(""))
        if "term" in cmd: onterm = True
        if onterm == False:
            try:
                check = subprocess.check_output(cmd, shell=True)
            except:
                print(f"{terminalgreen}{c_reset}{shellred}{c_lightred} Error! Command '{cmd}' returned non-zero exit status 1!{c_reset}")
                error = True
            if error == False:
                out = str(check.decode("utf-8"))
                print(c_reset + out)
        error = False
        onterm = False
        if cmd == "term --exit" or cmd == "term -e":
            sys.exit(f"{terminalgreen}{c_reset}{shellred}Exiting...{c_resetall}")
        elif cmd == "term --changepassword" or cmd == "term -cp":
            print(colorama.ansi.clear_screen())
            base64_strini = os.getenv("PASSWORD")
            base64_byti = base64_strini.encode("ascii") 
            sample_string_by = base64.b64decode(base64_byti) 
            sample_sring = sample_string_by.decode("ascii") 
            entpasd = input(f"{terminalgreen}{c_reset}{shellred}Old Password: {c_reset}")
            print(colorama.ansi.clear_screen())
            while entpasd != sample_sring:
                print(colorama.ansi.clear_screen())
                print(f"{terminalred}{c_reset}{shellred}Error! Entered wrong password!{c_reset}\n")
                entpasd = input(f"{terminalgreen}{c_reset}{shellred}Old Password: {c_reset}")
            print(colorama.ansi.clear_screen())
            newpswrd = input(f"{terminalgreen}{c_reset}{shellred}New Password: {c_reset}")
            while len(newpswrd) > 35 or len(newpswrd) < 5:
                print(colorama.ansi.clear_screen())
                print(f"{terminalred}{c_reset}{shellred} Error! Passwords cannot be smaller than 5 characters or longer than 35 characters!{c_reset}\n")
                newpswrd = input(f"{terminalgreen}{c_reset}{shellred}New Password: {c_reset}")
            print(colorama.ansi.clear_screen())
            verifnewpswrd = input(f"{terminalgreen}{c_reset}{shellred}Confirm new password: {c_reset}")
            while newpswrd != verifnewpswrd:
                print(colorama.ansi.clear_screen())
                print(f"{terminalred}{c_reset}{shellred}Error! Entered wrong password!{c_reset}\n")
                verifnewpswrd = input(f"{terminalgreen}{c_reset}{shellred}Confirm new password: {c_reset}")
            verifncode = verifnewpswrd.encode("ascii") 
            base6_bytes = base64.b64encode(verifncode) 
            base64_stri = base6_bytes.decode("ascii")
            f = open(".env","w+")
            f.write(f"PASSWORD='{base64_stri}'")
            f.close()
            print(colorama.ansi.clear_screen())
            print(f"{terminalgreen}{c_reset}{shellred}Successfully changed password! Returning to shell...{c_reset}")
        elif cmd == "term --userinfo" or cmd == "term -ui":
            basey64_strin = os.getenv("PASSWORD")
            base64_byty = basey64_strin.encode("ascii") 
            smple_string_bytes = base64.b64decode(base64_byty) 
            sam = smple_string_bytes.decode("ascii") 
            print(f"{c_reset}{c_green}User info:\n   -- {c_red}Username: {c_magenta}{usrname}\n   {c_green}-- {c_red}Password: {c_magenta}{sam}{c_reset}")
            time.sleep(3.6)
            print(colorama.ansi.clear_screen())
            print(f"{terminalgreen}{c_reset}{shellred}Screen cleared due to security reasons!{c_reset}")
        elif cmd == "term --clearscreen" or cmd == "term -cs":
            print(colorama.ansi.clear_screen())
        elif cmd == "term --help" or cmd == "term -h":
            print(f"{c_reset}dev was too lazy to make the help command so like yeah")

if __name__ == "__main__":
    main()
