# 1. Create a text file named sample.txt and write a user provided sentence into it.
# 2. Open an existing file and print its entire content.
# 3. Read and display only the first five characters from a file.
# 4. Read and display the last five characters of a file without using negative indexing.
# 5. Count and print the total number of characters in a file.
# 6. Count and print the total number of words in a file.
# 7. Count and print the total number of lines in a file.
# 8. Read a file line by line and print each line with its line number.
# 9. Append a new line of text to an existing file.
# 10. Completely overwrite the content of a file with new text.
# 11. Check if a file exists before opening; show a message if it does not.
# 12. Delete a file after confirming its existence.
# 13. Display only the first line and the last line of a file.
# 14. Copy the entire content of one file to another new file.
# 15. Merge the contents of two files into a third file.
# 16. Read a file and display only the lines containing a specific user provided word.
# 17. Read numeric values from a file and print their sum.
# 18. Find and print the longest word in a file.
# 19. Remove all blank lines from a file and save the result to a new file.
# 20. Reverse the entire content of a file character by character and write to another file.
# 21. Print characters at even positions from a file.
# 22. Print every alternate line from a file.
# 23. Count and display the frequency of each character in a file.
# 24. Count and display the frequency of each word in a file.
# 25. Identify and print the most repeated word in a file.
# 26. Print only the uppercase letters found in a file.
# 27. Print only alphabetic characters from a file while ignoring digits and punctuation.
# 28. Split the lines of a file into even lined and odd lined output files.
# 29. Read a comma separated file and print each column separately.
# 30. Implement a simple logger that appends a timestamped message to a file each time the program runs.
# 31. Count and print the number of vowels and consonants in a file.
# 32. Replace all occurrences of a specific word with another word and save it to a new file.
# 33. Read a file and convert all text to uppercase and save it.
# 34. Extract all unique words from a file and print them alphabetically.
# 35. Count how many times a user specified word appears in a file.
# 36. Count the total number of digits present in a file.
# 37. Write numbers from 1 to 100 into a file with one number per line.
# 38. Read a file and print it in reverse order line by line.
# 39. Create ten files named file1.txt to file10.txt and write sample content in each.
# 40. Read a binary file such as an image and create its exact copy.
# 41. Count the number of commented lines in a Python source file.
# 42. Encrypt the content of a file using a simple Caesar cipher with shift three and save it.
# 43. Search for email addresses inside a file and print them.
# 44. Read a file containing one word per line and sort all words alphabetically into a new file.
# 45. Find and print the shortest and longest lines in a file.
# 46. Create a simple to do list program that loads tasks from a file and saves them back.
# 47. Count occurrences of each file extension from a directory listing stored in a file.
# 48. Remove duplicate lines from a file while keeping their original order.
# 49. Write the current system date and time to a file every time the script runs without removing previous data.
# 50. Read a large file line by line and count how many lines contain the word error.
# 51. Use the r plus mode to read the first line and then write additional content to the same file.
# 52. Use the seek function to move the cursor to a specific byte location and read from there.
# 53. Read a very large file in chunks of 1024 bytes and count how many chunks were processed.
# 54. Wrap file access code in try except blocks to catch file related errors.
# 55. List all files in a directory and write their names and sizes to a file.
# 56. Read a JSON file, modify some values, and save the updated JSON back.
# 57. Read a configuration file using configparser and display all sections and key value pairs.
# 58. Use the pathlib module to create directories and files programmatically.
# 59. Create a temporary file using the tempfile module, write data, read it back, and allow it to delete automatically.
# 60. Create a backup of a file before modifying it and then overwrite the original file safely.

#A1
# try:
#     file=open('myTextFile.txt','a')
#     file.write("\n55. List all files in a directory and write their names and sizes to a file.")   
#     file.write("\n56.  Read a JSON file, modify some values, and save the updated JSON back.")
#     file.write("\n123456789")
#     file.write("\n,,,,,,,,,,,,,,,,,,,,,, ,,,,,,,,,,,,,, ,,,,,,,,,,,,,,")
#     file.close()
#     print("Append Mode completed successfully")
# except Exception as e:
#     print("write error-",e)




#A2
# try:
#     file=open('sample.txt','r')
#     print(file.read())
#     file.close()
#     print('Reads mode completed')
# except Exception as e:
#     print('read error-',e)




#A3
# try:
#     file=open('sample.txt','r')
#     print(file.read(5))
#     file.close()
#     print('Read mode completed')
# except Exception as e:
#     print('Read error-',e)







