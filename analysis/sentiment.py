from snownlp import SnowNLP


def cal_sentiment(text):
    s = SnowNLP(text)

    return s.sentiments


if __name__ == '__main__':
    text = '老子头一次遇到最坑爹的面试官fengquan，态度冰冷以及不尊重人，很明显就是欺负比他强的老司机！全程逼问，全盘否定！说啥要把我所有作品的psd都要交给他，连动画也要，还问啥游戏原画为啥没有动画作品呢？特么逗死人了？凭啥呢？然后在职场我给他做了笔试题之后，给他看，他盯着我画的图看了好久，然后说“画的没问题…”，然后再让我回去给他做第二个测试题就是上色，完了必须要AI的psd都要发给他。这啥玩意儿啊？！草草了事，要么说了，然后不想再废话就自己出门去算结束了。\n强烈建议大家不要去这家了，要么真入职了之后，迟早会恶意对待你们的。'
    sentiment = cal_sentiment(text)
    print(sentiment)
