from launch import LaunchDescription
from launch_ros.actions import Node
from math import pi

# Rotation Order: zyx and clockwise is positive, anti-clockwise negative

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments = ['0.13', '0.1', '0', '1.5708', '0', '1.5708', 'map', 'motive_origin']
        ),
        Node(
            package='ros2_tetherbot',
            executable='ros2_tetherbot_motive_transform_broadcaster'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments = ['0', '0.15', '0', '0', '-3.1415', '1.5708', 'tbot_motive_origin', 'tbot_center']
        ),
        Node(
            package='ros2_tetherbot',
            executable='ros2_tetherbot_tbot_pose_publisher'
        )
    ])