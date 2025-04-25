import os

def get_path(folder_name, file_name):
    """
    Returns the full path of a specified file from a given folder.

    Parameters:
        folder_name (str): Name of the folder containing the file.
        file_name (str): Name of the file to load from the folder.

    Returns:
        str: Full path to the file if both the folder and file are found.

    Raises:
        FileNotFoundError: If folder does not exist or if the file is not found within the folder.

    Example:
        >>> get_path('images', 'logo.png')
        '/path/to/current/directory/images/logo.png'
    """
    current_dir = os.getcwd()
    folder_path = os.path.join(current_dir, folder_name)
    file_path = os.path.join(folder_path, file_name)

    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder '{folder_name}' does not exist.")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found in folder '{folder_name}'.")

    return file_path