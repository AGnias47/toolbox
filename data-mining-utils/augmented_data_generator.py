#!/usr/bin/env python3

from utils.data import read_sample, write_sample
from pathlib import Path
import nlpaug.augmenter.word as naw

augmenter = naw.ContextualWordEmbsAug(model_path="bert-base-uncased", action="substitute")


def augment_class(path="data/labelled", classes_to_augment=("pr", "au"), output_fname="pro-russia"):
    """
    Loads data from files into a list of dicts

    Parameters
    ----------
    path: str
    classes_to_augment: tuple
    output_fname: str

    Returns
    -------
    Collection
        List of tweets stored as dicts
    """
    sample = list()
    augmented_sample = list()
    for fpath in Path(f"{path}/sia").glob("*.twint"):
        sample += read_sample(str(fpath), label=True)
    for fpath in Path(f"{path}/cluster").glob("*.twint"):
        sample += read_sample(str(fpath), label=True, cluster=True)
    for s in sample:
        if s.label in classes_to_augment:
            s.raw_content = augmenter.augment(s.raw_content)
            augmented_sample.append(s)
    write_sample(fname=f"data/labelled/augmented/{output_fname}.twint", tweets=augmented_sample, label=True)
    return augmented_sample


if __name__ == "__main__":
    augment_class()
