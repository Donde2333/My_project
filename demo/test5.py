sent_message = 'Hey there! This is a secret message.'
file_name = "sent_message.txt"

with open(file_name, 'w') as file:
  file.write(sent_message)

with open(file_name, 'r') as file:
  file.seek(0)
  file.truncate(10)
  Content = file.read()
  print(Content)

