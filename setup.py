#!/usr/bin/env python

import os

# Get absolute path
path = os.getcwd()
path = path + '/src' + '/model_from_sw'

# Folder paths
urdf_path = path + '/urdf'
launch_path = path + '/launch'


# URDF Folder
# List files in urdf folder
urdf_file = []

# Iterate directory
for files in os.listdir(urdf_path):
    # Check if current path is a file
    if os.path.isfile(os.path.join(urdf_path, files)):
    	# Check for the urdf extension
    	for i in files.split('.'):
    		if i == 'urdf':
        		urdf_file.append(files)

# Remove extension
name = urdf_file[0].split('.urdf')[0]

# Read in the file
with open(urdf_path + '/' + urdf_file[-1], 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(name, 'robot1')

# xacro file
xacro = urdf_file[-1] + '.xacro'

# Write the file out again
with open(urdf_path + '/' + xacro, 'w') as file:
  file.write(filedata)



# Launch Folder
# List files in launch folder
rviz_file = []
gazebo_file = []

# Iterate directory
for files in os.listdir(launch_path):
    # Check if current path is a file
    if os.path.isfile(os.path.join(launch_path, files)):
    	# Check for the urdf extension
    	for i in files.split('.'):
    		if i == 'display':
        		rviz_file.append(files)
	        if i == 'gazebo':
	        		gazebo_file.append(files)



# Read in the file
# RVIZ
with open(launch_path + '/' + rviz_file[-1], 'r') as file :
  filedata = file.read()

# Replace the target string
"""
	TODO:
 			Replace current line ex.: "textfile="$(find urdf_tester)/urdf/ranger_plus_case.asd.urdf.xacro" />"
 			Not just the one in the repository, so the code cant be run multiple times.

"""
#string_to_replace = urdf_file[-1]
string_to_replace = 'ranger.urdf.xacro'
good_string =  xacro

filedata = filedata.replace(string_to_replace, good_string)

# Write the file out again
with open(launch_path + '/' + rviz_file[-1], 'w') as file:
  file.write(filedata)


"""
     NO NEED TO MODIFY GAZEBO LAUNCH FILES LOL

# Gazebo
with open(launch_path + '/' + gazebo_file[-1], 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(name, "robot1")

# Write the file out again
with open(launch_path + '/' + gazebo_file[-1], 'w') as file:
  file.write(filedata)
"""