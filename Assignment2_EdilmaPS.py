#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('machine_data.csv')
print(df)
print(df.shape)
#%%
grpByManu = df.groupby(['manufacturef'])
dfa = grpByManu.get_group(('A',))
dfa = grpByManu.get_group(('B',))
dfa = grpByManu.get_group(('c',))
#%%
loada = dfa['load']
timea = dfa['time']
#%%
manufA = grpByManu.get_group(('A',))
manufB = grpByManu.get_group(('B',))
manufc = grpByManu.get_group(('c',))
#%%
plt.scatter(manufA['load'], manufA['time'], label='A', alpha=0.6)
plt.scatter(manufB['load'], manufB['time'], label='B', alpha=0.6)
plt.scatter(manufc['load'], manufc['time'], label='c', alpha=0.6)
plt.title("Load vs Time by Manufacturer")
plt.xlabel("Load")
plt.ylabel("Time")
plt.legend()
plt.show()
#%%
df['manufacturef'] = df['manufacturef'].astype('string').str.upper()
plot_df = df.dropna(subset=['manufacturef'])

order = sorted(plot_df['manufacturef'].unique())
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=plot_df, x='manufacturef', y='load', order=order, ax=axes[0])
axes[0].set_title("Load Distribution by Manufacturer")
axes[0].set_xlabel("")
axes[0].set_ylabel("Load")

sns.boxplot(data=plot_df, x='manufacturef', y='time', order=order, ax=axes[1])
axes[1].set_title("Time Distribution by Manufacturer")
axes[1].set_xlabel("")
axes[1].set_ylabel("Time")

plt.tight_layout()
plt.show()
#%%
