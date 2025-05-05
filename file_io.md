📁 Section 1: Fundamentals of File Handling (Questions 1–15)
What is the correct function to open a file in Python?

a) file.open()

b) open.file()

c) open() ✔

d) File()

Which mode is used to open a file for reading in Python?

a) "r" ✔

b) "w"

c) "a"

d) "x"

What does the "w" mode do when opening a file?

a) Opens a file for reading

b) Opens a file for writing (creates a new file or truncates existing) ✔

c) Opens a file for appending

d) Opens a file for exclusive creation

Which method reads the entire content of a file as a single string?

a) read() ✔

b) readline()

c) readlines()

d) readfile()

What does the readlines() method return?

a) A single string

b) A list of lines ✔

c) A list of characters

d) None of the above

How do you write multiple lines to a file in Python?

a) write_lines()

b) writelines() ✔

c) write()

d) writefile()

Which method is used to read a single line from a file?

a) read()

b) readline() ✔

c) readlines()

d) readone()

What does the "a" mode do when opening a file?

a) Opens a file for reading

b) Opens a file for writing (overwrites existing content)

c) Opens a file for appending (adds to end of file) ✔

d) Opens a file for exclusive creation

Which method is used to close a file in Python?

a) closefile()

b) file.close() ✔

c) close() 

d) endfile()

What is the purpose of the with statement in file handling?

a) It creates a new file

b) It automatically closes the file after the block is executed ✔

c) It appends data to a file

d) It reads the entire file at once

Which method returns the current position of the file pointer?

a) seek()

b) tell() ✔

c) position()

d) pointer()

How do you move the file pointer to the beginning of the file?

a) file.seek(0) ✔

b) file.tell(0)

c) file.move(0)

d) file.start()

What happens if you open a file in "x" mode and the file already exists?

a) The file is opened for writing

b) The file is overwritten

c) A FileExistsError is raised ✔

d) The file is opened for appending

Which method writes a string to a file?

a) write() ✔

b) writeline()

c) writelines()

d) writefile()

What does the "b" character signify in file modes like "rb" or "wb"?

a) Binary mode ✔

b) Buffered mode

c) Backup mode

d) Batch mode

📂 Section 2: Practical File Operations (Questions 16–30)
Which function is used to check if a file exists before opening it?

a) os.path.exists() ✔

b) file.exists() 

c) exists()

d) checkfile()

What is the correct way to open a file for both reading and writing without truncating it?

a) open("file.txt", "w+")

b) open("file.txt", "r+")

c) open("file.txt", "a+") ✔

d) open("file.txt", "rw")

Which method is used to delete a file in Python?

a) os.delete()

b) os.remove() ✔

c) file.delete()

d) remove()

What does the seek() method do?

a) Reads a specific line from the file

b) Moves the file pointer to a specified position ✔

c) Closes the file

d) Deletes the file content

How can you read the first five characters of a file?

a) file.read(5) ✔

b) read(file, 5)

c) file.readline(5)

d) file.readchars(5)

Which method is used to rename a file in Python?

a) os.rename()

b) file.rename() ✔

c) rename.file()

d) os.renameto()

What does the flush() method do?

a) Closes the file

b) Deletes the file content ✔

c) Flushes the internal buffer, writing data to the file

d) Reads the file content

Which method reads all lines of a file into a list?

a) readlines() ✔

b) readall()

c) readlist()

d) read()

What is the default mode when opening a file using open() without specifying a mode?

a) "w"

b) "a"

c) "r" ✔

d) "x"

Which of the following is a valid way to write to a file without overwriting its existing content?

a) Open the file in "w" mode

b) Open the file in "r" mode

c) Open the file in "a" mode ✔

d) Open the file in "x" mode

What will happen if you try to open a non-existent file in read mode?

a) A new file is created

b) The file is opened in write mode instead

c) A FileNotFoundError is raised ✔

d) Nothing happens

Which function is used to copy the contents of one file to another in Python?

a) shutil.copy() ✔

b) os.copy()

c) file.copy()

d) copyfile()

How do you read a file line by line in Python?

a) read_all_lines()

b) file.read_line()

c) for line in file: ✔

d) read_line(file)

Which method is used to write a list of lines to a file?

a) write(list)

b) writelines(list) ✔

c) writelist(list)

d) write_lines(list)

What does the tell() method return?

a) The name of the file

b) The size of the file

c) The current position of the file cursor  ✔

d) The total number of lines in the file

📄 Section 3: Code Analysis and Output Prediction (Questions 31–45)
Given the following code:

python
Copy
Edit
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
What does this code do?

a) Writes data to "data.txt"

b) Reads the entire content of "data.txt" and prints it ✔

c) Appends data to "data.txt"

d) Deletes "data.txt"

