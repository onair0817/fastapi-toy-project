from fastapi import FastAPI, Request
import aioredis
import json
import traceback


app = FastAPI()


async def call_api_server(request):
    # Call API server here
    return {"message": "API response", "cached": False}


@app.get("/")
async def root(request: Request):
    # Connect to Redis server
    try:
        redis = await aioredis.create_redis_pool("redis://localhost")
    except Exception as e:
        return {"error": f"{e}", "traceback": f"{traceback.print_exc()}"}

    # Check if the data exists in cache
    cache_key = f"{request.url}?value={request.query_params.get('value')}"
    try:
        response_data = await redis.get(cache_key.encode())
    except Exception as e:
        return {"error": f"{e}", "traceback": f"{traceback.print_exc()}"}

    if response_data:
        return {"message": json.loads(response_data.decode()), "cached": True}

    # Call API server if data is not in cache
    response = await call_api_server(request)

    # Save response in cache
    try:
        await redis.set(cache_key.encode(), json.dumps(response).encode(), expire=3600)
    except Exception as e:
        return {"error": f"{e}", "traceback": f"{traceback.print_exc()}"}

    redis.close()
    await redis.wait_closed()

    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
