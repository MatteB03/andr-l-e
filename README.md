# Introduction
Since Massimiliano Stignani and Satilde Mandoni commented on the bad structure of the README.md of a one hour project made for fun for dear friends of mine, here is the "detailed" description of this project.

# Context and data used
Andr-l-e is a very easy (but not enough to have a farfetched README.md it seems) language identifying game inspired by previous state-of-art trial and error benchmarks like Wordle and Flagle (I know it is completely different and not hint-based but the -le is there so trust me it will be fun).
The data used in the project is the WiLi_2018 dataset (https://huggingface.co/datasets/MartinThoma/wili_2018), which contains a total of 235000 paragraphs of 235 languages. The paragraphs are split in 117500 training and 117500 testing paragraphs, and each paragraph is assigned the label of the corresponding languages. 

# Files and game
The training paragraphs and labels are stored in the `x_train.txt` and `y_train.txt` files respectively, and the same goes for test data. Since the goal is user identification, the training and test sets are merged into a single dataset.
The main file, and the only one to be run, is `play.py`. It merges the dataset (future releases will take the whole set for the sake of efficiency but for now be patient), uses file `labels.csv` to create a dictionary of all labels to allow players to write the name of a language instead of memorizing the whole list of labels, then chooses a random paragraph and asks the player to guess which language it is in a prescribed number of tries. If they guess the language, the game ends. If they end their tries, the correct language is displayed. Simple AND not addictive, if Wordle is a cigarette this is a brick of tungsten in your mouth. Have fun.
