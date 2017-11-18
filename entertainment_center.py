import fresh_tomatos
import webbrowser
import media
# creating movie instances

toy_story = media.Movie(
    """Toy Story""",
    """movie about a toy :D""",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",  # NOQA
    """https://www.youtube.com/watch?v=KYz2wyBy3kc""")

avatar = media.Movie(
    """Avatar""",
    """marine who goes to space""",
    """https://images-na.ssl-images-amazon.com/images/I/41vuODnDSuL.jpg""",  # NOQA
    """https://www.youtube.com/watch?v=5PSNL1qE6VY""")

batman = media.Movie(
    """Batman vs. Superman""",
    """Batman is vigilante who fights for justice""",
    """http://cdn2-www.superherohype.com/assets/uploads/gallery/batman-vs-superman/batmanvsupermanposter.jpg""",  # NOQA
    """https://www.youtube.com/watch?v=IwfUnkBfdZ4""")

fight_club = media.Movie(
    """Fight Club""",
    """rule 1 , no one knows about the fight club""",
    "https://www.movieposter.com/posters/archive/main/67/MPW-33738""",  # NOQA
    """https://www.youtube.com/watch?v=J8FRBYOFu2w""")

sh_redemption = media.Movie(
    "Shawshank Redemption",
    "Crime Two imprisoned men bond" +
    "over a number of years",
    "https://sherrymedia.files.wordpress.com/2010/09/shawshank-redemption-poster.jpg?w=540",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

gone_girl = media.Movie(
    "Gone Girl",
    "thriller-Crime With his wife's disappearance" +
    " having become the focus of an intense media circus",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTwcWs6CK22NdvXZH0CbigLxoV-N3GIJypphImFYYv1vG_VKXTQ",  # NOQA
    "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

# creating Movie List

movies_list = [toy_story,
               avatar,
               batman,
               fight_club,
               sh_redemption,
               gone_girl]

# Displaying entertainment center in Web browser

fresh_tomatos.open_movies_page(movies_list)

# main

if __name__ == '__main__':
    pass
