import subprocess

def open_in_darktable(file_path: str):
    """
    Opens the specified file in the Darktable GUI using macOS 'open'.
    """
    subprocess.run(["open", "-a", "darktable", file_path], check=True)
