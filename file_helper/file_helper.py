import os


def clear_folder(folder_path):
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f'Can not delete {file_path} chief :(. Error: {e}')
    else:
        print(f'Folder {folder_path} does not exists.')


def get_all_files(folder_path):
    all_files = []
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                all_files.append(file_path)

    return all_files


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
