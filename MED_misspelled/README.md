# Minimum Edit Distance
The edit distance **(example Lavenshtein distance)**, measures the dissimilarity between two strings by calculating the minimum number of single-character edits needed to transform one string into the other. These edits include insertions, deletions, and substitutions. It serves as a metric for comparing the similarity of strings or words, often used in applications such as spell checking, DNA sequencing, and natural language processing.

In this work we have used **(Lavenshtein distance)** algorithm to find the correct spelling of misspelled words in the  Roger Mitton **Birkbeck PERIN2DAT.643** corpus and **WordNet** from NLTK as dictionary

## The Data
Two files, [SHEFFIELDDAT.643](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Data/SHEFFIELDDAT.643) and [FAWTHROP1DAT.643](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Data/FAWTHROP1DAT.643), out of the Birkbeck spelling error corpus by Roger Mitton was used for this experiment. They contain 1,193 words misspelled words in total and the correct equivalent of these words.

The WordNet dictionary contains 147,306 words.

## Requirements
You can find the modules and libraries used in this project in the [requirements.txt](https://github.com/BatMrE/Natural-language-processing/blob/main/MED_misspelled/requirements.txt) file.
```
pip install -r requirements.txt
```

## Files
* **[notebook file](https://github.com/BatMrE/Natural-language-processing/blob/main/MED_misspelled/Data/edit_distance.ipynb):** contains notebook with all functions and operations

* **[py file](https://github.com/BatMrE/Natural-language-processing/blob/main/MED_misspelled/Data/main.py):** contains python file with supporting file in src folder
