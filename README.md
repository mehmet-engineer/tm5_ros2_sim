# TM5-900 Cobot Description, RViz and Gazebo Fortress

TM Description, RViz and Gazebo Fortress package for TM5-900 robot arm in ROS2 Humble.

*Author: Mehmet Kahraman / Date 16.09.2026*

Main Requirements:
--
- Ubuntu 22.04 Jammy
- ROS 2 Humble Desktop
- Ignition Gazebo Fortress

Installation and ROS Packages:
--

Install those ros2 humble packages using apt
```
sudo apt install ros-humble-gz-ros2-control -y
sudo apt install ros-humble-gz-ros2-control-demos -y
sudo apt install ros-humble-ign-ros2-control -y
sudo apt install ros-humble-ros-gz-bridge -y
sudo apt install ros-humble-rqt* -y
sudo apt install ros-humble-joint-state-publisher* -y
sudo apt install ros-humble-launch-param-builder -y
sudo apt install ros-humble-parameter-traits -y
sudo apt install ros-humble-ros2-control -y
sudo apt install ros-humble-ros2-controllers -y
sudo apt install ros-humble-controller-interface -y
sudo apt install ros-humble-joint-trajectory-controller -y
sudo apt install ros-humble-joint-state-broadcaster -y
sudo apt install ros-humble-gripper-controllers -y
sudo apt install ros-humble-xacro -y
sudo apt install ros-humble-realtime-tools -y
sudo apt install ros-humble-hardware-interface -y
sudo apt install ros-humble-control-toolbox -y
sudo apt install ros-humble-filters -y
sudo apt install ros-humble-ros2bag -y
sudo apt install ros-humble-plotjuggler* -y
sudo apt install ros-humble-kdl-parser* -y
```

Clone workspace, build and source it
```
mkdir tm5_ros2_sim_ws
cd tm5_ros2_sim_ws
mkdir src
cd src
git clone https://github.com/mehmet-engineer/tm5_ros2_sim
cd ..
colcon build
source install/setup.bash
```

Running Launches and Nodes:
--

View robot on RViz
```
ros2 launch tm_description view_robot.launch.py
```
![img](assets/rviz.png)

Bringup robot on Gazebo Fortress
```
ros2 launch tm_gazebo tm5-900_gazebo.launch.py
```
![img](assets/gazebo.png)