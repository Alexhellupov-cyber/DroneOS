#!/bin/bash

echo "Stopping PX4..."

pkill -9 -f px4
pkill -9 -f gz
pkill -9 -f mavsdk_server

sleep 2

echo "Done."