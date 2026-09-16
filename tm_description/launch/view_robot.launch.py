import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import (
    Command,
    FindExecutable,
    PathJoinSubstitution,
)
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    # Robot Description Configuration
    robot_model_path = 'urdf'
    robot_model_file = 'tm5-900.xacro'

    # Specify the paths/directories to TM/ROS package definition
    project_description_pkg = 'tm_description'
    description_dir = get_package_share_directory(project_description_pkg)
    robot_description_file = os.path.join(description_dir, robot_model_path, robot_model_file)
    rviz_path_file = '/rviz/view_robot.rviz'
    rviz_config_file = description_dir + rviz_path_file

    # -------------------------------------------------------------------------
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            robot_description_file,
            " ",
            "name:=tm5"
        ]
    )

    robot_description = {'robot_description': ParameterValue(robot_description_content, value_type=None)}
    # -------------------------------------------------------------------------	

    # Publish TF
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            robot_description
        ]
    )

    # Publish joint states
    joint_state_slider = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output=['screen']
    )

    # Visualize in RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='log',
        arguments=['-d', rviz_config_file],
        parameters=[
            robot_description
        ]
    )

    # List of nodes to be launched
    return LaunchDescription(
        [
            robot_state_publisher_node,
            joint_state_slider,
            rviz_node,
        ]
    )
