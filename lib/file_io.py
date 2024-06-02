# lib/file_io.py

def write_file(file_name, file_content):
    """Write content to a file."""
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to a file."""
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    """Read content from a file."""
    with open(f"{file_name}.txt", encoding='utf-8') as file:
        return file.read()
