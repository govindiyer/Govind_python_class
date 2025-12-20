def append():
    try:
        file = open('Filehandle.txt', 'a')
        file.write("\nI am adding second line.")
        file.close()
        print("Append mode completed successfully.")


    except Exception as e:
        print("Append error:", e)
def read():
    try:
        file = open('Filehandle.txt', 'r')
        print(file.read())
        file.close()
    except Exception as e:
        print("Append error:", e)
append()
# read()