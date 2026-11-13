from pathlib import Path
import winreg, os

user_folder = input(">> ")
folder = Path(user_folder)
folder_cout = 0
file_cout = 0
path = os.path.dirname(os.path.abspath(__file__))

# adding to PATH
key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    "Environment",
    0,
    winreg.KEY_ALL_ACCESS
)

old, _ = winreg.QueryValueEx(key, "Path")

if path.lower() not in old.lower():
    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, old + ";" + path)
winreg.CloseKey(key)


if folder.is_dir():
    print(f"{folder.name}/")
    
    for item in sorted(folder.iterdir()):
        
        if item.is_dir():  # if the folder's content is a folder, then display it like this
            folder_cout += 1
            print(f"├── {item.name}/")
            
            for inner_item in sorted(item.iterdir()):
                print(f"│   ├── {inner_item.name}/")
            
        else:
            file_cout += 1
            print(f"├── {item.name}")
        
        
    # displaying the number of files and folders
    print(f"\nFiles: {file_cout}")
    print(f"Folders: {folder_cout}")
    
            
# error handling
elif not folder.is_dir():
    print("[!] Error! Enter the full path.")
    
elif not folder.exists():
    print("[!] Error! Such a path does not exist.")