# Write a program to create file, write the content
# and display the contents of the file with each line
# preceded with a line number (start with 1) followed by a colon.
print('Entered the content in the file')
print('and "end" signal the end of content')
try:
    fp = open('sample.txt', 'w')
    line = ''
    while line != 'end':
        line = input();
    fp.write(line + '\n')
    fp.close()
except IOError:
    print('There is an error in file operations')
    sys.exit()

print('Display the content of file')
try:
    fp = open('sample.txt', 'r')
    line = fp.readline()
    line_no = 1;
    while line != '':
        print(line_no, ':', line)
    line_no = line_no + 1
    line = fp.readline()
    fp.close()
except IOError:
    print('There is an error in file operations')
    sys.exit()
