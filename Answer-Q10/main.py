import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

answers = pd.read_csv('Data/Answer.csv', encoding="utf-16")
answers = answers.drop(0)
questions = pd.read_csv('Data/Questions.txt', encoding="utf-16")
Q_A = pd.read_csv('Data/Q_A.csv', encoding="utf-16")
user_badge = pd.read_csv('Data/user_badge.txt', encoding="utf-16")
tags = pd.read_csv('Data/tags.txt', sep='\t')
users = pd.read_csv('Data/U.csv', encoding="utf-16")

merged_Q_U = (
    questions.merge(users, left_on='OwnerUserId', right_on='Id', how='inner')
    .assign(Reputation_Category=lambda x: pd.qcut(x['Reputation'], q=3, labels=['Low', 'Medium', 'High']))
)

mean_scores = merged_Q_U.groupby('Reputation_Category', observed=False)['Score'].mean()

mean_scores.plot(kind='bar', figsize=(7, 5), rot=45, color="brown")
plt.title('Mean score for Each Reputation_Category')
plt.xlabel('Reputation_Category')
plt.ylabel('Mean score')
plt.tight_layout()
plt.savefig('Result question 10.png', dpi=300, bbox_inches='tight')
plt.show()
