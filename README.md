# data-driven-minecraft

This repository is a cut down and modified version of the [MCEdit-Unified](https://github.com/Khroki/MCEdit-Unified) codebase.

It contains some python scripts to help anyone trying to combine data with minecraft using code.

## peterborough_cathedral_from_lidar_dsm_dtm.py

Uses environment agency LiDAR data to model Peterborough Cathedral in sandstone.

## peterborough_cathedral_west_front_removed.py

Uses environment agency LiDAR data to model a second Peterborough Cathedral in sandstone with the west front blocks removed.

## peterborough_cathedral_west_front_from_point_cloud.py

Uses a photogrammetry point cloud, to reconstruct the west front first reducing the number of points by rounding each point to the nearest metre.