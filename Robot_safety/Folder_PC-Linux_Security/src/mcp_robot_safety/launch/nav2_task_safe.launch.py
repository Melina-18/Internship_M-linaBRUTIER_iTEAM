from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import GroupAction

def generate_launch_description():

    robot_id = LaunchConfiguration("robot_id")
    use_sim = LaunchConfiguration("use_sim")

    controller_config = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/controller_server.yaml'
    ])

    planner_config = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/planner_server.yaml'
    ])

    behavior_config = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/behavior_server.yaml'
    ])

    smoother_config = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/smoother_server.yaml'
    ])

    bt_navigator_config = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/bt_navigator.yaml'
    ])

    bt_navigator_pose_xml = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/behavior_trees/navigate_to_pose.xml'
    ])

    bt_navigator_poses_xml = PathJoinSubstitution([
        FindPackageShare('robotnik_simulation_navigation'),
        'config/behavior_trees/navigate_through_poses.xml'
    ])

    controller_server = Node(
        package='nav2_controller',
        executable='controller_server',
        name='controller_server',
        output='screen',
        parameters=[controller_config, {'use_sim_time': use_sim}],
        remappings=[
            ('cmd_vel', 'robotnik_base_control/cmd_vel_raw'),
            ('odom', 'robotnik_base_control/odom'),
        ]
    )

    planner_server = Node(
        package='nav2_planner',
        executable='planner_server',
        name='planner_server',
        output='screen',
        parameters=[planner_config, {'use_sim_time': use_sim}],
    )

    behavior_server = Node(
        package='nav2_behaviors',
        executable='behavior_server',
        name='behavior_server',
        output='screen',
        parameters=[behavior_config, {'use_sim_time': use_sim}],
        remappings=[
            ('cmd_vel', 'robotnik_base_control/cmd_vel_raw')
        ]
    )

    smoother_server = Node(
        package='nav2_smoother',
        executable='smoother_server',
        name='smoother_server',
        output='screen',
        parameters=[smoother_config, {'use_sim_time': use_sim}],
    )

    bt_navigator = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        name='bt_navigator',
        output='screen',
        parameters=[
            bt_navigator_config,
            {
                'use_sim_time': use_sim,
                'default_nav_to_pose_bt_xml': bt_navigator_pose_xml,
                'default_nav_through_poses_bt_xml': bt_navigator_poses_xml,
            }
        ],
        remappings=[
            ('odom', 'robotnik_base_control/odom'),
        ]
    )

    lifecycle_manager_navigation = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_navigation',
        output='screen',
        parameters=[
            {
                'use_sim_time': use_sim,
                'autostart': True,
                'node_names': [
                    'controller_server',
                    'planner_server',
                    'behavior_server',
                    'smoother_server',
                    'bt_navigator'
                ]
            }
        ]
    )

    group = GroupAction([
        controller_server,
        planner_server,
        behavior_server,
        smoother_server,
        bt_navigator,
        lifecycle_manager_navigation
    ])

    return LaunchDescription([group])
