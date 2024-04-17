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
Q_A = read_file("Data/Q_A.csv")
user_badge = read_file('Data/user_badge.txt', encoding="utf-16")
tags = pd.read_csv('Data/tags.txt', sep='\t')
users = read_file('Data/U.csv', encoding="utf-16")


merged_A_Q = pd.merge(answers, Q_A, left_on='Id', right_on='AId', how='inner')
merged_A_Q = pd.merge(merged_A_Q, questions, left_on='QId', right_on='Id', how='inner', suffixes=('_A', '_Q'))
merged_U_A_Q = pd.merge(users, merged_A_Q, left_on='Id', right_on='OwnerUserId_A', how='inner')
merged_U_A_Q['Closed_Q'] = merged_U_A_Q['ClosedDate_Q'].notnull().astype(int)
merged_U_A_Q['Bin'] = pd.qcut(merged_U_A_Q['Reputation'], q=10, labels=['D1', 'D2', 'T3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'])
merged_U_A_Q['Closed_Q'] = merged_U_A_Q['Closed_Q'].astype(float)
mean_closed_questions = merged_U_A_Q.groupby('Bin')['Closed_Q'].mean()

plt.figure(figsize=(7, 5))
sns.barplot(x=mean_closed_questions.index, y=mean_closed_questions.values)
plt.title('Mean Closed Questions for Each Bin Range')
plt.xlabel('Reputation Ranges')
plt.ylabel('Mean Closed Questions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Result question 5-1.png', dpi=300, bbox_inches='tight')
plt.show()


sns.boxplot(x='Closed_Q', y='Reputation', data=merged_U_A_Q[merged_U_A_Q['Reputation'] < 8000], palette=['red', 'blue'] )
plt.title('Distribution of Reputation based on Closed Questions')
plt.xlabel('Closed Question')
plt.ylabel('Reputation')
plt.savefig('Result question 5-2.png', dpi=1200, bbox_inches='tight')
plt.show()