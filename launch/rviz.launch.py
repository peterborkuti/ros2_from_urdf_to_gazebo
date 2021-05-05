import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions


def generate_launch_description():
    share_dir = get_package_share_directory('simple') 

    urdf_file = os.path.join(share_dir, 'simple.urdf')
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    rsp_params = {'robot_description': robot_desc}
    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='both',
                                  parameters=[rsp_params])



    rviz_conf_file = os.path.join(share_dir, 'simple.rviz')

    rviz = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_conf_file],
        output='screen')

    

    return launch.LaunchDescription([rsp, rviz])