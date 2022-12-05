# telescope-web 后台模块

## Run

### 获取代码并准备环境

```
// 1.克隆项目
git clone https://github.com/telescope-org/telescope-web.git  
// 2.准备环境
cd telescope-web
python3 -m venv venv/
pip3 install -r requirement.txt
```

### 设置Redis地址

找到代码中Redis.py文件，进行填入配置。

```python
import redis

class RedisConnection(object):
    def __init__(self):
        self.redis = redis.Redis(host='', port=6379, decode_responses=True, password='')  
    def get_redis(self):
       return self.redis
```

### 运行

```
python3 server.py
```

