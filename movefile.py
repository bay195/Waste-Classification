import os
import shutil
import random


def move_random_files(src_directory, percentage):

    # Mendapatkan daftar semua file di dalam direktori sumber
    files = os.listdir(src_directory)

    # Menghitung jumlah file yang akan dipindahkan
    num_files_to_move = int(len(files) * percentage)

    # Memilih file secara acak
    files_to_move = random.sample(files, num_files_to_move)

    for file_name in files_to_move:
        # Path lengkap file sumber dan tujuan
        src_file = os.path.join(src_directory, file_name)
        dest_file = os.path.join(f"{src_directory} val", file_name)

        # Memindahkan file
        shutil.move(src_file, dest_file)
        print(f"Moved: {src_file} to {dest_file}")


# Contoh penggunaan
src_directory = "Wadah Kaca"
percentage = 0.3  # 30%

move_random_files(src_directory, percentage)