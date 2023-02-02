from fastapi import FastAPI, Request
import aioredis
import json


app = FastAPI()


async def call_api_server(request):
    # Call API server here
    return {"message": "API response", "cached": False}


@app.get("/")
async def root(request: Request):
    # Connect to Redis server
    redis = await aioredis.create_redis_pool("redis://localhost")

    # Check if the data exists in cache
    cache_key = f"{request.url}?value={request.query_params.get('value')}"
    response_data = await redis.get(cache_key.encode())
    if response_data:
        return {"message": json.loads(response_data.decode()), "cached": True}

    # Call API server if data is not in cache
    response = await call_api_server(request)

    # Save response in cache
    await redis.set(cache_key.encode(), json.dumps(response).encode(), expire=3600)

    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
