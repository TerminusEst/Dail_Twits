import pandas as pd
import seaborn as sns; sns.set()
import parties
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime as dt


def plot_bar(df, column):
        
        df = df.sort_values(by=column)

        legend_patches = []

        for i in parties.colour:

                patch = mpatches.Patch(color=parties.colour[i], label=i)
                legend_patches.append(patch)


        labels = [i.get_label() for i in legend_patches]

        df[column].plot(kind='bar', color=df.Colour, fontsize=7)
        plt.ylabel(column)
        plt.legend(legend_patches, labels, loc=2)
        plt.show()


df = pd.read_csv('twit_stats.csv', parse_dates=[5])

df = df[df.Followers != 0]
df = df[df.Handle != 'None']


plot_bar(df, 'Followers')
plot_bar(df, 'Tweets')

df['Created'] = pd.to_datetime([i for i in df.Created], yearfirst=True)
df = df.sort_values(by='Created')

plt.plot(df.Created, range(len(df)))

plt.ylim([0,166])
plt.xlim([dt.date(2006, 3, 21), dt.datetime.now()])
plt.ylabel('Number of TDs on Twitter')
plt.xlabel('Date')


df = df[(df.Party != 'ULP') & (df.Party != 'CC') & (df.Party != 'WUA')]
df.boxplot(column='Followers', by='Party')

plt.ylim([0,30000])
plt.ylabel('Followers')
plt.show()

