import os

def get_version_strings():
    user_name = os.getlogin()
    base_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Roblox\\Versions"

    if not os.path.exists(base_path):
        print(f"The path {base_path} does not exist.")
        return

    required_files = {
        "content",
        "RobloxCrashHandler.exe",
        "RobloxPlayerInstaller.exe",
        "RobloxPlayerBeta.exe",
    }


    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)

        if os.path.isdir(folder_path) and folder.startswith("version-"):
            version_string = folder.split("version-")[-1]

            if all(os.path.exists(os.path.join(folder_path, file)) for file in required_files):
                print(" ")
                print(" ")
                print(f"           Version: {version_string}")
                print(" ")

if __name__ == "__main__":
    try:
        get_version_strings()
        input("\nEnter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
