import os
import json

def main():
    user_path = os.path.expandvars(r"C:\\Users\\%USERNAME%\\AppData\\Local\\Roblox\\Versions")

    if not os.path.exists(user_path):
        print(f"Path does not exist: {user_path}")
        return

    for folder_name in os.listdir(user_path):
        folder_path = os.path.join(user_path, folder_name)

        if os.path.isdir(folder_path):
            required_files = [
                "content",
                "RobloxCrashHandler.exe",
                "RobloxPlayerInstaller.exe",
                "RobloxPlayerBeta.exe"
            ]

            if all(os.path.exists(os.path.join(folder_path, f)) for f in required_files):
                client_settings_path = os.path.join(folder_path, "ClientSettings")
                os.makedirs(client_settings_path, exist_ok=True)

                json_file_path = os.path.join(client_settings_path, "ClientAppSettings.json")
                settings = {
                    "DFIntTaskSchedulerTargetFps": 999999,
                    "FFlagGameBasicSettingsFramerateCap5": False,
                    "FFlagTaskSchedulerLimitTargetFpsTo2402": "False"
                }

                with open(json_file_path, "w") as json_file:
                    json.dump(settings, json_file, indent=4)

                print(f"ClientSettings created in: {folder_path}")
            else:
                print(f"Required files not found in: {folder_path}")

if __name__ == "__main__":
    main()
