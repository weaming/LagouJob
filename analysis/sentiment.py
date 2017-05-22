from collections import defaultdict

import os
import re
import codecs

import jieba
import jieba.analyse
from snownlp import SnowNLP

STOP_WORDS = '../config/stopwords.txt'
BOSON_SENTIMENT_SCORE = '../config/BosonNLP_sentiment_score.txt'
NEGATIVE_COMMENT_WORDS = '../config/负面评价词语（中文）.txt'
DEGREE_WORDS = '../config/程度级别词语（中文）.txt'


def cal_sentiment(text):
    """
    calculate the sentiment value of a particular sentence powered by SnowNLP
    :param text: 
    :return: 
    """
    s = SnowNLP(text)

    return s.sentiments


def sentence2word(sentence):
    """
    cut the sentence into words and return the new words list without stop words 
    :param sentence: 
    :return: 
    """
    result_list = []
    original_list = jieba.cut(sentence, cut_all=True)
    stopwords_list = read_lines(STOP_WORDS)
    for _ in original_list:
        if _ not in stopwords_list:
            result_list.append(_)

    return result_list


def read_lines(filepath):
    word_list = list()
    with open(filepath, mode='rt', encoding='UTF-8') as f:
        for _ in f.readlines():
            word_list.append(_.replace('\n', ''))

    return word_list


def classify_words(wordDict):
    sentiment_list = read_lines(BOSON_SENTIMENT_SCORE)
    sentiment_dict = defaultdict()
    for s in sentiment_list:
        sentiment_dict[s.split(' ')[0]] = s.split(' ')[1]
    negative_list = read_lines(NEGATIVE_COMMENT_WORDS)
    degree_list = read_lines(DEGREE_WORDS)
    degree_dict = defaultdict()

    for d in degree_list:
        degree_dict[d.split(', ')[0]] = d.split(', ')[1]

    senWord = defaultdict()
    notWord = defaultdict()
    degreeWord = defaultdict()

    for word in wordDict.keys():
        if word in sentiment_dict.keys() and word not in negative_list and word not in degree_dict.keys():
            senWord[wordDict[word]] = sentiment_dict[word]
        elif word in negative_list and word not in degree_dict.keys():
            notWord[wordDict[word]] = -1
        elif word in degree_dict.keys():
            degreeWord[wordDict[word]] = degree_dict[word]

    return senWord, notWord, degreeWord


if __name__ == '__main__':
    text = '老子头一次遇到最坑爹的面试官fengquan，态度冰冷以及不尊重人，很明显就是欺负比他强的老司机！全程逼问，全盘否定！说啥要把我所有作品的psd都要交给他，连动画也要，还问啥游戏原画为啥没有动画作品呢？特么逗死人了？凭啥呢？然后在职场我给他做了笔试题之后，给他看，他盯着我画的图看了好久，然后说“画的没问题…”，然后再让我回去给他做第二个测试题就是上色，完了必须要AI的psd都要发给他。这啥玩意儿啊？！草草了事，要么说了，然后不想再废话就自己出门去算结束了。\n强烈建议大家不要去这家了，要么真入职了之后，迟早会恶意对待你们的。'
    print('/'.join(sentence2word(text)))
    # sentiment = cal_sentiment(text)
    # print(sentiment)
