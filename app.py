# Python script to make each of my day folders in my week folder

import os

required_paths = ['day1', 'day2', 'day3', 'day4', 'day5']

try:
    for path in required_paths:
        os.mkdir(path)
except OSError:
    print('Creation of directory has failed')
else:
    print ('Succesfully created the directorys')