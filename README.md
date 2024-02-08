# Language-Identifier-From-Text

## Overview

This repository contains a Python program for identifying the language of a given text based on letter frequency analysis. It differentiates between English and Spanish using probabilistic models and multinomial parameter vectors.

## Features

Probability Vector Parsing: Parses predefined probability vectors for English (e.txt) and Spanish (s.txt), representing the likelihood of each letter's occurrence in these languages.

Text Shredding: Analyzes a text file to count the occurrences of each uppercase letter from 'A' to 'Z', preparing the data for language identification.

Logarithmic Probability Computation: Utilizes logarithmic transformations to compute probabilities, enhancing numerical stability and avoiding underflow issues common in probability calculations.

Bayesian Language Identification: Employs Bayes' rule combined with the calculated log probabilities to ascertain the text's most likely language, taking prior probabilities into account.

## Getting Started

Ensure you have Python 3.x installed on your system. Place your text files (e.txt and s.txt for English and Spanish probabilities, respectively, and the text file you wish to analyze) in the same directory as the script.

Clone this repository:

git clone https://github.com/DeboJp/Language-Identifier-From-Text.git

Navigate to the repository folder:

cd Language-Identifier-From-Text

Run the script with the name of the text file you want to analyze:

python LanguageIdentifier.py letter0.txt

## How It Works

The program begins by reading the language probability vectors from e.txt and s.txt.
It then "shreds" the input text, counting each letter's occurrences and transforming this data into a format suitable for analysis.
Using the computed letter counts and the language probability vectors, the program calculates the log probabilities for each language.
Finally, it identifies the text's language by comparing these probabilities, outputting the most likely language and the probability of the text being in English.

## Contributing

Contributions to improve the accuracy or efficiency of this language identification program are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

