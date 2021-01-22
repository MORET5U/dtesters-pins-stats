import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ujson as uj

# Load the data
with open("data.json", "r", encoding="utf-8") as fp:
    data = uj.load(fp)

new_data = []
for day, queries in data.items():
    for query, results in queries.items():
        commit = {"day": day, "query": query, "results": results}
        new_data.append(commit)

df = pd.json_normalize(new_data, max_level=0)

# Time to display ¯\_(ツ)_/¯
sns.set_theme(style="whitegrid")
g = sns.catplot(
    data=df,
    kind="bar",
    hue="query",
    x="day",
    y="results",
    ci="cd",
    alpha=0.8,
    height=6,
    palette="crest",
)
g.despine(left=True)
g.set_axis_labels("Days", "Results found (amount)")
g.legend.set_title("Queries")

plt.show()
