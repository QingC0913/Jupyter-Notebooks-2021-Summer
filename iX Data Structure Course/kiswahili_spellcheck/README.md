# kiswahili_spellcheck

Normalize Corpus
-----

The Normalize Corpus.ipynb file takes in the text corpus sw_string.txt file and outputs the following three files:
  1. sw_corpus_tokenized.txt 
  2. sw_frequency.csv
  3. sw_training.txt
  
 The first file was used to calculate the frequencies of all words in the text corpus sw_string.txt, which were 
 then saved in the sw_frequency.csv file. This was for personal use to check the most frequent words and the most 
 frequent pairs, triplets, and quadruplets of words in our text corpus. 
 
 The grammar rules utilized to manually tag the data was from the Swahili Wikipedia page, which can be found here:
 * [Swahili Grammar](https://en.wikipedia.org/wiki/Swahili_grammar)
 
 Tags
 -----
 
 The following are the tags used in the sw_training.txt file:
 1. NOUN -> noun
 2. ADV -> adverb
 3. ADJ -> adjective
 4. DETER -> determiner
 5. PREP -> prepositions, pronouns, and conjunctions
 6. NUMBER -> numbers written in numerals (not spelled out)
 7. VERB -> verb
 
 Usage
 -----
 
 Clone the folder onto your local machine and ensure that your have latest version of python installed. Information for this 
 is easily available online.

 Download jupyter notebook to your local system with the following script:
 
 pip install notebook
 
 You can also run jupyter notebook through Anaconda and run the following script:
 
 conda install -c conda-forge notebook
 
 Open up terminal on your computer and move to the kiswahili_spellcheck file is:
 
 cd /Users/kgiomi/Downloads/kiswahili_spellcheck
 
 Then, run jupyter notebook:
 
 jupyter notebook
 
 A webpage should open, where you can open Normalize Corpus.ipynb. To run, click Cell -> Run All

 
 Next Steps for Normalize Corpus
 -----
 
 The Normalize Corpus file currently tags over 400,000 words, which makes up a sizeable training set, but the grammar 
 rules and the manually tagged data used in the Normalize Corpus.ipynb file should be checked by a native Swahili speaker.
 The accuracy isn't 100%, but with a check, there shouldn't be many changes to be made after the rules are checked over.
 
 The POSTagger.py tagging model can be improved, as there are more state-of-the-art tagging models out there with higher
 levels of accuracy than the Bigram tagger that is created.
