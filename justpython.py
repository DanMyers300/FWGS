with open('test.txt', 'r') as f:
    for line in f:
        # Split the line into a list of values
        values = line.strip().split(',')

        # Process the values as needed
        print(values)
