import os
import shutil

def add_to_startup():
    """ 📌 اضافه کردن برنامه به استارتاپ ویندوز """
    app_path = os.path.join(os.getenv("ProgramFiles"), "KhorshidCalendar", "khorshid_calendar.exe")
    startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    shortcut_path = os.path.join(startup_folder, "KhorshidCalendar.lnk")

    # 📌 ایجاد شورتکات برای اجرای خودکار
    with open(shortcut_path, "w") as shortcut:
        shortcut.write(f'@echo off\nstart "" "{app_path}"\n')

    print("✅ برنامه به استارتاپ ویندوز اضافه شد.")

if __name__ == "__main__":
    add_to_startup()
