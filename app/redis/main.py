import asyncio
from aioredis import Redis

async def main():
    # Redis 서버와의 연결을 설정합니다.
    redis = Redis.from_url("redis://localhost:6379", encoding="utf-8")

    # 키-값 쌍을 설정합니다.
    await redis.set("my_key", "my_value")
    print("Key set successfully")

    # 설정한 값을 검색합니다.
    value = await redis.get("my_key")
    print(f"Value retrieved: {value}")

    # 키-값 쌍을 삭제합니다.
    await redis.delete("my_key")
    print("Key deleted successfully")

    # 연결을 종료합니다.
    await redis.close()

# 비동기 함수를 실행합니다.
asyncio.run(main())

