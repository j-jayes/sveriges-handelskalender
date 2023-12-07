import os
import re
import json
import difflib

def combine_entries_with_similarity(directory, similarity_threshold=0.9):
    combined_entries = []
    entry_end_pattern = r'\d{4}'  # Looking for a year
    pnr_pattern = r'Pnr \d+'
    target_phrase = "Etableringsår"

    # Iterating over each file in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                current_entry = ''
                page_number = file_name.split("_")[-1].split(".")[0]

                for line in lines:
                    # Add line to current entry
                    current_entry += line

                    # Check each word in the line for a close match to "Etableringsår"
                    for word in line.split():
                        if difflib.SequenceMatcher(None, word.lower(), target_phrase.lower()).ratio() > similarity_threshold:
                            # If a close match is found, check if the line ends with a year
                            if re.search(entry_end_pattern, line):
                                # Look ahead to check for 'Pnr'
                                upcoming_text = ''.join(lines[lines.index(line):lines.index(line) + 5])
                                if re.search(pnr_pattern, upcoming_text):
                                    # End of an entry, add to combined entries
                                    combined_entries.append((current_entry.strip(), page_number))
                                    current_entry = ''
                            break

    return combined_entries

def save_entries_as_json(entries, output_directory):
    for index, (entry, page_number) in enumerate(entries):
        file_name = f"1971alfa_page_text_{page_number}_{index}.json"
        file_path = os.path.join(output_directory, file_name)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump({"entry": entry}, json_file, ensure_ascii=False, indent=4)

# Directory where the text files are stored
input_directory = "data/processed/handkal"
output_directory = "data/processed/handkal_json"

# ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Combine entries
combined_entries = combine_entries_with_similarity(input_directory)

# Save entries as JSON
save_entries_as_json(combined_entries, output_directory)
