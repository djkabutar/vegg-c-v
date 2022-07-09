from ast import keyword
import re

from rabin_karp import rabin_karp_string_matching

def get_all_keyword():
    num = [2, 4, 8, 16]
    # Scalar data types
    keywords = ["char", "uchar", "short", "ushort", "int", "unit", "long", "ulong", "float"]

    temp = []
    # Vector data types
    for keyword in keywords:
        for n in num:
            temp.append(keyword + str(n))

    keywords += temp

    # Image specific data types
    keywords += ["image2d_t", "image3d_t", "image1d_buffer_t", "image2d_buffer_t", "image1d_array_t", "image2d_array_t", "sampler_t", "event_t", "queue_t", "kernel_t", "program_t", "device_t", "context_t", "event_info_t", "queue_info_t", "kernel_info_t", "program_info_t", "device_info_t", "context_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t", "kernel_profiling_info_t", "program_profiling_info_t", "device_profiling_info_t", "context_profiling_info_t", "event_profiling_info_t", "queue_profiling_info_t"]

    # Memory objects
    keywords += ["bool", "unsigned", "half", "size_t", "ptrdiff_t", "intptr_t", "uintptr_t", "void", "unsigned int", "unsigned short", "unsigned char", "unsigned long"]

    # Qualifiers
    keywords += ["__global", "__kernel", "__constant", "__local", "__private", "__read_only", "__write_only", "__read_write", "global", "kernel", "private", "constant", "read_only", "write_only", "read_write", "local"]
    return keywords
 

def get_all_indexes(string, pattern):
    indexes = []
    for i in range(len(string) - len(pattern) + 1):
        if rabin_karp_string_matching(string[i:i+len(pattern)], pattern):
            indexes.append(i)
    return indexes

def check_valid_keywords(string, keywords):
    indexes = []
    for keyword in keywords:
        if keyword in string:
            indexes.append(keyword)
    return indexes

