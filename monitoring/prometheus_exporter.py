from prometheus_client import start_http_server, Gauge
import time

# Create a metric to track uptime
uptime_gauge = Gauge('axiomhive_uptime', 'AXIOMHIVE Uptime Percentage')

def main():
    # Start up the server to expose the metrics.
    start_http_server(8080)
    # Set the uptime to 99.9%
    uptime_gauge.set(99.9)
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()