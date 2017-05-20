# Data analysis of [Lagou](http://www.lagou.com/)
![LagouIcon](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)

## Introduction
This repository is designed for job data analysis of [Lagou](http://www.lagou.com/). 
The main function it includes is listed here: 

1. crawl job data from [Lagou](www.lagou.com), and get the latest info of jobs
2. data analysis and visualize
3. crawl job details info and generate word cloud as __Job Impression__

## Install
    pip install -r requirements.txt

## Basic Usage
1. clone this project from [github](https://github.com/EclipseXuLu/LagouJob.git)
2. change the file path in source code  
3. run [lagou_spider.py](spider/lagou_spider.py) to get job data and output them with a Excel file
4. run [hot_words.py](analysis/hot_words.py) to cut sentences, and return TOP30 hot words

## Analysis Results
> ![Image1](https://pic2.zhimg.com/a0c42bc6bd7c8743687ba50305c85821_b.jpg)
> ![Image2](https://pic3.zhimg.com/f89ca5a008f8ad84a1a2121888aa10c2_b.jpg)
> ![Image3](https://pic1.zhimg.com/85b930c6aff823a3b8ee73973d20f274_b.jpg)
> ![Image4](https://pic2.zhimg.com/0ce1858e3f261f0a90e50e79bd057e8d_b.png)
> ![Image5](https://pic3.zhimg.com/3854e7ca5a8c53e5bb98a2ae3add4a8e_b.png)

## Report
For more information, please visit my answer at [Zhihu](https://www.zhihu.com/question/36132174/answer/94392659).   
In addition, there is [an another repository](https://github.com/EclipseXuLu/JiaYuan.git) which may help you!   
The PPT report can be found [here](拉勾网数据分析.ppsm).

## One more thing
Inspired by Google IO 2017. We've gotten the data, but how can we make deeper analysis instead of just
doing simple statics. With the help of [Machine Learning](http://baike.baidu.com/link?url=_k8D5Ip3KB8tF-ljDntsbyBEHbmY48S3j4Z58s01MszOeiutS22lr83k_UJRcOSKy1H88FqPcj9WXKiuF5Hy7c1O8NF57EQw43u5Jk1gdaUWhlEgfaAvL-QR5KEi171a),
we can make full use of these data. 

Here are several insights I have thought yet.
* To train a model with machine learning algorithm and judge which company deserves your entrance.
* More features are being developing ~ 
