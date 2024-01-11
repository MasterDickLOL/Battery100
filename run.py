import subprocess
import time

def check_battery_level():
    su_command = "su -c 'dumpsys battery | grep level'"
    result = subprocess.run(su_command, shell=True, capture_output=True, text=True)
    
    try:
        percent = int(result.stdout.strip().split(":")[1])
        return percent
    except (IndexError, ValueError):
        return None

def play_alarm():
    subprocess.run(["mpv", "alarm.mp3"])

def main():
    while True:
        battery_level = check_battery_level()

        if battery_level is not None:
            if battery_level >= 100:
                print("Battery is at 100%. Playing alarm.")
                play_alarm()
                break
            elif battery_level >= 95:
                print("Battery is at {}%. Checking every minute.".format(battery_level))
                time.sleep(60)
            elif battery_level >= 90:
                print("Battery is at {}%. Checking every 5 minutes.".format(battery_level))
                time.sleep(300)
            else:
                print("Battery is at {}%. Checking every 10 minutes.".format(battery_level))
                time.sleep(600)
        else:
            print("Error retrieving battery level. Exiting.")
            break

if __name__ == "__main__":
    main()
    #play_alarm()