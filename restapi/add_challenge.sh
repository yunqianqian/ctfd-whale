curl -H "Content-Type: application/json" -X POST  "http://192.168.159.130:5000/challenge" -d '{
    "imageId":"8cf1bfb43f",
    "cpu": "0.5",
    "memory": "128m",
    "redirect_type": "redirt",
    "port": "80"
}'