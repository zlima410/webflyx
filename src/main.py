import os, shutil

def copy_from_src_to_dest(src_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)


if __name__ == "__main__":
    copy_from_src_to_dest("src", "public")