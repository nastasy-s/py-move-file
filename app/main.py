import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: mv source destination"
        )

    _, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    if not os.path.isfile(source):
        raise ValueError(f"Source '{source}' must be a file")

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.copy2(source, destination)

    os.remove(source)
