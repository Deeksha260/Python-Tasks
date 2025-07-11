file_name = "output.txt"
user_input = input("Enter text to write to the file: ")

with open(file_name, "w") as file:
    file.write(user_input + "\n")

print("Data successfully written to", file_name)


append_text = input("Enter additional text to append: ")

with open(file_name, "a") as file:
    file.write(append_text + "\n")

print("Data successfully appended.")

print("\nFinal content of", file_name + ":")
with open(file_name, "r") as file:
    print(file.read())