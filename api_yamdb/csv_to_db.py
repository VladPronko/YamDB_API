import csv
import sqlite3

path = 'db.sqlite3'

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/genre.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['slug']) for i in dr]
cur.executemany(('INSERT INTO reviews_genre (id, name, slug) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/category.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['slug']) for i in dr]
cur.executemany(('INSERT INTO reviews_category (id, name, slug) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/titles.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['year'], i['category_id']) for i in dr]
cur.executemany(('INSERT INTO reviews_title (id, name, year, category_id) '
                 'VALUES (?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/genre_title.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['title_id'], i['genre_id']) for i in dr]
cur.executemany(('INSERT INTO reviews_title_genre (id, title_id, genre_id) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/review.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['text'], i['score'], i['pub_date'],
              i['author_id'], i['title_id']) for i in dr]
cur.executemany(('INSERT INTO reviews_review (id, text, score, pub_date, '
                 'author_id, title_id) VALUES (?, ?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/users.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['username'], i['email'], i['role'], i['bio'],
              i['first_name'], i['last_name'], i['is_staff'],
              i['is_superuser'], i['is_active'], i['password'],
              i['date_joined']) for i in dr]
cur.executemany(('INSERT INTO reviews_user (id, username, email, role, bio, '
                 'first_name, last_name, is_staff, is_superuser, is_active, '
                 'password, date_joined) '
                 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('static/data/comments.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['review_id'], i['text'], i['author_id'],
              i['pub_date']) for i in dr]
cur.executemany(('INSERT INTO reviews_comment (id, review_id, text, author_id,'
                 ' pub_date) VALUES (?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()
