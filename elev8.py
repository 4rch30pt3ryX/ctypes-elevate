import ctypes, sys, os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    print(os.system("whoami /groups > text17.txt"))
else:
    # Re-run the program with admin rights
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    print(os.system("whoami /groups > text17.txt"))


    # "net session >NUL 2>NUL && echo is admin text17.txt || echo isnt admin > text17.txt"
