def modifier(input_file,output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()

        modified = content.replace("coding","PLP")

        with open(output_file, "w") as file:
            file.write(modified)

        print(f"File '{input_file}' has been modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

input_file = "week4input.txt"
output_file = "week4output.txt"

modifier(input_file,output_file)