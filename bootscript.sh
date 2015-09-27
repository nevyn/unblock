#!/bin/bash

### BEGIN INIT INFO
# Provides:          unblock
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Daemons for Unblock
# Description:       Reads two sensors and outputs audio for the unblock project
### END INIT INFO


case "$1" in 
    start)
        echo "Starting unblock"
        python /home/pi/unblock/unblock-input-reader.py &
        python /home/pi/unblock/unblock-music-runner.py &
        ;;
    stop)
        echo "Stopping unblock"
        killall unblock-input-reader
        killall unblock-music-runner
        ;;
    *)
        echo "Usage: /etc/init.d/servod start|stop"
        exit 1
        ;;
esac

exit 0



