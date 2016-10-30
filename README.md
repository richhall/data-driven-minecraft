# data-driven-minecraft

This repository is a cut down and modified version of the [MCEdit-Unified](https://github.com/Khroki/MCEdit-Unified) codebase.

It contains some python scripts to help anyone trying to combine data with minecraft using code.

## peterborough_cathedral_from_lidar_dsm_dtm.py

Uses environment agency LiDAR data to model Peterborough Cathedral in sandstone.

`>python peterborough_cathedral_from_lidar_dsm_dtm.py`

## peterborough_cathedral_west_front_removed.py

Uses environment agency LiDAR data to model a second Peterborough Cathedral in sandstone with the west front blocks removed.

`>python peterborough_cathedral_west_front_removed.py`

## peterborough_cathedral_west_front_from_point_cloud.py

Uses a photogrammetry point cloud, to reconstruct the west front first reducing the number of points by rounding each point to the nearest metre.

`>python peterborough_cathedral_west_front_removed.py`

# Installation

As with MCEdit-Unified, it is recommended to use virtualenv to keep dependencies sane and for easy deployment. You'll need Python 2.7 (Python 3 is not supported) at a minimum before getting started. Easy_install / pip is recommended.

Clone data-driven-minecraft using your github client of choice:

`>git clone --recursive https://github.com/richhall/data-driven-minecraft`

Or, if you've already cloned data-driven-minecraft in the past and need to update, go to the existing source folder then run:

`>git pull`

Optionally (but highly recommended), setup and activate [virtualenv and virtualenvwrapper](http://docs.python-guide.org/en/latest/dev/virtualenvs/). virtualenv will simplify development by creating an isolated and barebones Python environment. Anything you install while virtualenv is active won't affect your system-wide Python installation, for example.

`>cd data-driven-minecraft`
<br>
`>pip install virtualenv`
<br>
`>pip install virtualenvwrapper` (Linux and Mac OS X)
<br>
`>pip install virtualenvwrapper-win` (Windows)
<br>
`>mkvirtualenv data-driven-minecraft`

Install various dependencies. This may take a bit (especially numpy). 

`>pip install pillow` (used to read png files)
<br>
`>pip install numpy` 
<br>
`>pip install pypiwin32` (Windows only, needed for compiling)
<br>
`>pip install plyfile` (used to read ply point cloud)
<br>




