# battery_notifier
Here is a little battery notifier script that I just made.
## Usage 
1. copy the python file content to a file on your system
2. make it executable -sudo chmod +x file_path.py
3. execute it on every x session by adding it to .xinitrc or window manager config.
## Notes: 
1. I tried to make it the most power saver by adding a sleep time for the program, if its not working properly for you, you can change the sleep time i the python file.
2. you may need to install python-dbus using your package manager to give the plyer library the ability to make system notifications.
