# Check if two PDF documents are identical with Python
import hashlib
import os
import argparse

def hash_file(filename, algorithm= "sha256"):
    h = hashlib.new(algorithm)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): 
            h.update(chunk)
    return h.hexdigest()

print(hash_file("test.pdf"))

def compare_files(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    return hash1 == hash2

print(compare_files("test.pdf" , "test2.pdf"))
print(compare_files("test.pdf",  "test3.pdf"))