from dateutil import parser
from pyzabbix import ZabbixMetric, ZabbixSender

import fastdotcom
import time
import os
import json



sleep_min = int(os.getenv("SLEEP_MIN", 10))
date_format = os.getenv("DATE_FORMAT", "%a %b %d %X %Z %Y")
log_format = os.getenv("LOG_FORMAT", "{} - {} Mbps - Zabbix Response: {}")
output_file = os.getenv("OUTPUT_FILE", "/speed-log.txt")
test_duration = int(os.getenv("TEST_DURATION", 6))
zabbix_server = os.getenv("ZABBIX_SERVER", "127.0.0.1")
zabbix_port = int(os.getenv("ZABBIX_PORT", 8080))
zabbix_metric_hostname = os.getenv("ZABBIX_METRIC_HOST","Zabbix Server")
zabbix_metric_key = os.getenv("ZABBIX_KETRIC_KEY", "speedtest[fastdotcom]")

line_regex = re.compile(log_format.format("(.+?)", "([0-9.]+)"))


if __name__ == '__main__':
    print("Starting Logger")

    open(output_file, "a+").close()

    try:
        while True:
            speed = fastdotcom.fast_com(maxtime=test_duration)
            date = time.strftime(date_format)
            packet = [ ZabbixMetric(zabbix_metric_hostname, zabbix_metric_key, speed)]
            result = ZabbixSender(zabbix_server, zabbix_port).send(packet)
            output = log_format.format(date, speed, result)

            with open(output_file, "a+") as f:
                f.write(output + "\n")
            

            time.sleep(60 * sleep_min)
    except Exception as e:
        print(e)
        pass
