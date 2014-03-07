#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This is a tool to convert any encoding format to 'utf-8'.
How to use:
$ python zh_to_utf8.py filename.
'''


import os.path
import sys

_input_encoding_type = ''


def zh_to_utf8(input_file_object):
    '''
    Convert strings to utf-8.
    Parameter:
        input_file_object: file object type.
    Return:
        type: string.
        value: the type of encoding.
    '''
    string = input_file_object.read()
    encoding_type = ['gbk', 'utf-8', 'utf-16', 'big5', 'utf-32']
    for t in encoding_type:
        try:
            utf8 = string.decode(t).encode('utf-8')
            global _input_encoding_type
            _input_encoding_type = t
            break
        except UnicodeDecodeError:
            continue
    return utf8


def main():
    input_path = os.path.abspath(sys.argv[1])
    # Output file is created in the same directory as input file.
    dir_path = os.path.dirname(input_path)
    output_path = os.path.join(dir_path, 'output.srt')
    # The open mode must be 'rb', not 'r'.
    # Otherwise the Chinese charactor ':' will cause error while reading.
    input_file_object = open(input_path, 'rb')
    utf8 = zh_to_utf8(input_file_object)
    input_file_object.close()
    output_file_object = open(output_path, 'wb')
    output_file_object.write(utf8)
    output_file_object.close()
    global _input_encoding_type
    print 'Succeefully convert from ' + _input_encoding_type + ' to utf-8.'
    print 'Output file path is ' + output_path
    return


if __name__ == '__main__':
    main()
