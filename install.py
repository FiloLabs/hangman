import os
import subprocess
from subprocess import Popen
while True:
    dt = input('Would you like a desktop shortcut? > ')
    if dt.startswith('y'):
        dt = 1
        break
    elif dt.startswith('n'):
        dt = 0
        break
    else:
        print("Please only enter a yes/no (or y/n) response.")
if os.name == 'nt':
    os.chdir(os.environ['APPDATA'] + '\Microsoft\Windows\Start Menu\Programs')
    if not os.path.exists(os.environ['APPDATA'] + '\Microsoft\Windows\Start Menu\Programs\jvadair'):
        os.makedirs('jvadair')
    os.chdir(os.environ['APPDATA'])
    if not os.path.exists(os.environ['APPDATA'] + '\jvadair'):
        os.makedirs('jvadair')
    os.chdir('jvadair')
    os.system('curl -LJo hangman.exe https://github.com/FiloLabs/hangman/raw/master/Windows/no-install/hangman.exe')
    pth = '"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\jvadair\\'
    while True:
        batfile = open('execvbs.bat', 'w')
        batfile.write('''@echo off

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = ''' + pth + '''Hangman.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%APPDATA%\jvadair\hangman.exe" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%''')
        batfile.close()
        p = Popen("execvbs.bat")
        stdout, stderr = p.communicate()
        os.remove('execvbs.bat')
        if dt == 1:
            dt = dt - 1
            pth = '"%USERPROFILE%\\Desktop\\'
        else:
            break
    print('Done. The program should show up in your start menu now. If it doesn\'t show up at first, try again.')
    print('There is no need to delete the installer, as it can be run again to update the program.')
    input('Press enter to close this window.')
else:
    userpath = os.path.expanduser('~')
    os.chdir(userpath)
    if not os.path.exists('Games'):
        os.makedirs('Games')
    os.chdir('Games')
    if not os.path.exists('jvadair'):
        os.makedirs('jvadair')
    os.chdir('jvadair')
    if not os.path.exists('Hangman'):
        os.makedirs('Hangman')
    os.chdir('Hangman')
    if 'arm' in os.uname():
        os.system('curl -LJo hangman https://github.com/FiloLabs/hangman/raw/master/Linux/hangman_arm')
    else:
        os.system('curl -LJo hangman https://github.com/FiloLabs/hangman/raw/master/Linux/hangman')
    os.system('x-terminal-emulator -e "sudo chown ' + userpath[6:]+ ' hangman && sudo chmod 770 hangman"')
    pth = '/usr/share/applications'
    while True:
        os.chdir(pth)
        os.system('x-terminal-emulator -e "sudo curl -LJo hangman.desktop https://github.com/FiloLabs/hangman/raw/master/Linux/hangman.desktop && sudo chown ' + userpath[6:] + ' hangman.desktop"')
        if dt == 1:
            dt = dt - 1
            pth = userpath + '/Desktop'
        else:
            break
    os.chdir('/usr/share/icons')
    os.system('x-terminal-emulator -e "sudo curl -LJo jvaico.png https://github.com/FiloLabs/hangman/raw/master/jvaico.png"')
    print('Please enter your password in the popup windows so that the installer can download the neccessary files. The program should then show up in your application menu. If it doesn\'t show up at first, try again.')
    print('There is no need to delete the installer, as it can be run again to update the program.')
    input('Press enter to close this window.')
