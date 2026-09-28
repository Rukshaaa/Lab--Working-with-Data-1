#!/usr/bin/env python
# coding: utf-8

# # Working with Data Lab 1
# 
# ## 🔍 Overview
# The lab is designed to be self-guided, providing solutions for each exercise to check your work and assist if you get stuck. However, it is important to first attempt to solve the problem on your own as this is the best way to learn. If you become stuck, don't give up and seek help from the instructor, peers, or even a search engine like Google. Be mindful that not all answers from a search engine may be correct, so use your judgement to determine the validity of the information. Remember, the best way to learn is to try solving the problem yourself first.
# 
# ### 🎯 Objectives
# This lab will introduce you to the basics of working with data in Python. You will learn:
# - how to read and write data from and to a file
# - how to use the `pandas` library to work with data in a `DataFrame`
# - how to read data from CSV file (local and remote)
# - how to read data from SQL Database

# In[ ]:


# We will keep coming back to this cell to add "import" statements, and configure libraries as we need
import pandas as pd
import numpy as np

from urllib.request import urlretrieve
from zipfile import ZipFile


# Configure pandas to display 500 rows; otherwise it will truncate the output
pd.set_option('display.max_rows', 500)


# ## Part 1: Reading and Writing Data to files

# ### Exercise 1
# In the following code block, create a file called `text.txt` and write the following text to the file: `This is a test file.`
# 
# This is achieved by 3 steps:
# 1. Open the file for writing using the `open()` function
# 2. Writing to the file using the `write()` function
# 3. Closing the file using the `close()` function
# 
# <details>
#   <summary>Hints</summary>
# 
#   * End the line with a newline character `\n` to ensure that any new text is written on a new line.
#   * The `open()` function is a built-in Python function that is used to open a file. It takes two arguments: the first is the file name, and the second is the mode in which to open the file. The mode 'r' is for reading, 'w' is for writing, 'a' is for appending to the file.
#    * The `write()` function is a method of the file object, which is returned by the `open()` function. It is used to write a string to the file.
#    * The `close()` function is also a method of the file object and it is used to close the file after it's done, it will release the resources associated with the file.
# </details>

# In[1]:


# Open File with a "write" mode (ideally, the file should be saved to the data folder)
file = open("data/text.txt", "w")

# write the text to the file
file.write("This is a test file.\n")

# close the file
file.close()


# <details>
#   <summary>💡 Solution (You don't learn if you just look at this, struggle a bit before you open this)</summary>
# 
#   ```python
#   f = open('data/text.txt', 'w')
#   f.write('This is a test file.\n')
#   f.close()
#   ```
# </details>
# 

# ### Exercise 2
# In the previous task, you were required to manually open and close the file, which is not the most efficient way to handle files. A more efficient way is to use the `with()` statement. It automatically closes the file after the block of code is finished executing. 
# 
# For example, instead of writing:
# 
# ```python
# file = open('example.txt', 'r')
# contents = file.read()
# file.close()
# ```
# You can write:
# 
# ```python
# with open('example.txt', 'r') as file:
#     contents = file.read()
# ```
# 
# In the following code block, **Append** to the same file, `text.txt`, the following text: `This is a second line.` using the `with()` statement.

# In[2]:


# using the "with" statement, append to the same file the following text: "This is a second line."
with open('data/text.txt', 'a') as f:
    f.write('This is a second line.\n')


# In[3]:


with open('data/text.txt', 'r') as f:
    print(f.read())


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   with open('data/text.txt', 'a') as f:
#       f.write('This is a second line.')
#   ```
# </details>

