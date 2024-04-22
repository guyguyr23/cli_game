# Import the libraries inputimeout, TimeoutOccurred 
from inputimeout import inputimeout 

# Try block of code 
# and handle errors 
try: 
	time_over = inputimeout(prompt='Name your best friend:', timeout=3) 
	print(time_over)
except Exception: 
	time_over = 'Your time is over!'
	print(time_over) 

# Print the statement on timeoutprint(time_over) 
