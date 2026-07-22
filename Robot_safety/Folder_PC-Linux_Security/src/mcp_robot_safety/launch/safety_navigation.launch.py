from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import PushRosNamespace, Node
from launch.actions import GroupAction

def generate_launch_description():
    declared_arguments = [
        DeclareLaunchArgument("robot_id", default_value="robot"),
        DeclareLaunchArgument("use_sim", default_value="true"),
    ]

    robot_id = LaunchConfiguration("robot_id")
    use_sim = LaunchConfiguration("use_sim")

    # Ta version modifiée de nav2_task (remap cmd_vel_raw)
    nav2_task_safe = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('mcp_robot_safety'), 'launch/nav2_task_safe.launch.py'
            ])
        ),
        launch_arguments={'robot_id': robot_id, 'use_sim': use_sim}.items()
    )

    # nav2_mission original, inchangé
    nav2_mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('robotnik_simulation_navigation'), 'launch/nav2_mission.launch.py'
            ])
        ),
        launch_arguments={'robot_id': robot_id, 'use_sim': use_sim}.items()
    )

    # Ton nœud de sécurité
    safety_filter = Node(
        package='mcp_robot_safety',
        executable='safety_node',
        name='robotnik_safety_filter',
        output='screen',
        parameters=[{'use_sim_time': use_sim}],
    )

    group = GroupAction([
        PushRosNamespace(robot_id),
        nav2_task_safe,
        nav2_mission,
        safety_filter,
    ])

    return LaunchDescription(declared_arguments + [group])
