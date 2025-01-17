import os
import shutil

user_name = os.environ.get('USERNAME') 
roblox_versions_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Roblox\\Versions"

required_files = [
    "content", 
    "RobloxCrashHandler.exe", 
    "RobloxPlayerInstaller.exe", 
    "RobloxPlayerBeta.exe"
]

def has_required_files(folder_path):
    for required in required_files:
        if not os.path.exists(os.path.join(folder_path, required)):
            return False
    return True

for folder_name in os.listdir(roblox_versions_path):
    folder_path = os.path.join(roblox_versions_path, folder_name)
    
    if os.path.isdir(folder_path):
        if not has_required_files(folder_path):
            print(f"Deleting folder: {folder_path}")
            shutil.rmtree(folder_path)

print("Cleanup completed.")