#A4
# with open("sample.txt", "r", encoding="utf8") as f:
#     text = f.read()
#     print(text[len(text) - 5:])












#A5
# try:
#     file=open('sample.txt','r')
#     print(len(file.read()))
#     file.close()
#     print('Read mode completed')
# except Exception as e:
#     print('Read error-',e)






#A6
#Count and print the total number of words in a file
# try:
#     file=open('sample.txt','r'):
#         x=file.read()
#         y=x.split()
#         z=len(y)
#     print(z)
# except FileNotFoundError:
#     print(f"Error: The file '{file}' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# #A7
# 7. .Count and print the total number of lines in a file
# file1='sample.txt'
# count=0
# try:
#     with open(file1,'r')as file:
#       for line in file:
#          count+=1
#     print(count)
# except FileNotFoundError:
#     print(f"Error: The file '{file}' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

    




 

#A8
# 8. Read a file line by line and print each line with its line number.
# try:
#     with open('sample.txt', 'r') as file:
#         for line_number, line in enumerate(file, start=1):
#             print(f"Line {line_number}: {line.strip()}")
# except FileNotFoundError:
#     print(f"Error: The file 'sample.txt' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")









# 9. Append a new line of text to an existing file
# try:
#     file=open('sample.txt','a')
#     file.write("\nHello, my name is Govind")
#     file.close()
#     print("append mode completed")
# except Exception as e:
#     print(f"Read Error: {e}")











# 10. Completely overwrite the content of a file with new text.
# file_path = "example_file.txt"
# new_text = "This new text completely replaces the old content of the file.\nIt even supports multiple lines."
# with open(file_path, 'w') as file:
#     file.write(new_text)
# print(f"Content of '{file_path}' has been overwritten.")




# 11. Check if a file exists before opening; show a message if it does not.
# import os
# filename = "sample.txt"
# if os.path.exists(filename):
#     print(f"The file '{filename}' exists. Opening it now...")
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             print("File content:")
#             print(content)
#     except IOError as e:
#         print(f"An error occurred while opening the file: {e}")
# else:
#     print(f"Error: The file '{filename}' does not exist.")
# print("Script finished.")






# 12. Delete a file after confirming its existence.
# import os
# filename = "sample.txt"
# if os.path.exists(filename):
#     os.remove(filename)
#     print("Deleting completed")
# else:
#     print(f"Error: The file '{filename}' does not exist.")




# 13. Display only the first line and the last line of a file.
# try:
#     file=open('myTextFile.txt','r')
#     file.seek(0)
#     print("First Line: ",file.readlines()[0])
#     print(file.readlines()[len(file.readlines())-1])
# except FileNotFoundError:
#     print('File does not exist')


# 14. Copy the entire content of one file to another new file.
# try:
#     with open('Filehandle .txt','r') as copiedfile:
#         content=copiedfile.read()
#     with open('myTextfile.txt','w') as writtenfile:
#         writtenfile.write(content)
#     print("COPIED MODE SUCCESSFULLY COMPLETED")
# except FileNotFoundError:
#     print('File does not exist')

# 15. Merge the contents of two files into a third file.
# with open('myTextFile.txt','w') as mergedfile:
#     with open('myTextFile2.txt','r') as file1:
#         mergedfile.write(file1.read())
#     with open('Filehandle.txt','r') as file2:
#         mergedfile.write(file2.read())

#16.Read a file and display only the lines containing a specific user provided word.
# word=input("Enter The Word:  ")
# try:
#     with open('myTextFile.txt','r') as file:
#         for line in file:
#             if word.lower() in line.lower():
#                 print(line.strip())
# except FileNotFoundError:
#     print('File does not exist')

#17.Read numeric values from a file and print their sum.
# totalsum=0
# with open('myTextFile.txt','r') as file:
#     for line in file:
#         try:
#             number=float(line.strip())
#             totalsum+=number
#         except ValueError:
#             print("Skipping line",line.strip())
# print(totalsum)

#18.Find and print the longest word in a file
# longest=""
# with open('myTextFile.txt')as file:
#     words=file.read().split()
#     for i in words:
#         if len(i)>len(longest):
#             longest=i
# print(longest)
# print(len(longest))

# 19. Remove all blank lines from a file and save the result to a new file.
# fulllines=[]
# with open('Filehandle.txt','r')as file1:
#     for line in file1:
#         if line.strip():
#             fulllines.append(line)
# with open('myTextFile.txt','w')as file2:
#     file2.writelines(fulllines)
# print(file2)

