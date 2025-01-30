import sys
import time
import jdatetime
import os
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction, QPainter, QPixmap, QFont
from PyQt6.QtCore import Qt

class KhorshidCalendar:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # 📌 تاخیر برای حل مشکل نمایش در ویندوز 11
        time.sleep(2)
        self.app.setQuitOnLastWindowClosed(False)

        # 📌 بررسی اینکه System Tray در دسترس هست یا نه
        if not QSystemTrayIcon.isSystemTrayAvailable():
            print("❌ System Tray is not available on this system.")
            sys.exit(1)
        
        # 📌 دریافت تاریخ شمسی
        self.update_date()

        # 📌 ایجاد آیکون روز (عدد بدون پس‌زمینه)
        self.tray_icon = QSystemTrayIcon(self.create_day_icon(), self.app)
        self.tray_icon.setToolTip(self.full_date)  # 📌 نمایش تاریخ کامل فارسی هنگام Hover

        # 📌 ایجاد منوی خروج
        menu = QMenu()
        exit_action = QAction("خروج", self.app)
        exit_action.triggered.connect(self.exit_app)
        menu.addAction(exit_action)
        self.tray_icon.setContextMenu(menu)

        self.tray_icon.show()
        print("✅ برنامه در System Tray اجرا شد.")
        sys.exit(self.app.exec())

    def update_date(self):
        """ 📌 دریافت تاریخ شمسی و تبدیل به عدد روز + تاریخ کامل فارسی """
        today = jdatetime.date.today()
        self.day = str(today.day)  # 📌 فقط عدد روز (مثلاً: "12")
        self.full_date = today.strftime("%A | %d %B | %Y")  # 📌 نمایش تاریخ کامل فارسی
        self.full_date = self.convert_to_persian(self.full_date)  # 📌 تبدیل متن به فارسی

    def convert_to_persian(self, text):
        """ 📌 تبدیل نام روزها و ماه‌ها به فارسی """
        text = text.replace("Saturday", "شنبه")
        text = text.replace("Sunday", "یک‌شنبه")
        text = text.replace("Monday", "دوشنبه")
        text = text.replace("Tuesday", "سه‌شنبه")
        text = text.replace("Wednesday", "چهارشنبه")
        text = text.replace("Thursday", "پنج‌شنبه")
        text = text.replace("Friday", "جمعه")

        text = text.replace("Farvardin", "فروردین")
        text = text.replace("Ordibehesht", "اردیبهشت")
        text = text.replace("Khordad", "خرداد")
        text = text.replace("Tir", "تیر")
        text = text.replace("Mordad", "مرداد")
        text = text.replace("Shahrivar", "شهریور")
        text = text.replace("Mehr", "مهر")
        text = text.replace("Aban", "آبان")
        text = text.replace("Azar", "آذر")
        text = text.replace("Dey", "دی")
        text = text.replace("Bahman", "بهمن")
        text = text.replace("Esfand", "اسفند")

        return text

    def create_day_icon(self):
        """ 📌 ایجاد آیکون عدد روز بدون پس‌زمینه (Transparent) """
        size = 64  # اندازه آیکون
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)  # 📌 پس‌زمینه کاملاً شفاف
        
        # 📌 رسم عدد روز روی آیکون بدون پس‌زمینه
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        font = QFont("Arial", 28, QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.black)
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, self.day)  # 📌 رسم عدد روز
        painter.end()

        return QIcon(pixmap)

    def exit_app(self):
        """ 📌 خروج از برنامه """
        self.tray_icon.hide()
        sys.exit()

if __name__ == "__main__":
    print("🚀 برنامه در حال اجرا...")
    KhorshidCalendar()
