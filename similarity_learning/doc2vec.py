#Import packages
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import os
import natsort

filenames = os.listdir('./txt')
#Create empty list to store file contents
doc = []

for filename in natsort.natsorted(filenames,reverse=False):
    with open(os.path.join('./txt', filename)) as file:
        content = file.read()
        doc.append(content.lower())       

# Tokenization of each document
tokenized_doc = []
for d in doc:
    tokenized_doc.append(word_tokenize(d.lower()))

# Convert tokenized document into gensim formated tagged data
tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_doc)]
    
## Train doc2vec model
model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, workers=4, epochs = 100)
# Save trained doc2vec model
model.save("sl_doc2vec.model")
## Load saved doc2vec model
model= Doc2Vec.load("sl_doc2vec.model")

# # find most similar doc 
test_doc = word_tokenize("work page profile update".lower())
# print(model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5))

print("The top 5 similar requirements are: \n")
result = model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5)
for i in result:
    print(doc[i[0]]+'('+str(i[1])+')')

# for tag in model.docvecs.doctags.keys():
#     print("the vectors  "+ str(tag, model.docvecs[tag]))  # Prints the learned numpy array for this tag

## Print model vocabulary
# print(str(model.wv.vocab))