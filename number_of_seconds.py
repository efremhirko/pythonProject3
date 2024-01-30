from datetime import timedelta

# Get the hour, minute, and second values from the user
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

# Define the duration using the user-provided values
duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

# Convert the duration to seconds
total_seconds = duration.total_seconds()

# Print the result with two decimal places
print(f"There are {total_seconds:.2f} seconds in {hours} hours, {minutes} minutes, and {seconds} seconds.")

print("\nstudent name: Ephrem Hirko\n")
print("ID: RU1360/12")