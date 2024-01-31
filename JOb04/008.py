import os

def rename_files(directory_path, file_extension):
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

    files.sort()

    count = 1

    for old_name in files:
        new_name = f"{count:03d}{file_extension}"

        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        os.rename(old_path, new_path)

        count += 1

    print(f"Rename completed for {len(files)} files.")

directory_path = "เส้นทางไปยัง Directory ที่ต้องการ"
file_extension = ".jpg"
rename_files(directory_path, file_extension)