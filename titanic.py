import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

sns.countplot(data=train , x="Survived")
plt.title("Survival Count")
plt.show()

sns.countplot(data=train, x='Pclass', hue='Survived')
plt.title("Survival by Passenger Class")
plt.show()

sns.histplot(data=train, x='Age', hue='Survived', kde=True)
plt.title("Age Distribution by Survival")
plt.show()

