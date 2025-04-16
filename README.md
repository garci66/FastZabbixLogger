# FastLogger
A docker image that logs your speed against fast.com given an interval and sends it to a zabbix server

# Environment variables:

### SLEEP_MIN 
Default: `10`

Specifies the interval between tests

### DATE_FORMAT
Default: `"%a %b %d %X %Z %Y"`

Specifies the date format

### LOG_FORMAT
Default: `"{} - {} Mbps - Zabbix Response: {}"`

`{}` are replaced by the date (formatted as above), the speed and the response from zabbix

### OUTPUT_FILE
Default: `"/speed-log.txt"`

Filename to where the results will be logged

### TEST_DURATION
Default: `6`

How many seconds the test runs for

### ZABBIX_SERVER
Default: `127.0.0.1`

IP address of the zabbix server to send results to

### ZABBIX_PORT
Default: `10051`

The port on which the zabbix sender is listening to

### ZABBIX_METRIC_HOST
Default: `"Zabbix Server"`

The zabbix host name for the device on which the metric is reported under

### ZABBIX_METRIC_KEY
Default: `speedtest[fastdotcom]`

The key name for the reported value. It should be configured under the host with a type of Trapper
The template (in the repo) should create the times

## Some details on how to launch
```

 1177  docker run --name zabbix-fastdotcom   -e TEST_DURATION=10 -e ZABBIX_SERVER=192.168.128.7 -e ZABBIX_PORT=10051  -d garci66/fastzabbixlogger:0.1.2
 1179  docker exec -it zabbix-fastdotcom sh
 1181  docker stop zabbix-fastdotcom
 1183  docker stop zabbix-fastdotcom
 1185  dockerrm zabbix-fastdotcom
 1186  docker rm zabbix-fastdotcom
 1187  docker run --name zabbix-fastdotcom   -e TEST_DURATION=10 -e ZABBIX_SERVER=192.168.128.7 -e ZABBIX_PORT=10051 -e ZABBIX_METRIC_HOST="Zabbix server"  -d garci66/fastzabbixlogger:0.1.2
 1188  docker exec -it zabbix-fastdotcom sh
 1190  docker stop zabbix-fastdotcom
 1191  docker run --name zabbix-fastdotcom  --restart=always  --link zabbix-server:zabbix-server  -e TEST_DURATION=10 -e SLEEP_MIN=60 -e ZABBIX_METRIC_HOST="Zabbix server"  -d garci66/fastzabbixlogger:0.1.3
 1192  docker rm zabbix-fastdotcom
 1193  docker run --name zabbix-fastdotcom  --restart=always  --link zabbix-server:zabbix-server  -e TEST_DURATION=10 -e SLEEP_MIN=60 -e ZABBIX_METRIC_HOST="Zabbix server"  -d garci66/fastzabbixlogger:0.1.3
 1195  docker exec -it zabbix-fastdotcom sh
 1197  docker stop zabbix-fastdotcom
 1198  docker rm zabbix-fastdotcom
 1199  docker run --name zabbix-fastdotcom  --restart=always  --link zabbix-server:zabbix-server  -e TEST_DURATION=20 -e SLEEP_MIN=60  -d garci66/fastzabbixlogger:0.1.4
```
