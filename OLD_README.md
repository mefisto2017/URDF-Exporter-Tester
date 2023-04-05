### Old Method

- Rename the urdf file in the folder urdf as *name*.urdf.xacro


- Edit the urdf file as:
  - Change line 6 to the name of your robot *name*
  - Change every filename="" line to include the urdf_tester

![This is an image](images/urdf.png)

<br />

- Edit the display file in the launch folder
  - Change line 6 to *name*.urdf.xacro

![This is an image](images/display_launch.png)

<br />

- Edit the gazebo file in the launch folder
  - Change line 16 to -model *name*
  
![This is an image](images/gazebo_launch.png)
