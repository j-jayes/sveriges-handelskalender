import os
import json

def batch_process_entries_to_text(input_directory, output_directory, batch_size):
    # Read all JSON files and store their contents
    entries = []
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                entry = json.load(json_file)
                # Extract values and concatenate them into a single string
                entry_text = ' '.join(map(str, entry.values()))
                entries.append(entry_text)

    # Group entries into batches and save as text files
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i + batch_size]
        batch_text = '\n\n'.join(batch)  # Separate each entry with two newlines
        batch_file_name = f"batch_{i // batch_size + 1}.txt"
        batch_file_path = os.path.join(output_directory, batch_file_name)
        with open(batch_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(batch_text)

# Example usage
input_directory = "data/processed/handkal_json"  # Directory containing individual JSON files
output_directory = "data/processed/handkal_batches"  # Output directory for batched files
batch_size = 10  # Number of entries per batch file

# ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

batch_process_entries_to_text(input_directory, output_directory, batch_size)