# ### Exercise 3
# Create a file called data.txt and write multiple lines of numbers to it. Each line should contain 2 numbers separated by a tab. The first number should be an increment of 2 starting from 2, and the second number should be the first number raised to the power of 3 (3). Only use numbers from 2 to 20. The file should look like this:
# ```
# 2	8
# 4	64
# 6	216
# 8	512
# 10	1000
# 12	1728
# 14	2744
# 16	4096
# 18	5832
# 20	8000
# ```
# <details>
#   <summary>Hints</summary>
#   
#   * You may need to use a loop to iterate over a range of numbers (2-20)
#   * You can use the `range()` function to generate a sequence of numbers for your loop
#     * The `range` method takes 3 arguments: the start, the stop, and the step. The start is the first number in the sequence, the stop is the last number in the sequence (non-inclusive), and the step is the difference between each number in the sequence.
#   * You can call the write function from within a for-loop
#   * You can't write an integer to a file, you need to convert it to a string first
#   * use the `with` statement to open the file.
#   * the file should be opened in write mode.
#   * to construct the line of (text) to send to your file, you can use: 
#     * string concatenation (e.g. `str1 + str2`)
#     * string-literals (f-strings) (e.g. `f'{str1}{str2}'`)
#     * `format()` method (e.g. `'{}{}'.format(str1, str2)`)
#  
# </details>

# In[4]:


with open('data/data.txt', 'w') as file:
    for i in range(2, 21, 2):
        file.write(f"{i}\t{i ** 3}\n")


# In[5]:


with open('data/data.txt', 'r') as file:
    print(file.read())


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   with open('data/test-data.txt', 'w') as file:
#     for i in range(2, 21, 2):
#       file.write(f"{i}\t{i ** 3}\n")
#   ```
# </details>

# ### Exercise 4
# Read the file your created in the previous exercise and print the contents to the screen. The first column should be captured in an array called `x` and the second column should be captured in an array called `y`.
# 
# <details>
#   <summary>Hints</summary>
# 
#   * You can use the `readlines()` function to read all the lines in the file and store them in a list.
#   * You can use the `split()` function to split a string into a list of substrings.
#   * You can use the `append()` function to add an item to the end of a list.
#   * You can use the `strip()` function to remove whitespace and newline characters from the beginning and end of a string.
# 
# </details>

# In[6]:


x = []
y = []

