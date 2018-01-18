# FastLogger
A docker image that logs your speed against fast.com given an interval and sends it to a zabbix server

# Environment variables:

## SLEEP_MIN 
Default: 10
Specifies the interval between tests

## DATE_FORMAT
Default: "%a %b %d %X %Z %Y"
Specifies the date format

## LOG_FORMAT
Default: "{} - {} Mbps - Zabbix Response: {}"
{} are replaced by the date (formatted as above), the speed and the response from zabbix

## OUTPUT_FILE
Default: "/speed-log.txt"

## TEST_DURATION
Default: 6
How many seconds the test runs for

## ZABBIX_SERVER
Default: 127.0.0.1
IP address of the zabbix server to send results to

## ZABBIX_PORT
Default: 10051
The port on which the zabbix sender is listening to

## ZABBIX_METRIC_HOST
Default: "Zabbix Server"

The zabbix host name for the device on which the metric is reported under

## ZABBIX_KETRIC_KEY
Default: speedtest[fastdotcom]

The key name for the reported value. It should be configured under the host with a type of Trapper
The template (in the repo) should create the times
