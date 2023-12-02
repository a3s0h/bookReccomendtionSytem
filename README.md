# BookReccomendtionSytem

<h2>Overview</h2>
Three robust recommendation systems are used here:

Popularity Based: Discover trending and popular books.
Content Based: Get recommendations based on the content you love.
Collaborative Based: Dive into a world of recommendations from like-minded readers.


<h2>Getting Started</h2>
<h2>Prerequisites</h2>
Make sure you have the following installed:

Flask
NumPy
Pandas
Gunicorn
You can install these dependencies by running:
```bash
$ pip install -r requirements.txt
```
Data Source
url : https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

<h2>Usage</h2>
Clone the repo:

```bash
$ git clone https://github.com/your-username/BookRec.git
$ cd BookRec
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

Run the app:
```bash
$ gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
Visit http://localhost:5000 in your browser and start exploring personalized book recommendations.

<h2>Models used</h2>
<ul>
<li>Popularity Based: Straight from the reading trends.</li>
<li>Content Based: Tailored recommendations based on your favorite genres.</li>
<li>Collaborative Based: Join the community and discover books loved by others with similar tastes.</li>
</ul>
