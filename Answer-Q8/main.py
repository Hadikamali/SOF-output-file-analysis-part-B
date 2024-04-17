import pandas as pd
import numpy as np
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
user_badge = pd.read_csv('Data/user_badge.txt', encoding="utf-16")
tags = pd.read_csv('Data/tags.txt', sep='\t')
users = read_file('Data/U.csv', encoding="utf-16")

answers_q_a = pd.merge(answers, q_a, left_on='Id', right_on='AId', how='inner')
answers_question = pd.merge(answers_q_a, questions, left_on='QId', right_on='Id', how='inner', suffixes=('_A', '_Q'))
answers_question.head()

answer_counts = (
    answers_question.groupby('Id_Q').size()
    .reset_index(name='Answer_count')
    .assign(Answer_count=lambda x: np.where(x['Id_Q']
    .isin(answers_question[answers_question['AId'] == -1]['Id_Q'].unique())
                                            , 0, x['Answer_count']))
)
answer_counts

questions = answer_counts.merge(questions, left_on='Id_Q', right_on='Id', how='inner')
questions

questions['Answer_count_Category'] = pd.cut(questions['Answer_count'], bins=[-1, 0, 20, 50, float('inf')], labels=['Zero', 'Low', 'Medium', 'High'])
mean_scores = questions.groupby('Answer_count_Category')['Score'].mean()

mean_scores.plot(kind='bar', figsize=(7, 5))
plt.title('Mean Score for Each Answer count Category')
plt.xlabel('Answer count Category')
plt.ylabel('Mean Score')
plt.tight_layout()
plt.savefig('Result question 8.png', dpi=1200, bbox_inches='tight')
plt.show()
