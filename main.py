import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv('sales_data.csv')
print(df.head())

df_sales = df['Sales']
df_sales_mean = df_sales.mean()
print(df_sales_mean)

#need to visualation
sns.scatterplot(x='Website-Traffic', y='Sales', data=df)
plt.show()