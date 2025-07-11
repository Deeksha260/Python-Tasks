def read_file(file_name):
    try:

        with open(file_name, 'r') as file:

            print("File content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:

        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:

        print(f"An unexpected error occurred: {e}")

read_file("sample.txt")