with open('data/data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line_split = line.strip().split('\t')
        x.append(line_split[0])
        y.append(line_split[1])

print("X Array: ")
print(x)
print("Y Array: ")
print(y)


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   x = []
#   y = []
# 
#   with open('data/test-data.txt', 'r') as file:
#       lines = file.readlines()
#       for line in lines:
#           line_split = line.strip().split('\t')
#           x.append(line_split[0])
#           y.append(line_split[1])
# 
#   print("X Array: ")
#   print(x)
#   print("Y Array: ")
#   print(y)
#   ```
# </details>

# ### Exercise 5
# using the `x` and `y` arrays you created in the previous exercise, construct a pandas `DataFrame` called `test_df` with `x` and `y` as columns.
# 
# <details>
#   <summary>Hints</summary>
# 
#   * Make sure you import the pandas library (top cell of the notebook)
#   * You can use the [📜`DataFrame()` function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to create a new DataFrame.

# In[7]:


import pandas as pd 
test_df = pd.DataFrame({'x': x, 'y': y})

# Write your code above this line
test_df


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   test_df = pd.DataFrame({'x': x, 'y': y})
#   ```
# </details>

# ## Part 1': read and write files using pandas

# ### Exercise 1
# Read the previously generated file `data/test-data.txt` into a pandas DataFrame called `test_df2` using the `read_table()` function. 
# The file contains 2 columns of numbers separated by a tab. The first column is called `X` and the second column is called `Y`.
# 
# <details>
#   <summary>Hints</summary>
#   
#   * Make sure you import the pandas library (top cell of the notebook)
#   * You can use the [📜`read_table()` function](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html) to read a file into a DataFrame.
#   * since your file doesn't have a header line, make sure your set the `header` parameter to `None`.
# </details>

# In[8]:


test_df2 = pd.read_table('data/data.txt', header=None, names=('X', 'Y'))
# Write your code above this line
test_df2


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   test_df2 = pd.read_table('data/test-data.txt', header=None, names=('X','Y'))
#   ```
# </details>

# ### Exercise 2
# rewrite the `test_df2` DataFrame to a "Comma-Separated-File" (CSV) file called `data/test-data2.csv` using the `to_csv()` function.

# In[9]:


test_df2.to_csv('data/test-data2.csv', index=False)


# 📝: Check the data folder to make sure the file was created successfully

# 
# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   test_df2.to_csv('data/test-data.csv', index=False)
#   ```
# </details>

# ### Exercise 3
# Read a CSV file that's hosted remotely on the internet into a pandas DataFrame called `tips_df`. The file is located at the following URL: `https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv`

# In[10]:


url = "https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"
tips_df = pd.read_csv(url)

# Write your code above this line
tips_df


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   url = "https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"
#   tips_df = pd.read_csv(url)
# 
#   tips_df
#   ```
# </details>

# #### Side Bar: Downloading Datasets from Kaggle (1-Extra Credit)
# Kaggle.com is a go-to spot for data science and machine learning enthusiasts. It's packed with tons of datasets for competitions and tutorials, making it the perfect place for anyone looking to sharpen their skills.
# 
# Often, you may find yourself wanting to download a dataset from Kaggle to use in your own projects. One way to do this is to download the dataset from the website and then import it into your project. But if you don't want to download the dataset manually, you can use libraries like ([`opendatasets`](https://pypi.org/project/opendatasets/)) to download the datasets you need directly from Kaggle.
# 
# <details>
# <summary>To get Kaggle Credentials Setup: </summary>
# 
# 1. Create a Kaggle account
# 2. Get your API token. You can do this by going to the 'Account' tab in your Kaggle profile settings and clicking on 'Create API Token'. It will download the json file which contains the credentials.
# 3. Save the `json` file in the same directory as your notebook and rename it to `kaggle.json`. your credentials should now be read automatically by the [`opendatasets`](https://pypi.org/project/opendatasets/) library.
# 
# ⚠️ Note that the `kaggle.json` file contains your Kaggle API credentials in plain text.
# - Make sure you don't upload it to a public repository or share it with anyone. 
# - There's nothing super secret here yet, but this is the right practices.
# - Also I added `kaggle.json` to `.gitignore` file so it won't be uploaded to GitHub.
# </details>
# 
# For 3 points of Extra Credit, follow the instructions on the [`opendatasets`](https://pypi.org/project/opendatasets/) documentation, to download the following datasets from kaggle.com
# - [Law School Admissions & Bar Passage](https://www.kaggle.com/danofer/law-school-admissions-bar-passage)
# - [US Election Dataset](https://www.kaggle.com/datasets/tunguz/us-elections-dataset)
# 
# Once the file is downloaded, you can read it into a pandas DataFrame using the `read_csv()` function from the local file.
# 
# ```python
# df = pd.read_csv('data/law-school-admissions-bar-passage/bar_pass_prediction.csv')
# ```

# In[15]:


get_ipython().system('pip install opendatasets')


# In[16]:


import opendatasets as od

od.download("https://www.kaggle.com/danofer/law-school-admissions-bar-passage", data_dir="data")
od.download("https://www.kaggle.com/datasets/tunguz/us-elections-dataset", data_dir="data")


# In[17]:


df = pd.read_csv('data/law-school-admissions-bar-passage/bar_pass_prediction.csv')
df.head()


# 🚩 If you haven't already been updating committing your code to GitHub, this is a reminder to do so.

# ## Part2: Reading a Writing Data From SQL
# 
# SQL (Structured Query Language) is a programming language used to manage and manipulate relational databases. It is used to create, modify, and query databases. There are different dialects of SQL, such as MySQL, PostgreSQL, and Microsoft SQL Server, that may have slight variations in syntax and features. However, the basic structure and functionality of SQL remains the same across different dialects. These dialects are specific to certain relational database management systems (RDBMS) and are optimized to work with those systems.
# 
# One Variation of this Dialect is called SQLite. It is a software library that provides a relational database management system. Unlike other SQL dialects, SQLite is a self-contained, serverless, zero-configuration, and transactional SQL database engine. SQLite is lightweight, fast, and easy to use, and it doesn't have the overhead or complexity of other SQL dialects, making it a good choice for small to medium-sized projects.
# 
# In the following exercise, we will be using SQLite to practice reading and writing data from a database. The same concepts can be applied to other SQL dialects.

# ## Downloading a SQLite Database
# This code snippet below is downloading a file called "chinook.zip" from a website, then it decompressed the zip file and extracts all of its contents to the "data" directory. 
# 
# The first line imports the `urlretrieve` function from the `urllib.request` library, which is used to download the file. 
# The second line imports the ZipFile class from the zipfile library, which is used to handle the downloaded zip file.
# 
# **⚠️ This is a bad Practice:**
# IDEALLY, you should make those imports in the imports cell at the top of the notebook. But for the sake of simplicity, we will be importing them here.
# 
# 
# The next line uses the urlretrieve function to download the "chinook.zip" file, and assigns it to a variable called "file_handle". 
# After that, it creates an instance of the ZipFile class, passing the "file_handle" variable as the first argument, and the string "r" as the second argument, which indicates that the file should be opened in read mode. 
# The next line calls the extractall() method on the zipfile object, passing the directory "./data" as the argument, which extracts all the files inside the zip file to that directory. Finally, it calls the close() method on the zipfile object to close the zipfile.

# In[ ]:


from urllib.request import urlretrieve
from zipfile import ZipFile

file_handle, _ = urlretrieve('https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip')
zipfile = ZipFile(file_handle, 'r')
zipfile.extractall('./data')
zipfile.close();


# In[22]:


# Above code was not working for me
from urllib.request import Request, urlopen
from zipfile import ZipFile
from io import BytesIO

url = 'https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as response:
    zip_bytes = response.read()

with ZipFile(BytesIO(zip_bytes), 'r') as zipfile:
    zipfile.extractall('./data')


# ## Exercise 1: Create a connection to the chinook database (solved)
# 

# In[28]:


get_ipython().run_line_magic('pip', 'install sqlalchemy')


# In[29]:


from sqlalchemy import create_engine
# This time, I'm providing the code to set up the database connection
from sqlalchemy import create_engine

# For different databases, the connection string will be different. For a SQLite saved in the data folder, the connection string is:
connection_string = 'sqlite:///data/chinook.db'
engine = create_engine(connection_string)

db_connection = engine.connect()
# We will be using this variable to make queries to the database



# ❓**Point out one bad practice in the snippet above.** (Write your answer here)

# This is the database diagram for the Chinook database. It shows the tables and the relationships between them.
# ![Chinook Database Diagram](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)
# 
# #### Sample
# Here's an example of how you can read a SQLite database into a pandas DataFrame.
# 
# ```python
# # Note that db_connection is a variable that contains the connection to the database
# albums = pd.read_sql_query("SELECT * FROM albums", db_connection)
# ```
# 
# if the sql query is too long and you want to write it in multiple lines, you can use triple quotes to write it in multiple lines.
# 
# ```python
# albums = pd.read_sql_query(
#   """
#   SELECT *
#   FROM albums
#   """, db_connection)
# ```

# ### Exercise 2: 
# Read everything (*) in the `genres` table into a pandas DataFrame called `genres_df`

# In[30]:


genres_df = pd.read_sql(sql='SELECT * FROM genres;', con=db_connection)

# Write your code above this line
genres_df


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   genres_df = pd.read_sql(sql='SELECT * FROM genres;', con=db_connection)
#   ```
# </details>

# ### Exercise 3:
# Write a query to get all the albums the contained tracks with the word "tomorrow" in their titles. Read the results into a pandas DataFrame called `albums_df`
# The query should return the following columns: `AlbumTitle`, `TrackName`, `ArtistId`
# 
# <details>
#   <summary>Hints</summary>
# 
#   * Your query will need to join the `albums` and `tracks` tables.
#     * Look at the diagram above to see how the tables are related.
#   * You may need to use the `LIKE` keyword in your sql query
# </details>
# 

# In[31]:


sql = '''
SELECT
    a.Title AS AlbumTitle,
    t.Name AS TrackName,
    a.ArtistId AS ArtistId
FROM
    albums a
    INNER JOIN tracks t ON t.AlbumId = a.AlbumId
WHERE
    t.Name LIKE '%tomorrow%'
'''
albums_df = pd.read_sql(sql=sql, con=db_connection)

# Write your code above this line
albums_df


# <details>
#   <summary>💡 Solution </summary>
# 
#   ```python
#     sql = '''
#     SELECT
#         a.Title as AlbumTitle,
#         t.Name as TrackName,
#         a.ArtistId as ArtistId
#     FROM
#         albums a
#         INNER JOIN tracks t ON t.AlbumId = a.AlbumId
#     WHERE
#         t.Name LIKE '%tomorrow%'
#     '''
#     albums_df = pd.read_sql(sql=sql, con=db_connection)
#   ```
# </details>

# ### Exercise 4: 
# Write a query to get all the artists of the "Rock" genre. Read the results into a pandas DataFrame called `rock_artists_df`
# 
# <details>
#   <summary>Hints</summary>
# 
#   * Your query will need to join the `artists` and `genres` tables.
#     * Look at the diagram above to see how the tables are related.
#   * You may need to use the `DISTINCT` keyword in your sql query
#   * You should get back 50 records
# </details>
# 

# In[32]:


sql = '''
SELECT
    DISTINCT artists.ArtistId AS ArtistId,
    artists.Name AS ArtistName
FROM
    artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    JOIN tracks ON albums.AlbumId = tracks.AlbumId
    JOIN genres ON tracks.GenreId = genres.GenreId
WHERE
    genres.Name = 'Rock'
'''
rock_artists_df = pd.read_sql(sql=sql, con=db_connection)

# Write your code above this line
rock_artists_df


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   sql = '''
#     SELECT
#         DISTINCT artists.ArtistId as ArtistId,
#         artists.Name as ArtistName
#     FROM
#         artists
#         JOIN albums ON artists.ArtistId = albums.ArtistId
#         JOIN tracks ON albums.AlbumId = tracks.AlbumId
#         JOIN genres ON tracks.GenreId = genres.GenreId
#     WHERE
#         genres.Name = 'Rock'
#   '''
#   rock_artists_df = pd.read_sql(sql=sql, con=db_connection)
#   ```
# </details>

# ### Exercise 5:
# using `pandas.concat` method, add a new genre called "Arabic Pop", with an id of "26" to a new dataframe called `genres_data` DataFrame.
# 
# 
# <details>
#   <summary>Hints</summary>
# 
#   Here's a sample code for how to use the `pandas.concat` method.
#   ```python
#   # Given 2 dataframes, dataframe1 and dataframe2
#   dataframe1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#   dataframe2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
# 
#   pd.concat([dataframe1, dataframe2], ignore_index=True)
#   ```
# </details>

# In[33]:


genres_data = pd.concat([
    genres_df,
    pd.DataFrame({'GenreId': [26], 'Name': ['Arabic Pop']})
], ignore_index=True)

# Write your code above this line
genres_data


# <details>
#   <summary>💡 Solution </summary>
# 
#   ```python
#     new_genre = pd.DataFrame({'GenreId': [26], 'Name': ['Arabic Pop']})
#     genres_df = pd.concat([genres_df, new_genre], ignore_index=True)
#   ```
# 
#   Another solution
# 
#   ```python
#   genres_data = pd.concat([
#     genres_data,
#     pd.DataFrame.from_records([{'GenreId': '26', 'Name': 'Arabic Pop'}])
#   ], ignore_index= True)
#   ```
# </details>

# ### Exercise 6:
# use the `to_sql` method to write the updated `genres_df` DataFrame to the `genres` table in the database.
# 
# <details>
#   <summary>Hints</summary>
#   
#   * use the [📜`to_sql` method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html) to write the updated `genres_data` DataFrame to the `genres` table in the database.
#   * You can use the `if_exists` argument to specify what to do if the table already exists.
#     * You can set it to `replace` to replace the table with the new data.
#     * You can set it to `append` to append the new data to the existing table.
#     * You can set it to `fail` to raise an error if the table already exists.
#   * If you're saving the entire dataframe, then you need to use `replace`, if you're only saving the new record dataframe, then use `append`.
# </details>

# In[ ]:





# <details>
#   <summary>💡 Solution </summary>
# 
#   ```python
#   genres_data.to_sql('genres', db_connection, if_exists='replace', index=False) 
#   ```
# </details>

# In[ ]:


# This re-queries the database to make sure the data was saved correctly
genres_data2 = pd.read_sql(sql='SELECT * FROM genres;', con=db_connection)

genres_data2


# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.

# In[1]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python notebook.ipynb')

