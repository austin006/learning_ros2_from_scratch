# #First Example
# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     ld = LaunchDescription()
#     number_publisher = Node(
#         package="my_py_pkg",
#         executable="number_publisher"
#     )
#     number_counter = Node(
#         package="my_py_pkg",
#         executable="number_counter"
#     )
#     ld.add_action(number_publisher)
#     ld.add_action(number_counter)
#     return ld

# Second Example
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    param_config = os.path.join(get_package_share_directory("my_robot_bringup"), "config", "number_params.yaml")
    ld = LaunchDescription()
    number_publisher1 = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="num_pub1",
        remappings=[("/number", "/my_number")],
        parameters=[
            {"number": 3},
            {"publish_period": 1.5}
        ]
    )
    number_publisher2 = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="num_pub2",
        remappings=[("/number", "/my_number")],
        parameters=[param_config]
    )
    number_counter = Node(
        package="my_py_pkg",
        executable="number_counter",
        remappings=[("/number", "/my_number")]
    )
    ld.add_action(number_publisher1)
    ld.add_action(number_publisher2)
    ld.add_action(number_counter)
    return ld