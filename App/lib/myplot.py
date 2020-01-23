import io
import seaborn as sns
import matplotlib.pyplot as plt
import base64

class Myplot:
    def __init__(self, datasource):
        self.__datasource = datasource

    def plot(self):
        img = io.BytesIO()
        sns.set(style="whitegrid")
        # Initialize the matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 15))
        fig.suptitle('Horizontally stacked subplots')
        # Plot the crashes where alcohol was involved
        # sns.set_color_codes("muted")
        g = sns.barplot(
            y=list(self.__datasource.keys()),
            x=list(self.__datasource.values())
        )

        for i, v in enumerate(list(self.__datasource.values())):
            g.text(v + 3, i + .25, str(v), color='orange')

        # Add a legend and informative axis label
        ax.legend(ncol=2, loc="lower right", frameon=True)
        ax.set(xlim=(0, 24), ylabel="", xlabel="Word")
        sns.despine(left=True, bottom=True)

        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)

        return base64.b64encode(img.getvalue()).decode("utf-8")
