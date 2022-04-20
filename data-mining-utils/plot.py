#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_stacked_bar_plot(sample, attribute, ax, title=None, font_size=12):
    """
    Generates a stacked bar plot for a single category. This method utilizes the DataFrame.append()
    method which is deprecated.

    Parameters
    ----------
    sample: Collection
    attribute: str
        Attribute to create stacked plot for
    ax: plt.axes.Axes
    title: str (default is None)
    font_size: int (default is 12)

    Returns
    -------
    plt.axes.Axes
    """
    df = pd.DataFrame().append(pd.DataFrame(sample).value_counts(attribute), ignore_index=True)
    df.plot.bar(
        stacked=True,
        ax=ax,
        title=title,
        xlabel=None,
        ylabel="Count",
        fontsize=font_size,
        legend=True,
    ).xaxis.set_visible(False)
    return ax


def generate_confusion_matrix(y, ax, colormap="flare", font_size=12):
    cf_mtx = sns.heatmap(y, annot=True, cmap=colormap, ax=ax)
    cf_mtx.set_xlabel("Predicted", fontsize=font_size)
    cf_mtx.set_ylabel("Actual", fontsize=font_size)


if __name__ == "__main__":
    sample = [{"jawn": t} for t in ["j", "j", "k", "j"]]
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    generate_stacked_bar_plot(sample, "jawn", ax[0])

    y = [[1, 2], [0, 3]]
    generate_confusion_matrix(y, ax[1])

    plt.show()
