import MySQLdb
conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

# c = conn.cursor()
# c.execute('DROP TABLE IF EXISTS cities')
# c.execute("""CREATE TABLE cities ('rank' integer,'city' text,'population' integer)""")
# c.execute('INSERT INTO cities VALUES (%s, %s, %s)',(1,'上海',24150000))
# c.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',{'rank': 2, 'city': 'カラチ', 'population':23500000})
# c.executemany()('INSET INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', [{'rank': 3, 'city':'北京','population':21516000},{'rank': 4, 'city':'天津','population':14722100},{'rank': 5, 'city':'イスタンブル','population':14160467}])

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS `cities`")
cursor.execute('''CREATE TABLE IF NOT EXISTS `cities` (
    `id` integer NOT NULL,
    `city` text,
    `population` integer,
    PRIMARY KEY (id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')
 
cursor.execute('INSERT INTO cities VALUES (%s, %s, %s)',(1,'上海',24150000))
cursor.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',{'rank': 2, 'city': 'カラチ', 'population':23500000})
cursor.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', [{'rank': 3, 'city':'北京','population':21516000},{'rank': 4, 'city':'天津','population':14722100},{'rank': 5, 'city':'イスタンブル','population':14160467}])


conn.commit()

cursor.execute('SELECT * FROM cities')
for row in cursor.fetchall():
	print(row)

conn.close()