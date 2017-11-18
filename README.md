# movie trailer


### Introduction

This is a Documentation of udacity Full stack web-development nano degree First project " *** movie trailer website *** " .

***
### List of Contents
* fresh_tomatoes.py
- fresh tomatoes.html
- media.py
- entrtainment_center.py*

***
### Contents
- **`fresh_tomatoes.py`** is a ready file from this [repository](https://github.com/udacity/ud036_StarterCode) . It has a **`open_movie_page()`** function that will take in your list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies

- **`fresh_tomatoes.html`** is ready **HTML** code used by `fresh_tomatoes.py`  to build the webpage on your browser

- **`media.py`**   is a movie class that takes movie's `name `, `story line` , `link to image` , `link of youtube trailer` 

- **`entertainment_center.py`** by calling the constructor **`media.Movie()`** to instantiate movie objects. You’ve given movies their own custom data structure by defining the movie class and constructor, and now these objects can be stored in a list data structure. This list of movies is what the **`open_movies_page()`** function needs as input in order to build the **HTML** file, so you can display the website.

***
### How to Use

- **Download** `fresh_tomates.py` and `fresh_tomatoes.html` from this [repository](https://github.com/udacity/ud036_StarterCode) . 


- in **`entertainment_center.py`**  import **`media`**, **`webbrowser`**, **`fresh_tomatoes`**.

- create your object of your favorite movie by passing `name `, `story line` , `link to image` , `link of youtube trailer` when creating object .
**Example:** 
```
		avatar = media.Movie(
			# name
		"""Avatar""",	
		# story line			
			"""marine who goes to space""",
			# img Link
			"""https://images-na.ssl-images-amazon.com/images/I/41vuODnDSuL.jpg""",
			#YouTube Link
			"""https://www.youtube.com/watch?v=5PSNL1qE6VY""")
```
- Create List of movie instances 
**Example:** 
```
	movies_list = [toy_story,
			       avatar,
			       batman,
			       fight_club,
			       sh_redemption,
			       gone_girl]
```
- Call **`open_movie_page(movie_list)`** 
- **Run** your code and Enjoy :) .



