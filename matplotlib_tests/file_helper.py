import os


def create_plot_dir(dir_name: str):
    if not os.path.exists(dir_name):
        # Create the dir.
        os.makedirs(dir_name)
        print(f"Created output dir `{dir_name}`.")
    elif os.path.isdir(dir_name):
        print(f"Using output dir `{dir_name}`")
    else:
        raise FileExistsError(f"`{dir_name}` exists and is not a directory!")
