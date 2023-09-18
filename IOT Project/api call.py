import requests

url = "http://127.0.0.1:8000/notifyUser/"
data = {
    "sensor_name": "Accelerometer",
    "customer_id":  "2",
    "checkparam": {"x":100,"y":90,"z":80}
}

res = requests.post(url, json=data)
print(res.status_code)
print(res.json())