import os

def rename_files(directory_path):
    # ตรวจสอบว่า directory นี้มีอยู่จริงหรือไม่
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    # รวบรวมไฟล์ทั้งหมดใน directory
    dir_list = os.listdir(directory_path)

    for i, filename in enumerate(dir_list, start=1):
        # แยกชื่อและนามสกุลของไฟล์
        name, ext = os.path.splitext(filename)

        # สร้างชื่อใหม่
        new_name = f"{i:03d}{ext}"

        # สร้างเส้นทางเข้าไฟล์เดิมและเส้นทางไปยังไฟล์ใหม่
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)

        # Rename ไฟล์
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} to {new_name}")

# ตัวอย่างการใช้งาน
directory_path = "C:\\Users\\forth\\OneDrive\\Desktop\\Data Structure and Algorithms\\New folder"
rename_files(directory_path)