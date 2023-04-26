# create an empty dictionary to store the data
data = {}

# open the text file for reading
with open("test.txt", "r") as file:
    # read each line in the file
    for line in file:
        # remove any leading or trailing whitespace from the line
        line = line.strip()

        # check if the line contains a colon
        if ":" in line:
            # split the line into key-value pairs
            key, value = line.split(":", 1)
            # remove any leading or trailing whitespace from the key and value
            key = key.strip()
            value = value.strip()
            # add the key-value pair to the dictionary
            data[key] = value

# print the dictionary as a table
for key, value in data.items():
    print("{:<30} {}".format(key, value))
