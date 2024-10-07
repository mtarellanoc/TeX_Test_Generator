# !/usr/bin/python3.10
from jupyterlab.browser_check import test_flags

import test_gen
import os

for file in os.listdir('.'):
    if file.endswith('.tex'):

        try:
            with open(file, 'r') as rfile:
                file_body = rfile.read()
                file_body_update = test_gen.update_body(file_body)

                if file_body == file_body_update:

                    test_gen.compile_tex(file)

                else:
                    new_file = f"{file.split('.tex')[0]}--Standalone.tex"
                    with open(new_file, 'w') as wfile:
                        wfile.write(file_body_update)

                    test_gen.compile_tex(new_file)
                    test_gen.df_global.drop(test_gen.df_global.index, inplace=True)
        except:
            continue




