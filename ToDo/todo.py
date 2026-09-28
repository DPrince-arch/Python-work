from datetime import datetime
import subprocess

def appSender(script: str):
    subprocess.run(["osascript", "-e", script]) 

def main():
    print("Welcome to the TODO app!")
    start = input("Enter the start date (YYYY-MM-DD HH-MM-SS): ")
    end = input("Enter the end date (YYYY-MM-DD HH-MM-SS): ")
    name = input("Enter event name: ").replace('"', '\\"')

    start_date = datetime.strptime(start, "%Y-%m-%d %H-%M-%S")
    end_date = datetime.strptime(end, "%Y-%m-%d %H-%M-%S")

    if end_date <= start_date:
        raise ValueError("End date must be after start date.")

    start_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
    end_str = end_date.strftime("%Y-%m-%d %H:%M:%S")


    applescript = f'''
tell application "Calendar"
    tell calendar "Home"
        set startDate to date "{start_str}"
        set endDate to date "{end_str}"

        make new event with properties {{summary:"{name}", start date:startDate, end date:endDate}}
    end tell
    
tell application "Clock"
    display notification "Event '{name}' added from {start_str} to {end_str}"
    end tell
end tell
'''
    appSender(applescript)  

if __name__ == "__main__":
    main()
