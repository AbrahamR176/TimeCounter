import datetime
import pyperclip
import keyboard
from infi.systray import SysTrayIcon

# Initialize variables
start_time = None
is_running = False
sysicon2 = SysTrayIcon(icon="red.ico", hover_text="None")

# Modifier keys
modifiers = ['Ctrl', 'Shift', 'Alt']

def start_timer():
    global start_time, is_running
    if not is_running:
        start_time = datetime.datetime.now()
        print("Timer started at:", start_time.strftime("%d/%m/%Y %I:%M %p"))
        is_running = True

def stop_timer():
    global start_time, is_running
    if is_running:
        end_time = datetime.datetime.now()
        print("Timer stopped at:", end_time.strftime("%d/%m/%Y %I:%M %p"))
        
        # Calculate elapsed time in minutes
        delta = end_time - start_time
        minutes = round(delta.total_seconds() / 60)
        
        # Format the results
        #result = f"{minutes:.0f} minutes {end_time.strftime("%d/%m/%Y %I:%M %p")}"
        print(minutes)
        
        # Copy to clipboard
        pyperclip.copy(minutes)
        
        is_running = False
        start_time = None

def change_sysincon_color(newicon):
    global sysicon2
    sysicon2.update(icon=newicon)

def change_sysincon_hover(newmsg):
    global sysicon2
    sysicon2.update(hover_text=newmsg)

def on_key_event(event):
    global start_time, file
    key = event.name
    if key == '~' and all(keyboard.is_pressed(mod) for mod in modifiers):
        change_sysincon_color('green.ico')
        start_timer()
        change_sysincon_hover(str(start_time))

    elif key == '|' and all(keyboard.is_pressed(mod) for mod in modifiers):
        change_sysincon_color('red.ico')
        stop_timer()

# Register the event handler for the target keys
keyboard.hook_key('~', on_key_event)
keyboard.hook_key('|', on_key_event)

print("Press Ctrl+S to start the timer and Ctrl+E to stop it.")
print("Results will be copied to clipboard when stopped.")

sysicon2.start()

# Keep the program running
while True:
    keyboard.wait()