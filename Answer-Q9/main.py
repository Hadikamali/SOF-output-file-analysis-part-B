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


correlation = questions['ViewCount'].corr(questions['Score'])
plt.scatter(questions['ViewCount'], questions['Score'], color="darkred")
plt.title('Correlation between ViewCount and Score')
plt.xlabel('ViewCount')
plt.ylabel('Score')
plt.savefig('Result question 9.png', dpi=300, bbox_inches='tight')
print(correlation)
plt.show()