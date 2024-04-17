import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


def read_file(path, encoding="utf-16"):
    df = pd.read_csv(path, encoding=encoding)
    return df


questions = read_file("Data/Questions.txt")
answers = read_file("Data/Answer.csv")
answers = answers.drop(0)
q_a = read_file("Data/Q_A.csv")
merged_Q_A = pd.merge(questions, q_a, left_on='Id', right_on='QId', how='inner')
accepted_flag = merged_Q_A.groupby('Id')['accepted'].any().astype(int)
questions['accepted_flag'] = accepted_flag
correlation = questions['accepted_flag'].corr(questions['ViewCount'])
median_view_count = questions.groupby('accepted_flag')['ViewCount'].median()

sns.barplot(x=median_view_count.index.map({1: 'Accepted', 0: 'Not Accepted'}), y=median_view_count.values, color='blue')
plt.ylabel('Median View Count')
plt.title('Median Of View Count for Accepted vs Not Accepted Answers')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.savefig('Result question 1.png', dpi=1200, bbox_inches='tight')

