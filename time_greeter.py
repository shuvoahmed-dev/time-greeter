# A simple time-based greeting script

import time  # Import time module

# Get current time in HH:MM:SS format
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# Print greeting based on current time
if '05:00:00' <= timestamp < '12:00:00':
    print("Good Morning")
elif '12:00:00' <= timestamp < '17:00:00':
    print("Good Afternoon")
elif '17:00:00' <= timestamp < '21:00:00':
    print("Good Evening")
else:
    print("Good Night")
