#!/bin/bash

PX4_DIR="$HOME/Projects/PX4-Autopilot"
DRONEOS_DIR="$HOME/Projects/DronOS"

case "$1" in

start)
    echo "Starting PX4..."
    cd "$PX4_DIR"

    env -i \
    HOME="$HOME" \
    USER="$USER" \
    PATH="/usr/bin:/bin:/usr/local/bin" \
    bash -lc "make px4_sitl gz_x500"
    ;;

stop)
    echo "Stopping PX4..."
    pkill -f mavsdk_server
    pkill -f px4
    pkill -f gz
    ;;

restart)
    echo "Restarting PX4..."
    pkill -f mavsdk_server
    pkill -f px4
    pkill -f gz
    sleep 2
    cd "$PX4_DIR"

    env -i \
    HOME="$HOME" \
    USER="$USER" \
    PATH="/usr/bin:/bin:/usr/local/bin" \
    bash -lc "make px4_sitl gz_x500"
    ;;

dev)
    echo "Starting development environment..."

    pkill -f mavsdk_server
    pkill -f px4
    pkill -f gz

    sleep 2

    gnome-terminal -- bash -c "
        cd "$PX4_DIR"

        env -i \
        HOME="$HOME" \
        USER="$USER" \
        PATH="/usr/bin:/bin:/usr/local/bin" \
        bash -lc "make px4_sitl gz_x500"
        exec bash
    "

    sleep 10

    cd "$DRONEOS_DIR"

    source .venv/bin/activate

    python src/main.py
    ;;

*)
    echo "Usage:"
    echo "./scripts/drone.sh start"
    echo "./scripts/drone.sh stop"
    echo "./scripts/drone.sh restart"
    echo "./scripts/drone.sh dev"
    ;;
esac
