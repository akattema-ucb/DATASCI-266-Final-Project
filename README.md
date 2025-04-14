# DATASCI 266 Final Project
#### Spring 2025
#### Achintya Kattemalavadi (akattema@berkeley.edu)

This repository contains the work for the project "Multi-Label GitHub Issue Classification", completed as the final project for the DATASCI 266 NLP course in the MIDS program, spring 2025 term.

## Files Included
The files in this dataset, in the order they are used, are:
1. `construct_dataset.ipynb`: Construct the dataset on which the models in this project were trained.
1. `eda_and_split.ipynb`: Do some basic EDA on the dataset, resample the data to deal with label class imbalance, and split the dataset into train, validation, and test sets.
1. `reformat_ds_for_huggingface.py`: Script to convert the dataset to a format which works with HuggingFace transformers, specifically with a `text` string field and a `labels` list (one-hot encoded) field.
1. `experiments.ipynb`: The actual training, testing, and evaluation code for the models in this project.

The datasets for this project are located here: https://drive.google.com/drive/folders/1tJHJNBUcfgi0H-idfsHRtkaFNsjiBZMq?usp=share_link