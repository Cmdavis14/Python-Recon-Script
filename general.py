import os

"""
Creates a directory if it does not exist.
Args:
    directory (str): The path of the directory to be created.
Returns:
    None
"""

# Check if the directory already exists
def create_dir(directory):
    if not os.path.exists(directory):
        # If the directory does not exist, create it recursively
        os.makedirs(directory)



"""
Writes data to a file.
Args:
    path (str): The path of the file to be written.
    data (str): The data to be written to the file.
Returns:
    None
"""

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()



