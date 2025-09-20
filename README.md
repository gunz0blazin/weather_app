+----------------+       +-----------------------+
|  Local Sensors |       |  External Weather API |
| (ESP32, RPi)   |       |  (OpenWeather, NWS)   |
+--------+-------+       +-----------+-----------+
         |                           |
         v                           v
+----------------+          +--------------------+
|   MQTT Broker  |          | API Fetch Service  |
|   (Mosquitto)  |          | (Python/Node/Etc.) |
+--------+-------+          +----------+---------+
         |                             |
         +-------------+---------------+
                       v
              +------------------+
              |    Database      |
              | (InfluxDB/Postgres)|
              +---------+--------+
                        |
            +-----------+------------+
            |                        |
            v                        v
   +-------------------+    +-------------------+
   | Web API Service   |    | Visualization     |
   | (FastAPI/Flask)   |    | (Grafana / HA)    |
   +---------+---------+    +---------+---------+
             |                        |
             v                        v
      +--------------+        +----------------+
      | Apps/Clients |        | Remote Access  |
      | (Web/Mobile) |        | (Tailscale)    |
      +--------------+        +----------------+
