import os
from shutil import copyfile


def collect_html(src_path, dst_path):
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if os.path.splitext(file)[1] in ['.html', '.htm']:
                is_unique, dst_file, i = False, file, 1
                while not is_unique:
                    if os.path.exists(os.path.join(dst_path, dst_file)):
                        dst_file = os.path.splitext(file)[0] + f'({i})' + os.path.splitext(file)[1]
                        i = i + 1
                        continue
                    is_unique = True

                try:
                    copyfile(os.path.join(root, file), os.path.join(dst_path, dst_file))
                except Exception as e:
                    print(e)


# note: if destination folder placed in source hierarchy than it content will copy again too
collect_html('./my_project', './my_project/templates')
