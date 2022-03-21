import nltk
from nltk.corpus.reader import TaggedCorpusReader
from pickle import dump, load

"""
Given a language file and a POS tagged corpus, return a model that can be used
to tag words.
@param {string} corpus_root - the path to the langauge file containing the
training file
@param {string} train_file - the file inside the corpus_root containing the the
tagged corpus
"""


def create_model(corpus_root, train_file):
    text_tagged = TaggedCorpusReader(corpus_root, ".txt")
    sent_tag = text_tagged.tagged_sents(train_file)

    t0 = nltk.DefaultTagger('NOUN')
    t1 = nltk.UnigramTagger(sent_tag, backoff=t0)
    t2 = nltk.BigramTagger(sent_tag, backoff=t1)
    return t2


"""
Given a tagging model and a file destination, write it to a file
@param {Object} model - the model we are exporting
@param {string} file_path - the file path we are exporting to
"""


def export_model(model, file_path):
    with open(file_path, 'wb') as out_file:
        dump(model, out_file, -1)


"""
Given a file containing a taggin model, return that model
@param {string} file_path - the file containing the tagging model
"""


def import_model(file_path):
    with open(file_path, 'rb') as in_file:
        tagger = load(in_file)
    return tagger


"""
Given a file with sentences in the "language", return the tagges sentences
@param {Object} model - the tagging model we use to tag
@param {string} text_path - the file containg the text to tag
"""


def tag_file(model, text_path):
    with open(text_path) as txt:
        content = txt.read().replace("\n", " ")

    tokens = content.split()
    tagged_tokens = model.tag(tokens)
    return tagged_tokens
