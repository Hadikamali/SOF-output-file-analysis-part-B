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
user_badge = pd.read_csv('Data/user_badge.txt', encoding="utf-16")
tags = pd.read_csv('Data/tags.txt', sep='\t')
users = pd.read_csv('Data/U.csv', encoding="utf-16")
merged_U_A_Q = pd.DataFrame()

answers_q_a = pd.merge(answers, q_a, left_on='Id', right_on='AId', how='inner')
answers_question = pd.merge(answers_q_a, questions, left_on='QId', right_on='Id', how='inner', suffixes=('_A', '_Q'))
merged_U_A_Q = pd.merge(users, answers_question, left_on='Id', right_on='OwnerUserId_A', how='inner')
sns.scatterplot(x='Reputation', y='Score_Q', data=merged_U_A_Q, color="darkred")
plt.title('Correlation between Reputation and Score_Q')
plt.xlabel('Reputation')
plt.ylabel('Score_Q')
plt.savefig('Result question 4-1.png', dpi=1200, bbox_inches='tight')
plt.show()

merged_U_A_Q['Bin'] = pd.qcut(merged_U_A_Q['Reputation'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
mean_scores = merged_U_A_Q.groupby('Bin')['Score_Q'].mean()
plt.figure(figsize=(7, 5))
sns.barplot(x=mean_scores.index, y=mean_scores.values)
plt.title('Mean Score Questions for Each Bin Range')
plt.xlabel('Reputation Ranges')
plt.ylabel('Mean Score Questions')
plt.tight_layout()
plt.savefig('Result question 4-2.png', dpi=1200, bbox_inches='tight')
plt.show()
