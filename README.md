<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.284 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sat May 08 2021 23:18:49 GMT-0700 (PDT)
* Source doc: ROS2 from URDF to Gazebo

WARNING:
You have 5 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 0.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p>
<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# From URDF to Gazebo


## ROS2 and Gazebo-11 \
Péter Borkuti, 2021.05

How to create a simulation in Gazebo and control/watch it with ROS2


## Tags

URDF, xacro, SDF, rviz2, launch, gazebo world, gazebo model, joint state publisher, joint pose trajectory


## Useful links:

[http://gazebosim.org/tutorials/?tut=ros_urdf](http://gazebosim.org/tutorials/?tut=ros_urdf)

[https://github.com/ros-controls/ros2_control_demos](https://github.com/ros-controls/ros2_control_demos)

[http://gazebosim.org/tutorials?tut=build_robot&cat=build_robot](http://gazebosim.org/tutorials?tut=build_robot&cat=build_robot)

[http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros](http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)


## Steps



1. create a robot in URDF with xacro with fixed joints and view it in rviz2
2. add gazebo elements to URFD to view robot in gazebo
3. change fixed joints with movable joints
4. control robot with rviz2 and joint_state_publisher_gui
5. control robot with python3 and watch it in rviz
6. create a gazebo model
7. create a gazebo world
8. add gazebo plugin to world and model to move it from ros2 topics and view it in gazebo
9. add gazebo plugin to world and model to watch its joint states from ros2 topics


## Prerequisites

ubuntu, ros2 foxy, gazebo-11, setup ros2 and colcon, have ros2_ws ros2 workspace, be familiar with colcon, topics, ros2 packages, basic ros2 tutorials


## Step-by-step:

See the commit messages in  [https://github.com/peterborkuti/ros2_from_urdf_to_gazebo/commits/master](https://github.com/peterborkuti/ros2_from_urdf_to_gazebo/commits/master)
