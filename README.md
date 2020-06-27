# Weight Tracker

This app is simple weight tracker made using FastAPI.

## Run
```
uvicorn main:app --reload
```

### Test endpoints via FastAPI build-in endpoint
```
http://127.0.0.1:8000/docs
```

### Test endpoints from console
/add_measurement
```
curl -X PUT "http://127.0.0.1:8000/add_measurement/user_id={user_id}&weight={weight}" -H "accept: application/json"
```

/get_weight
```
curl -X GET "http://127.0.0.1:8000/get_weight/{user_id}" -H "accept: application/json"
```
/get_weights
```
curl -X GET "http://127.0.0.1:8000/get_weights/{user_id}" -H "accept: application/json"
```
