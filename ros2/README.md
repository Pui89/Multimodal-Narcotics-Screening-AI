# Optional ROS 2 workspace

For an actual ROS 2 build, use Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic. Review ../docs/PUI89_FULL_ROBOTICS_STACK_INTEGRATION.md first. These commands are optional operator actions; they are not run by repository changes or CI.

From the repository root on a compatible machine:

```bash
source /opt/ros/jazzy/setup.bash
cd ros2
colcon build --packages-select pui89_sim_bridge
source install/setup.bash
ros2 run pui89_sim_bridge pui89_sim_proposal_bridge --ros-args -p project_id:=PUI89 -p ready_action:=REQUEST_HUMAN_REVIEW
```

In a separate terminal publish synthetic state, then echo the symbolic proposal:

```bash
source /opt/ros/jazzy/setup.bash
source ros2/install/setup.bash
ros2 topic pub --once /pui89/sim/world_state std_msgs/msg/String "{data: '{"sensors_ok": true, "sensor_data_fresh": true, "comms_ok": true, "confidence": 0.9, "human_review_required": true}'}"
ros2 topic echo /pui89/sim/action_proposal
```

The bridge emits JSON labels only. It has no velocity, Nav2 goal, MAVLink, cutter, propulsion, door, alarm or enforcement command.