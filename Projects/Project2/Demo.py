try:
    file = open('Bill_Split.txt', 'a')
    file.write("\nThis is the code.")
    file.close()
    print("Append mode completed successfully.")
except Exception as e:
    print("Append error:", e)