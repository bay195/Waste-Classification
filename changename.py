import os


def rename_files(directory,name):
    # Mendapatkan daftar semua file di dalam direktori
    files = os.listdir(directory)

    # Mengurutkan file berdasarkan nama asli untuk menjaga urutan
    files.sort()

    # Mengubah nama file menjadi file1, file2, dan seterusnya
    for index, filename in enumerate(files):
        # Mendapatkan ekstensi file
        file_extension = os.path.splitext(filename)[1]

        # Membuat nama baru
        new_name = f"{name}{index + 1}.jpg"

        # Mendapatkan path lengkap file lama dan file baru
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Mengganti nama file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")


# Contoh penggunaan
directory_path = "Test/Kardus"
rename_files(directory_path, "KardusTest")