from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mcp_robot_safety',
            executable='safety_node',
            name='robotnik_safety_filter',
            output='screen',
            # On intercepte ce que Claude envoie pour le forcer à passer par notre filtre
            remappings=[
                ('/robot/robotnik_base_control/cmd_vel', '/robot/robotnik_base_control/cmd_vel_raw')
            ]
        )
    ])
