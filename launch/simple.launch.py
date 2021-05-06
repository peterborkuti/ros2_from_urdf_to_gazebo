import os

from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
import launch
import launch_ros.actions


def generate_launch_description():
    urdf_dir = get_package_share_directory('simple')
    xacro_file = os.path.join(urdf_dir, 'simple.xacro')

    params = {'robot_description': Command(['xacro',' ', xacro_file])}
    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='both',
                                  parameters=[params])
    jsp_gui = launch_ros.actions.Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui')

    return launch.LaunchDescription([rsp, jsp_gui])