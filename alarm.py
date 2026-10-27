import datetime
import time


def set_alarm():
    print("--- Python Alarm Clock ---")
    while True:
        alarm_time_input = input(
            "Enter alarm time in 24-hour format (HH:MM:SS): "
        )
        try:
            datetime.datetime.strptime(alarm_time_input, "%H:%M:%S")
            break
        except ValueError:
            print("❌ Invalid format! Please use HH:MM:SS (e.g., 07:30:00).")

    print(f"\n🔔 Alarm successfully set for {alarm_time_input}")
    print("Clock is running... Press Ctrl+C to cancel at any time.\n")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_input:
            print(f"\n🚨 [{current_time}] WAKE UP! Time to start your day! 🚨")
            try:
                import winsound

                winsound.Beep(1000, 3000)
            except ImportError:
                print("\a" * 5)
                print("🎵 Sound playback completed.")
            break
        time.sleep(1)


if __name__ == "__main__":
    try:
        set_alarm()
    except KeyboardInterrupt:
        print("\n👋 Alarm cancelled. Goodbye!")