# 20. Reverse the entire content of a file character by character and write to another file.
# with open('Filehandle.txt','r')as file1:
#     content=file1.read()
# reversed=content[::-1]
# with open('myTextFile.txt','w')as file2:
#     file2.write(reversed)
# print(file2)

# 21. Print characters at even positions from a file.
# try:
#     file=open('myTextFile.txt','r')
#     index=0
#     while True:
#         character=file.read(1)
#         if not character:
#             break
#         if index%2==0:
#             print(character,end=" ")
#         index+=1
#     file.close
#     print()
# except FileNotFoundError:
#      print("File not Found")


# 22. Print every alternate line from a file.
# with open('myTextFile.txt','r') as file:
#     lines=file.readlines()
#     for line in lines[0::2]:
#         print(line.strip)

# 23. Count and display the frequency of each character in a file.

# 24. Count and display the frequency of each word in a file.


# 25. Identify and print the most repeated word in a file.

# 26. Print only the uppercase letters found in a file.
# try:
#     with open('myTextFile.txt','r')as file:
#         content=file.read()
#         for char in content:
#             if char.isupper():
#                 print(char,end=" ")
# except FileNotFoundError:
#     print("File not found")
                      


# 27. Print only alphabetic characters from a file while ignoring digits and punctuation.
# filtered_content=""
# try:
#     with open('myTextFIle.txt','r') as file:
#         content=file.read()
#         for char in content:
#             if char.isalpha():
#                 filtered_content+=char
#     print(filtered_content)
# except FileNotFoundError:
#     print("File was not found")
# except Exception as e:
#     print("An unexpected error occured" ,e, "Please try again") 

# 28. Split the lines of a file into even lined and odd lined output files.
# with open('myTextFile.txt','r') as in_file, open('Filehandle.txt','w') as odd_file, open('myTextFile2.txt','w') as even_file:
#     count=1
#     for line in in_file:
#         if count%2 != 0:
#             odd_file.write(line)
#         else:
#             even_file.write(line)

# 29. Read a comma separated file and print each column separately.
 
# import csv
# import io
# file_content = """Name,Age,City
# Alice,30,New York
# Bob,25,Los Angeles
# Charlie,35,Chicago"""
# f = io.StringIO(file_content)
# reader = csv.reader(f)
# try:
#     header = next(reader)
# except StopIteration:
#     print("File is empty.")
#     exit()
# columns = [[] for _ in header]

# for row in reader:
#     for i, field in enumerate(row):
#         columns[i].append(field)
# for i, col in enumerate(columns):
#     print(f"Column '{header[i]}':")
#     print(col)
#     print("-" * 20)
# f.close()


# 30. Implement a simple logger that appends a timestamped message to a file each time the program runs.

# 31. Count and print the number of vowels and consonants in a file.
# vowels_count=0
# consonants_count=0
# vowels='aeiouAEIOU'
# consonants='bcdfghjklmnpqrstvwxysBCDFGHJKLMNPQRSTVWXYZ'
# try:
#     with open('myTextFile.txt','r') as file:
#         file_content=file.read()
#         for char in file_content:
#             if char in vowels:
#                 vowels_count+=1
#             elif char in consonants:
#                 consonants_count+=1
#     print(vowels_count)
#     print(consonants_count)
# except FileNotFoundError:
#     print(f"Error: The file was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# 32. Replace all occurrences of a specific word with another word and save it to a new file.

# 33. Read a file and convert all text to uppercase and save it.

# try:
#     with open('myTextFile.txt','r') as file_read:
#         content=file_read.read()
#     upper_content=content.upper()
#     with open('myTextFile2.txt', 'w') as file_write:
#         file_write.write(upper_content)
#     with open('myTextFile2.txt', 'r') as file_verify:
#         print("\nContent of the output file:")
#         print(file_verify.read())

# except FileNotFoundError:
#     print(f"Error: file was not found.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")

# 34. Extract all unique words from a file and print them alphabetically.

# 35. Count how many times a user specified word appears in a file.

# 36. Count the total number of digits present in a file.

# 37. Write numbers from 1 to 100 into a file with one number per line.

# 38. Read a file and print it in reverse order line by line.

# 39. Create ten files named file1.txt to file10.txt and write sample content in each.

# 40. Read a binary file such as an image and create its exact copy.