import jieba
import jieba.analyse
from snownlp import SnowNLP

STOP_WORDS = '../config/stopwords.txt'
BOSON_SENTIMENT_SCORE = '../config/sentiment/BosonNLP_sentiment_score.txt'
NEGATIVE_COMMENT_WORDS = '../config/sentiment/negativecommentCN.txt'
DEGREE_WORDS = '../config/sentiment/degreewordsCN.txt'


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


if __name__ == '__main__':
    text = '本书为数据学习方法的导论，面向非数学专业的高年级本科生、硕士和博士研究生。本书还涵盖了大量的R实验，详细解释了在实际生活中如何践行不同的方法，因此对于实践派数据科学家来说是有用的资源。'
    sentiment = cal_sentiment(text)
    print(sentiment)
