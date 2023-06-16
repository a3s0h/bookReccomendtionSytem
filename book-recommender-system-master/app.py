from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from fuzzywuzzy import process

popular_df = pd.read_pickle('popular.pkl')
pt = pd.read_pickle('pt.pkl')
books = pd.read_pickle('books.pkl')
similarity_scores = pd.read_pickle('similarity_scores.pkl')

default_image_url = 'https://example.com/default_image.jpg'  # Replace with your own default image URL

app = Flask(__name__)


@app.route('/')
def index():
    default_image_url = "default_image.jpg"  
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           default_image_url=default_image_url
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    if user_input not in pt.index:
        # Perform fuzzy search to find similar book names
        matches = process.extract(user_input, pt.index, limit=5)
        similar_books = [match[0] for match in matches]
        similar_books_data = []
        
        for similar_book in similar_books:
            temp_df = books[books['Book-Title'] == similar_book]
            author_name = list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)[0]
            image_url = list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)[0]
            similar_books_data.append([similar_book, author_name, image_url or default_image_url])
        
        return render_template('recommend.html', data=similar_books_data)

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
