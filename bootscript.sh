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

cd /home/pi/unblock/

startup()
{
        mkdir -p log
	rm -rf log/run.log
	echo "Ok, starting for real in 10s" >> log/run.log
	sleep 5
        echo "Starting Pigpio" >> log/run.log
        pigpiod
	sleep 2
	echo "Starting led runner" >> log/run.log
	python unblock-led-runner.py &> log/leds.log &
	sleep 2
	echo "Starting PureData" >> log/run.log

        bash unblock-music-runner.bash &> log/music.log &
        sleep 3

	echo "Starting input reader" >> log/run.log
        python unblock-input-reader.py &> log/input.log &
        echo "Done" >> log/run.log
}

case "$1" in 
    start)
        echo "Starting unblock"
	startup &
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



