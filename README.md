# gopher_robot_version #

Create a file containing the name and version of various ROS and system packages.

The following paths are used for ROS:
* /opt/yujin/amd64/indigo-devel
* /opt/yujin/amd64/indigo-stable
* /opt/ros


### Install ###
~~~~
(sudo) pip install gopher_robot_version
~~~~

### Usage ###
~~~~
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --verbose             Show what is actually written to file
  -o OUTPUT, --output OUTPUT
                        Allows to specify an output filepath for the data
~~~~

### TODO ###
* Make the path configurable
* Improve code with "try"
