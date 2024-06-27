from python_on_whales import docker
from redis import Redis

if exists("redis"):

    docker.build("redis")
    redis_container = docker.run("redis", detach=True, publish=[(6379, 6379)])
    # the container is up and listening on port 6379

    redis_client = Redis()
    redis_client.set("hello", "world")
    print(redis_client.get("hello"))
# b'world'
else:
    print("no redis")
