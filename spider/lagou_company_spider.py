import time

from util import log
from config import config
from spider import lagou_spider

import requests
import pandas as pd


def crawl_company(havemark=0):
    """
    crawl company's info 
    :param havemark: 0 for not showing interviewees' remark; 1 for showing interviewees' remark; the default value is 0 
    :return: 
    """
    COMPANY_LIST = list()

    req_url = 'https://www.lagou.com/gongsi/0-0-0.json?havemark=%d' % havemark
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/gongsi/0-0-0?havemark=0',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
                      'Mobile/13B143 Safari/601.1'
    }

    for pn in range(20):
        params = {
            'first': 'false',
            'pn': str(pn),
            'sortField': '0',
            'havemark': str(havemark)
        }

        response = requests.post(req_url, headers=headers, params=params, cookies=lagou_spider.get_cookies(),
                                 timeout=10)
        print(response.url)
        if response.status_code == 200:
            company_list_per_page = response.json()['result']
            for company in company_list_per_page:
                COMPANY_LIST.append([company['companyId'], company['companyShortName'],
                                     company['city'], company['companyFeatures'],
                                     company['companyFullName'], company['financeStage'], company['industryField'],
                                     company['interviewRemarkNum'], company['positionNum'], company['processRate']])
            log.info('page %d has been crawled down~' % (pn + 1))
        elif response.status_code == 403:
            log.error('403 forbidden...')
        else:
            log.error(response.status_code)
        time.sleep(config.TIME_SLEEP)

    return COMPANY_LIST


if __name__ == '__main__':
    company_list = crawl_company(0)
    cols = [u'公司编码', u'公司名称', u'所在城市', u'企业文化', u'公司全称', u'融资阶段', u'所属行业', u'面试评价', u'在招职位', u'简历处理速率']
    df = pd.DataFrame(company_list, columns=cols)
    df.to_excel('./data/company.xlsx', 'Company')
    log.info('Processing done!')
