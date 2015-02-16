# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))

# Get the number of days 
days = (total_seconds // 86400) % 86400

# Get the number of remaining hours.
hours = (total_seconds % 86400) // 3600
         
# Get the number of remaining minutes.
minutes = (total_seconds // 60) % 60

# Get the number of remaining seconds.
seconds = total_seconds % 60

# Display the results.

if total_seconds >= 86400:
    print('Days:', days)
else:
    print(' ')

if total_seconds >= 3600:
    print('Hours:', hours)
else:
    print(' ')
    
if total_seconds >= 60:
    print('Minutes:', minutes)
else:
    print(' ')

if seconds > 0:
    print('Seconds:', seconds)
else:
    print(' ')

