import os

# Iterate directory
def find_file(folder_name):
    res = []
    if folder_name == None or len(folder_name)==0:
        return res
    for path in os.listdir(folder_name):
        # check if current path is a file
        if os.path.isfile(os.path.join(folder_name, path)):
            if(path.endswith(".c")):
                res.append(os.path.join(folder_name, path))
        else:
            res += find_file(os.path.join(folder_name, path))
    return res

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
dir_path = '../project2/testdir/'
for path in find_file(dir_path):
    print(path)
# expected output
# ../project2/testdir/subdir3/subsubdir1/b.c
# ../project2/testdir/t1.c
# ../project2/testdir/subdir5/a.c
# ../project2/testdir/subdir1/a.c    
# Test Case 2
for path in find_file(""):
    print(path)
# expected output empty list 
# Test Case 3
for path in find_file(None):
    print(path)
# expected output empty list 
