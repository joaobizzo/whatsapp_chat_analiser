import os


chat_txt = 'files/chat.txt'
new_chat_txt = 'files/new_chat.txt'

# Read in the chat.txt file
with open(chat_txt, 'r') as f:
    chat_lines = f.readlines()

# Remove LEFT-TO-RIGHT MARK ([U+200E]) from each line
modified_lines = []
for line in chat_lines:
    modified_line = line.replace('\u200E', '').replace(';', '')  # Remove ; and emojis= U+200E
    modified_lines.append(modified_line)

# Write the modified lines back to the original file
with open(new_chat_txt, 'w') as f:
    f.writelines(modified_lines)
