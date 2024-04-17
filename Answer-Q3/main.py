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

answers_q_a = pd.merge(answers, q_a, left_on='Id', right_on='AId', how='inner')
answers_question = pd.merge(answers_q_a, questions, left_on='QId', right_on='Id', how='inner', suffixes=('_A', '_Q'))
correlation = answers_question['Score_A'].corr(answers_question['Score_Q'])

sns.scatterplot(x='Score_Q', y='Score_A', data=answers_question)
plt.title('Score Question and Score Answer Correlation')
plt.xlabel('Score Question')
plt.ylabel('Score Answer')
plt.savefig('Result question 3.png', dpi=1200, bbox_inches='tight')
plt.show()
print(correlation)

