import os

def remove_br_tags(directory_path):
    """
    Removes all <br/> tags from the files in the specified directory.

    Args:
        directory_path (str): The path to the directory containing the files.

    Returns:
        None
    """
    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    for file_name in files:
        try:
            with open(os.path.join(directory_path, file_name), 'r', encoding='latin-1') as file:
                content = file.read()
                # Replace <br/> tags with empty string
                modified_content = content.replace('<br/>', '')

            with open(os.path.join(directory_path, file_name), 'w', encoding='latin-1') as file:
                file.write(modified_content)
        except UnicodeDecodeError as e:
            print(f"Error decoding file: {file_name}. {str(e)}")

# Call the function
remove_br_tags("data/raw/nuisv")
remove_br_tags("data/raw/handkal")


import os

def clean_text_files_1971(source_dir, target_dir):
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.txt'):
            with open(os.path.join(source_dir, file_name), 'r') as file:
                lines = file.readlines()
            
            # Extract the expected page number from the file name
            expected_page_number = int(file_name.split('_')[-1].split('.')[0]) - 2

            # Check if the last line contains the expected page number
            if lines[-1].strip() == str(expected_page_number):
                lines = lines[:-1]  # Remove the last line

            # Write the cleaned content to a new file in the target directory, using the same filename in the target directory
            with open(os.path.join(target_dir, file_name), 'w') as new_file:
                new_file.writelines(lines)

# Usage
source_directory = "data/raw/handkal/"
target_directory = "data/processed/handkal/"
# ensure that target directory exists
if not os.path.exists(target_directory):
    os.makedirs(target_directory)
clean_text_files_1971(source_directory, target_directory)


