import igl 
import glob

import sys
import os.path as osp 
import os
import re
arguments = sys.argv[1:-1]
output_dir = sys.argv[-1]
file_ext_filter = ['obj', 'off']
ply_ext = 'ply'
regex_string = '('+'|'.join(file_ext_filter) + ')$'

def convert(arguments, output_dir='.'):
    for name in arguments:
        if not osp.exists(name):
            continue

        elif osp.isdir(name):
            convert(arguments=glob.glob(osp.join(name, "**")), output_dir = osp.join(output_dir, name))
        
        elif osp.isfile(name) and re.search(regex_string, name): # if off or obj file. will be true.
            v, f = igl.read_triangle_mesh(name)
            if not osp.exists(output_dir):
                os.makedirs(output_dir)
            name = osp.basename(name)
            name = re.sub(regex_string, ply_ext, name)
            igl.write_triangle_mesh(osp.join(output_dir, name), v, f)


        

    

if __name__ =="__main__":
    if len(sys.argv) == 1 : 
        print("usage : python obj2ply dir_or_file1 ... [dir_or_file_N]  [ output_dir ]")
        print("dir_or_file : obj or off file")
        print("output_dir : default current working directory")

    print("input args : ", arguments)
    print("output dir", output_dir)
    convert(arguments, output_dir)
    print("end ...")

