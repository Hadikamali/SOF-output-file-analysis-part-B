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
users = read_file('Data/U.csv', encoding="utf-16")

badge_count = user_badge.groupby('UserId').size().reset_index(name='badgeCount')
badge_count

user_badge = pd.merge(users, badge_count, left_on='Id', right_on='UserId', how='inner')
sns.scatterplot(x='badgeCount', y='Reputation', data=user_badge, color="yellow")
plt.title('Correlation between badgeCount and Reputation')
plt.xlabel('badgeCount')
plt.ylabel('Reputation')
plt.savefig('Result question 6.png', dpi=1200, bbox_inches='tight')  # Save the scatter plot as a PNG file
plt.show()

correlation = user_badge['badgeCount'].corr(user_badge['Reputation'])
correlation
