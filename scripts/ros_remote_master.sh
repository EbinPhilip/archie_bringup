#!/bin/bash
REMOTE_EXPORT_SCRIPT=~/ros_remote_server.sh

if [[ $1 == "off" ]]
then
    sed -i -e "/export/s/^#*/#/" $REMOTE_EXPORT_SCRIPT
    echo "remote master: off"
else
    sed -i -e "/export/s/^#*//" $REMOTE_EXPORT_SCRIPT
    echo "remote master: on"
fi
