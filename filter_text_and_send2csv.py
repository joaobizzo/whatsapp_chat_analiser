import os

chat_txt = 'files/chat.txt'
new_chat_txt = 'files/new_chat.txt'
final_chat_csv = 'files/final_chat.csv'


# Read in the chat.txt file
with open(chat_txt, 'r') as f:
    chat_lines = f.readlines()

# Remove LEFT-TO-RIGHT MARK ([U+200E]) from each line
modified_lines = []
for line in chat_lines:
    modified_line = line.replace('\u200E', '').replace(';', '')  # Remove ; and emojis= U+200E
    # Only append the line if it doesn't start with '[' and neither 'omitid' nor 'ocultad' are in it
    if not line.startswith('[') or 'omitid' in line or 'ocultad' in line:
        continue
    modified_lines.append(modified_line)

# Write the modified lines back to the original file
with open(new_chat_txt, 'w') as f:
    f.writelines(modified_lines)


# Read in the chat.txt file
with open(new_chat_txt, 'r') as f:
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

# Remove '[' and ']' characters from each line
modified_lines = [line.replace('[', '').replace(']', '') for line in modified_lines]

# Change the 11th character to a semicolon
modified_lines = [line[:10] + ';' + line[11:] if len(line) > 10 else line for line in modified_lines]

# Write the modified lines back to the new CSV file
with open(final_chat_csv, 'w') as f:
    f.writelines(modified_lines)
