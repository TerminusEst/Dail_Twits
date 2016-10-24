import pandas as pd
import seaborn as sns.set()
import parties
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def plot_bar(df, column):
        
        df = df.sort([column])

        legend_patches = []

        for i in parties.colour:

                patch = mpatches.Patch(color=parties.colour[i], label=i)
                legend_patches.append(patch)


        labels = [i.get_label() for i in legend_patches]

        df[column].plot(kind='bar', color=df.Colour, fontsize=7)
        plt.ylabel(column)
        plt.legend(legend_patches, labels, loc=2)
        plt.show()


df = pd.read_csv('twit_stats.csv')

df = df[df.Followers != 0]

plot_bar(df, 'Followers')
plot_bar(df, 'Tweets')

df = df[(df.Party != 'ULP') & (df.Party != 'CC') & (df.Party != 'WUA')]
df.boxplot(column='Followers', by='Party')

plt.ylim([0,30000])
plt.ylabel('Followers')
plt.show()
