import os
import pickle

def export_as_pickle(obj, folder_name, file_name):
    """
    Serializes a Python object and saves it as a .pkl file in a specified folder.

    Parameters:
        obj: The Python object to be serialized.
        folder_name (str): Name of the folder where pkl file will be saved.
        file_name (str): Name of the file. Must end with '.pkl' extension.

    Returns:
        None

    Raises:
        ValueError: If file_name does not end with '.pkl' extension.
        FileNotFoundError: If folder does not exist.
    """
    try:
        if not file_name.endswith('.pkl'):
            raise ValueError("File name must end with '.pkl' extension.")
        
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        folder_path = os.path.join(parent_dir, folder_name)
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Folder '{folder_name}' does not exist.")
        
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        print(f"Object saved as '{file_name}' successfully.")
    except (ValueError, FileNotFoundError) as e:
        print(e)