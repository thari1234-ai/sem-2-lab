with open("C:\\Users\\user\\OneDrive\\Desktop\\skibidi_input.txt") as inline, open("C:\\Users\\user\\OneDrive\\Desktop\\skibidi_output.txt", "w") as outline:
    lines = inline.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            outline.write(lines[i])  # Write even-indexed lines to the output file
            print(lines[i].strip())  # Print the line without extra whitespace