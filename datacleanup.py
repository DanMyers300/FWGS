with open("text.txt", "r") as file:
    lines = file.readlines()

# Remove blank lines
lines = filter(lambda x: x.strip(), lines)

# Replace newlines with commas
result = ",".join(map(str.strip, lines))

with open("output.txt", "w") as file:
    file.write(result)
