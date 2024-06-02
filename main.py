import com
import speech_recognition as sr
import time

while 1:

    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

        com.callback(listener, input_speech)
     










# import spacy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import LinearSVC

# class Category:
#     BOOKS = "BOOKS"
#     BANK = "BANK"

# train_x = ["good characters and plot progression", "check out the book", "good story. would recommend", "novel recommendation", "need to make a deposit to the bank", "balance inquiry savings", "write a check"]
# train_y = [Category.BOOKS, Category.BOOKS, Category.BOOKS, Category.BOOKS, Category.BANK, Category.BANK, Category.BANK]

# tfidf_vectorizer = TfidfVectorizer()
# train_x_tfidf = tfidf_vectorizer.fit_transform(train_x)

# clf_svm = LinearSVC()
# clf_svm.fit(train_x_tfidf, train_y)

# test_x = ["check this story out"]
# test_x_tfidf = tfidf_vectorizer.transform(test_x)

# predicted_categories = clf_svm.predict(test_x_tfidf)
# for category in predicted_categories:
#     print(category)


# from scholarly import scholarly

# def search_and_summarize(query):

#     # Search for papers
#     search_query = scholarly.search_pubs('sun')
#     scholarly.pprint(search_query)    # Extract relevant information from the search results
#     # for result in search_results:
#     #     title = result.bib['title']
#     #     abstract = result.bib['abstract']

#         # Summarize the abstract using NLP techniques
#         # (Replace this with your own NLP code)
#         # summaries = [sentence for sentence in abstract.split('.') if sentence[0] != 'Abstract']

#         # # Display or store the summaries as needed
#         # print(f"Title: {title}")
#         # print("Abstract:")
#         # for summary in summaries:
#         #     print(summary)
#         # print("\n")

# # Example usage
# search_and_summarize("sun")


# from scholarly import scholarly

# # Retrieve the author's data, fill-in, and print
# # Get an iterator for the author results
# search_query = scholarly.search_pubs('sun')
# # Retrieve the first result from the iterator
# pubs = list(search_query)
# print(pubs)
# # print([pub['bib']['title'] for pub in pubs])












# # from googlesearch import search
# from bs4 import BeautifulSoup
# import requests
# import re
# import time

# # import nltk
# # from nltk.corpus import stopwords
# # nltk.download('stopwords')

# query = "cpu wiki"

# # for j in search(query, num_results=1, sleep_interval=1):
# #     print(j)

# from googlesearch.googlesearch import GoogleSearch
# response = GoogleSearch().search(query)
# for result in response.results:
#     print("Title: " + result.title)
#     print("Content: " + result.getText())



# # url = j
# # result = requests.get(url).text
# # doc = BeautifulSoup(result, "html.parser")

# # for tags in doc.find_all('p'):

# #     text = tags.get_text()

# #     print(text)

