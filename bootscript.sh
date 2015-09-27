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

# http://raspberrywebserver.com/serveradmin/run-a-script-on-start-up.html

case "$1" in 
    start)
        echo "Starting unblock"
        bash /home/pi/unblock/unblock-music-runner.bash &
	sleep 3
        python /home/pi/unblock/unblock-input-reader.py &
        ;;
    stop)
        echo "Stopping unblock"
	pkill -f unblock
	killall pd
        ;;
    *)
        echo "Usage: /etc/init.d/servod start|stop"
        exit 1
        ;;
esac

exit 0



