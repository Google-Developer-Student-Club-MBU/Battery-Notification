import psutil
from plyer import notification
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged
    return percent, power_plugged

def notify_low_battery():
    title = "Low Battery Warning"
    message = "Your battery level is low. Please plug in your charger."
    notification.notify(
        title=title,
        message=message,
        timeout=10,  # Display the notification for 10 seconds
    )

def main():
    while True:
        battery_percent, power_plugged = get_battery_status()

        if not power_plugged and battery_percent <= 20:
            notify_low_battery()

        time.sleep(300)  # Check battery status every 5 minutes (adjust as needed)

if __name__ == "__main__":
    main()
