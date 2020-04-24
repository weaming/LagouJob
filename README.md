# Job crawler of [Lagou Job](http://www.lagou.com/)

![Lagou](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)

## Introduction

This repository holds the code for job data analysis of [Lagou](http://www.lagou.com/).
The main functions included are listed as follows:

1. Crawling job data from [Lagou](www.lagou.com), and get the latest information of jobs about Internet.
2. Proxies are collected from [XiCiDaiLi](https://www.xicidaili.com/nn/1).

## Prerequisites

```shell
pip install -r requirements.lock
docker run -d --name mongo -p 27017:27017 \
    -v $HOME/data/mongo:/data/db \
    mvertes/alpine-mongo
```

## How to Use
1. clone this project from [github](https://github.com/lucasxlu/LagouJob.git).
2. Lagou's anti-spider strategy has been upgrade frequently recently. I suggest you run [proxy_crawler.py](./spider/proxy_crawler.py) to get IP proxies and execute the code with [PhantomJS](http://phantomjs.org/).
3. run [m_lagou_spider.py](spider/m_lagou_spider.py) to crawl job data, it will generate a collection of Excel files in ```./data``` directory.

## LICENSE
[Apache-2.0](./LICENSE)
