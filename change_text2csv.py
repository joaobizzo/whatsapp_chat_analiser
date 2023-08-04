import os

chat_txt = 'files/new_chat.txt'
new_csv = 'files/new_csv.txt'

# Read in the chat.txt file
with open(chat_txt, 'r') as f:
    chat_lines = f.readlines()

# Replace the third occurrence of ':' with ';'
modified_lines = []
for line in chat_lines:
    # Add a semicolon at the 20th character position
    if len(line) >= 21:
        line = line[:21] + ';' + line[21:]

    parts = line.split(':', 2)  # Split the line into 3 parts at the first two colons
    if len(parts) == 3:  # Ensure there are at least three parts
        modified_line = f"{parts[0]}:{parts[1]}:{parts[2].replace(':', ';', 1)}"  # Replace the third colon with semicolon
        modified_lines.append(modified_line)
    else:
        modified_lines.append(line)  # Keep the line as is if it doesn't have three parts

# Write the modified lines back to the new CSV file
with open(new_csv, 'w') as f:
    f.writelines(modified_lines)
