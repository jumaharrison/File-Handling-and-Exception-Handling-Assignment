def read_and_write_file():
    try:
        # Ask user for the filename
        input_filename = input("Harrison_juma:")

        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified content
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content saved to: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: The file cannot be read. Check file permissions.")

# Run the function
read_and_write_file()
