#!/bin/bash

echo "Restarting PX4..."

pkill -f mavsdk_server
pkill -f px4
pkill -f gz

sleep 2

cd ~/Projects/PX4-Autopilot

make px4_sitl gz_x500