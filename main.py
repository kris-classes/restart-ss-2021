"""
Small program that shows how to create an API that talks to an SQLite database.

Get the database from here: https://github.com/krp/sakila-sqlite

Requires fastapi and uvicorn packages.
Install with pip install fastapi uvicorn
"""

import fastapi
import sqlite3


app = fastapi.FastAPI()

connection = sqlite3.connect('sakila.db')
all_countries_query = 'SELECT * FROM country;'
all_cities_query = 'SELECT * FROM city;'

results = connection.execute(all_cities_query).fetchall()
# print(results)
#for city in results:
 #   print(city)
def get_cities(country):
    cities_in_country = f'''
    SELECT city,country FROM country
    INNER JOIN city
    WHERE country.country_id = city.country_id 
    AND country.country = '{country}'
    ORDER BY country ;
        '''
    #print(cities_in_country)
    results = connection.execute(cities_in_country).fetchall()
    print(results)
    return results

get_cities("India")
get_cities("New Zealand")


@app.get("/countries")
async def countries():
    all_countries = "SELECT * FROM country;"
    results = connection.execute(all_countries).fetchall()
    return results

@app.get("/parameters_example")
async def purple(jimi, haze, param3, some_other_parameter):
    return "hello"


@app.get("/cities")
async def cities(country_name):
    #display a list of cities based on country names
    results = get_cities(country_name)
    return results 


@app.get("/blog/{topic}/articles")
async def articles(topic):
    return f"TODO:make this return articles for {topic}!"

@app.post("/login")
async def handle_login(username, password):
    #verify username and password
    #return a randomnly generated token if login is successful
    #otherwise return error
    if username == "johnsmith" and password == "password123":
        return "Login Successful Token is asdf1234hjkl"
    else: 
        return "Incorrect username or password"
