# BookReccomendtionSytem

##Overview
Three robust recommendation systems are used here:

Popularity Based: Discover trending and popular books.
Content Based: Get recommendations based on the content you love.
Collaborative Based: Dive into a world of recommendations from like-minded readers.


##Getting Started
##Prerequisites
Make sure you have the following installed:

Flask
NumPy
Pandas
Gunicorn
You can install these dependencies by running:

##bash
pip install -r requirements.txt

Data Source
url : https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

##Usage
Clone the repo:

##bash
git clone https://github.com/your-username/BookRec.git
cd BookRec
Install dependencies:

##bash
pip install -r requirements.txt
Run the app:

##bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
Visit http://localhost:5000 in your browser and start exploring personalized book recommendations.

Models
Popularity Based: Straight from the reading trends.
Content Based: Tailored recommendations based on your favorite genres.
Collaborative Based: Join the community and discover books loved by others with similar tastes.
