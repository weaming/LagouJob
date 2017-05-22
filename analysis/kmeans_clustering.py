from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd


def main(csv_filepath):
    df = pd.read_csv(csv_filepath).loc[:,
         ['companyScore', 'describeScore', 'comprehensiveScore', 'interviewerScore', 'usefulCount', 'myScore',
          'replyCount',
          'isAnonymous', 'sentiment']]
    df['isAnonymous'] = [int(_) for _ in df['isAnonymous']]
    df_scaled = pd.DataFrame(preprocessing.scale(df))
    kmeans_model = KMeans(n_clusters=5, random_state=1).fit(df_scaled)
    labels = kmeans_model.labels_
    print(kmeans_model)


if __name__ == '__main__':
    main('../spider/data/lagou_interviewee.csv')
