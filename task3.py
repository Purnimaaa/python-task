import sys
import random

def generate_email(name):
  # Split the name into first name and Last_name
  parts = name.split(',')
  Last_name = parts[0]
  first_names = parts[1].strip()

  # Generate the initials
  initials = '.'.join([n[0] for n in first_names.split()]).lower()

  # Generate the random numbers
  numbers = ''.join([str(random.randint(0, 9)) for i in range(4)])

  # Remove any non-alphabetic characters from the Last_name
  Last_name = ''.join([c for c in Last_name if c.isalpha()]).lower()

  # Return the email
  return f'{initials}.{Last_name}{numbers}@poppleton.ac.uk'

# Check that a file name was provided
if len(sys.argv) < 2: #sys argv ma duita(file .py .txt) argument pass garxeko hunxau
  print("Error: Missing command-line argument.")
  sys.exit(1)

# Open the input file
# This code opens the file specified on the command line and reads all of the lines into a list.
try:
  with open(sys.argv[1], 'r') as f: #
    lines = f.readlines()
except:
  print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
  sys.exit(1)

# Open the output file
try:
  with open('abc.txt', 'w') as f:
    # Generate the emails
    for line in lines:
      parts = line.strip().split()
      student_id = parts[0]
      name = ' '.join(parts[1:])
      email = generate_email(name)
      f.write(f"{student_id} {email}\n")
except:
  print("Error: Cannot open abc.txt for writing. Sorry about that.")
  sys.exit(1)
