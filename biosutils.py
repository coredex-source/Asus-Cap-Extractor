"""
This library is used to extract the bios data from a .cap file.
It checks a relative address and dumps the bios data.
The data is stored in a .bin file.

Main function:
caputils(capfile, output):
:param capfile: Path to the .cap file to process.
:param output: Path to the output file where the BIOS region will be saved.

"""

# Define known BIOS sizes (in bytes)
KNOWN_BIOS_SIZES = [
    1 * 1024 * 1024,
    2 * 1024 * 1024,
    4 * 1024 * 1024,
    8 * 1024 * 1024,
    16 * 1024 * 1024,
    32 * 1024 * 1024
]

def search_hex_pattern_in_file(file_path, pattern):
    """
    Search for a specific hex pattern in the given file.
    
    :param file_path: Path to the binary file to search in.
    :param pattern: Hexadecimal pattern to search for.
    :return: A tuple containing the extracted data and the starting index, or (None, None) if not found.
    """
    with open(file_path, 'rb') as file:
        content = file.read()

        # Convert the content to a hexadecimal string for easy searching
        hex_content = content.hex()

        # Convert the search pattern to a hexadecimal string
        hex_pattern = pattern.hex()

        # Search for the pattern in the content
        match_index = hex_content.find(hex_pattern)

        if match_index == -1:
            print("Pattern not found in the file.")
            return None, None
        else:
            # Convert match_index back to bytes index
            byte_index = match_index // 2
            print(f"Pattern found at byte index: {byte_index}")

            # Return the content starting from the match
            return content[byte_index:], byte_index


def determine_bios_size(data_length):
    """
    Determine the closest BIOS size based on the length of the data.
    
    :param data_length: Length of the extracted data in bytes.
    :return: Closest known BIOS size.
    """
    # Find the closest known BIOS size
    closest_size = min(KNOWN_BIOS_SIZES, key=lambda x: abs(x - data_length))
    print(f"Closest BIOS size determined: {closest_size / (1024 * 1024)} MB")
    return closest_size


def extract_bios_region(extracted_data):
    """
    Extract the BIOS region from the extracted data, based on a determined size.
    
    :param extracted_data: Data extracted from the binary file.
    :return: Truncated BIOS region.
    """
    # Calculate the length of the extracted data
    data_length = len(extracted_data)

    # Determine the closest BIOS size
    bios_size = determine_bios_size(data_length)

    # Truncate the extracted data to the determined BIOS size
    bios_region = extracted_data[:bios_size]

    return bios_region


def caputils(capfile, output):
    """
    Process the given capture file (capfile), extract the BIOS region, and save it to the output file.
    
    :param capfile: Path to the .cap file to process.
    :param output: Path to the output file where the BIOS region will be saved.
    """
    # Define the hex pattern you are searching for
    hex_pattern = bytes([0x02, 0x00, 0x00, 0x83])

    # Search for the hex pattern and get the data
    extracted_data, start_index = search_hex_pattern_in_file(capfile, hex_pattern)

    if extracted_data:
        # Extract the BIOS region using the dynamically found size
        bios_region = extract_bios_region(extracted_data)

        # Save the extracted BIOS region to a new file
        with open(output, 'wb') as output_file:
            output_file.write(bios_region)
        print(f"Extracted BIOS region saved as '{output}'.")
    else:
        print("No data extracted. Pattern not found.")