What is the output of the following code if "data.txt" contains "Hello World"?

python
Copy
Edit
with open("data.txt", "r") as file:
    print(file.readline())
a) Hello

b) Hello World ✔

c) H

d) Hello World\n

What does the following code do?

python
Copy
Edit
with open("data.txt", "w") as file:
    file.write("Python")
a) Reads "Python" from "data.txt"

b) Appends "Python" to "data.txt"

c) Writes "Python" to "data.txt", overwriting existing content ✔

d) Deletes "data.txt"

What is the output of the following code?

python
Copy
Edit
with open("data.txt", "a") as file:
    file.write("Python")
a) Overwrites "data.txt" with "Python"

b) Appends "Python" to the end of "data.txt" ✔

c) Deletes "data.txt"

d) Reads "Python" from "data.txt"

What does the following code do?

python
Copy
Edit
with open("data.txt", "x") as file:
    file.write("Python")
a) Creates "data.txt" and writes "Python" to it ✔

b) Opens "data.txt" for reading

c) Appends "Python" to "data.txt"

d) Deletes "


📌 Section 4: Error Handling & Best Practices (Questions 36–45)
Which error is raised when trying to read a file that doesn't exist?
a) IOError
b) FileNotFoundError ✔
c) NameError
d) ValueError

Why is using the with statement recommended for file handling?
a) It improves reading speed
b) It ensures the file is closed automatically ✔
c) It renames files automatically
d) It avoids importing modules

Which exception should you catch for general file handling errors?
a) KeyError
b) ValueError
c) Exception ✔
d) TypeError

What will happen if you forget to close a file after writing to it?
a) The file content may not be saved properly ✔
b) The file will be deleted
c) The file opens in read-only mode
d) It automatically closes

Which module provides file utility functions like copying or removing files?
a) fileutils
b) os
c) shutil ✔
d) sys

In file handling, what is a "buffer"?
a) A temporary storage in memory ✔
b) A backup of the file
c) A file read mode
d) A cursor

How would you safely handle a file read with potential error?
a) Just use open()
b) Use a loop
c) Use try-except block ✔
d) No handling needed

Which of these is a good practice when handling files?
a) Never close the file
b) Write large files in binary mode
c) Always hard-code file paths
d) Use with block and handle exceptions  ✔

Which of the following is NOT a valid file mode?
a) "wt" ✔
b) "ra" 
c) "rb"
d) "a+"

What will the code below print?

python
Copy
Edit
with open("data.txt", "w") as f:
    f.write("12345")
print(f.closed)
a) False 
b) True
c) Error ✔
d) None

🔁 Section 5: Understanding File Pointer and Iteration (Questions 46–55)
Which method can you use to rewind the file pointer to the beginning?
a) file.start()
b) file.reset()
c) file.seek(0) ✔
d) file.rewind()

What does this code snippet do?

python
Copy
Edit
file = open("data.txt", "r")
file.seek(5)
print(file.read())
a) Reads first 5 characters ✔
b) Reads whole file
c) Starts reading from character 5 onward
d) Skips the first 5 lines

What is the correct way to loop through lines in a file?
a) while file:
b) file.foreach()
c) for line in file: ✔
d) file.loop()

What does file.closed return?
a) The content of the file
b) True if file is closed ✔
c) False always
d) The file size

After calling file.close(), what happens if you call file.read()?
a) Reads content
b) Raises an exception ✔
c) Returns empty string
d) Closes the file again

Which file mode allows both reading and writing?
a) "r"
b) "a"
c) "r+" ✔
d) "x"

How can you ensure that file is written and saved properly before it’s closed?
a) Use flush() ✔
b) Use tell()
c) Use seek()
d) Use writeall()

How do you open a file to append data without removing existing content?
a) "w"
b) "a" ✔
c) "r"
d) "x"

How many arguments does open() typically accept?
a) 0
b) 1
c) 2 ✔
d) 3

Which method will read the next line during file iteration?
a) nextline()
b) readline()
c) readlines() ✔
d) readnext()

🧠 Section 6: Real-World Task Simulation (Questions 56–60)
You want to store user feedback line by line in a file. Which file mode is best?
a) "r"
b) "w"
c) "a" ✔
d) "x"

You want to preserve existing file content while adding logs. Which mode to use?
a) "r"
b) "w"
c) "a" ✔
d) "w+"

Which type of file mode is ideal for images or videos?
a) Text mode
b) Binary mode ✔
c) Append mode
d) Read mode

You need to extract each sentence from a file into a list. What method do you use?
a) read()
b) readline()
c) readlines() ✔
d) getlines()

In a Python script, what's the best way to avoid errors when opening an external file?
a) Use try-except with open() ✔
b) Open directly without checking
c) Use a global variable
d) Use print statements before opening