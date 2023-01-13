# Initialize variables to track statistics
no_total_runner = 0
no_total_time = 0
fastest_time = float('inf')
fastest_runner = None
slowest_time = 0

# Read input from the user
print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("Let's go!\n")
while True:
    user = input("> ")
    if user == "END":
        break

  # Split the user into the runner number and time
    lines = user.split("::")
    if len(lines) != 2:
        print("Error in data stream. Ignorning. Carry on.")
        continue
    
    runner_number = lines[0]
    time = lines[1]

    
    if not time.isdigit():
        print("Error in data stream. Ignorning. Carry on.")
        continue

    
    time = int(time)
    no_total_runner += 1
    no_total_time += time
    if fastest_time is None or time < fastest_time:
        fastest_time = time
        fastest_runner = runner_number
    if slowest_time is None or time > slowest_time:
        slowest_time = time


# Calculate average time
if no_total_runner == 0:
    print("No data found. Nothing to do. What a pity.")
    sys.exit()
else:
    average_time = no_total_time / no_total_runner

# Convert the times to minutes and seconds
fastest_time_minutes = fastest_time // 60
fastest_time_seconds = fastest_time % 60
slowest_time_minutes = slowest_time // 60
slowest_time_seconds = slowest_time % 60
average_time_minutes = average_time // 60
average_time_seconds = average_time % 60

# Print the results
print(f'Total runners: {no_total_runner}')
print(f'Average time: {average_time_minutes} minutes {average_time_seconds} seconds')
print(f'Fastest time: {fastest_time_minutes} minutes {fastest_time_seconds} seconds')
print(f'Slowest time: {slowest_time_minutes} minutes {slowest_time_seconds} seconds')
print(f'Fastest runner : {fastest_runner}')
