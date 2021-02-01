import time

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')

start = time.time()
find_users_sync(3)
find_users_sync(2)
find_users_sync(1)
end = time.time()
print(f'>>> 동기 처리 총 소요 시간: {end - start}')



import time
import asyncio

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        # CPU is not Sleep
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

# start = time.time()
# await asyncio.wait([
#     find_users_async(3),
#     find_users_async(2),
#     find_users_async(1),
# ])
# end = time.time()
# print(f'>>> 비동기 처리 총 소요 시간: {end - start}')
