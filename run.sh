#!/bin/bash

pkill -f mavsdk_server >/dev/null 2>&1
pkill -f "python.*main.py" >/dev/null 2>&1

source .venv/bin/activate

cd src

python main.py