import time
import random

import celery
# from celery import Celery
# from celery import group
# from celery import chord


app = celery.Celery(
    'tasks',
    broker = 'pyamqp://guest:guest@localhost//',
#    result_backend = 'cache+memcached://127.0.0.1:11211//',
    backend = 'cache+memcached://127.0.0.1:11211//',
)

@app.task
def build_server():
    print('wait 10 sec')
    time.sleep(10)
    server_id = random.randint(1, 100)
    return server_id


@app.task
def build_servers():
    g = celery.group(
        build_server.s() for _ in range(10)) #비동기로 10개 실행
    return g()

@app.task
def callback(result):
    for server_id in result:
        print(server_id)
    print('clean up')
    return 'done'

@app.task
def build_servers_with_cleanup(): # 이상하게 작동함@@
    c = celery.chord(
        (build_server.s() for _ in range(10)),
        callback.s())
    return c()

@app.task
def setup_dns(server_id):
    print('setup dns for {}'.format(server_id))
    return 'done for {}',format(server_id)

@app.task
def deploy_customer_server(): # 순서를 붙여서 Tasker 실행
    chain = build_server.s() | setup_dns.s()
    return chain()

