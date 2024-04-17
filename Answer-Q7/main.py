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

merged_A_Q = pd.merge(answers, Q_A, left_on='Id', right_on='AId', how='inner')
merged_A_Q = pd.merge(merged_A_Q, questions, left_on='QId', right_on='Id', how='inner', suffixes=('_A', '_Q'))
merged_Q_A = pd.merge(questions, Q_A, left_on='Id', right_on='QId', how='inner')
merged_A_Q['accepted_flag'] = merged_Q_A.groupby('Id')['accepted'].any().astype(int)

merged_A_Q['CreationDate_A'] = pd.to_datetime(merged_A_Q['CreationDate_A'], errors='coerce')
merged_A_Q['CreationDate_Q'] = pd.to_datetime(merged_A_Q['CreationDate_Q'], errors='coerce')

merged_A_Q['timeDiffrence(Hours)'] = (merged_A_Q['CreationDate_A'] - merged_A_Q['CreationDate_Q']).dt.total_seconds() / 60 / 60
df = merged_A_Q[merged_A_Q['timeDiffrence(Hours)'] > 0]


merged_A_Q['timeDiffrence(Hours)'] = (merged_A_Q['CreationDate_A'] - merged_A_Q['CreationDate_Q']).dt.total_seconds() / 60 / 60
df = merged_A_Q[merged_A_Q['timeDiffrence(Hours)'] > 0]
correlation = df['timeDiffrence(Hours)'].corr(df['accepted_flag'])
sns.scatterplot(x='accepted_flag', y='timeDiffrence(Hours)', data=df, color="lime")
plt.title('Correlation between timeDiffrence(Hours) and accepted flag')
plt.xlabel('accepted flag')
plt.ylabel('timeDiffrence(Hours)')
plt.savefig('Result question 7-1.png', dpi=300, bbox_inches='tight')
plt.show()

df = df.copy()

df.loc[:, 'Bin'] = pd.cut(df['timeDiffrence(Hours)'], 6)

mean_scores = df.groupby('Bin', observed=False)['accepted_flag'].mean()

plt.figure(figsize=(7, 5))
sns.barplot(x=mean_scores.index, y=mean_scores.values)
plt.title('Mean accepted flag for Each Bin Range')
plt.xlabel('timeDiffrence(Hours) Ranges')
plt.ylabel('Mean accepted flag ')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Result question 7-2.png', dpi=300, bbox_inches='tight')
plt.show()
