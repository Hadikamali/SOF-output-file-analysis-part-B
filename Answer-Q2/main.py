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

correlation = questions['ViewCount'].corr(questions['CommentCount'])
print(correlation)

sns.scatterplot(x=questions['ViewCount'], y=questions['CommentCount'], data=questions)
plt.title('Correlation between ViewCount and CommentCount')
plt.xlabel('ViewCount')
plt.ylabel('CommentCount')
plt.savefig('Result question 2.png', dpi=1200, bbox_inches='tight')
plt.show()