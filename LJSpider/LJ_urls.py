# 运行该脚本往 redis里面添加任务list添加爬取目标url
import redis

urls = []
# 北京朝阳区二手房 1-100页爬取
for i in range(1,101):
    url = 'http://bj.lianjia.com/ershoufang/chaoyang/pg%dco32/' % i
    urls.append(url)

r =redis.Redis('localhost')


r.lpush('lianjia_beijing_urls', *urls)