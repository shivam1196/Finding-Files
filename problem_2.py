import os


def find_files(suffix, path):
    all_paths = []

    try:
        list_of_dir = os.listdir(path)
    except FileNotFoundError:
        return "Path does not exist"

    if len(suffix) is 0 or not "." in suffix:
        return "Please provide a valid suffix"

    for item in list_of_dir:
        _new_path = path + "/" + item
        if item.endswith(suffix):
            all_paths.append(_new_path)

        elif not (os.path.isfile(_new_path)):
            all_paths = all_paths + find_files(suffix, _new_path)

    return all_paths


if __name__ == "__main__":
    print(find_files(".c","testdir"))  # ['testdir/subdir5/a.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir1/a.c']
    print(find_files(".c", "testdir/subdir1"))  # ['testdir/subdir1/a.c']
    print(find_files(".c", "testdir/subdir2"))  # []
    print(find_files(".c", "testdir/subdir3"))  # ['testdir/subdir3/subsubdir1/b.c']
    print(find_files(".c", "testdir/subdir4"))  # []
    print(find_files(".c", "testdir/subdir5"))  # ['testdir/subdir5/a.c']
    print(find_files("c", "testdir"))  # Please provide a valid suffix
    print(find_files("", "testdir"))  # Please provide a valid suffix
    print(find_files(".c", "testing"))  # Path does not exist
