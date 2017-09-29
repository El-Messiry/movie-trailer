import webbrowser


class Movie(object):
    '''
    Movie class to store title,storyline,img and trailer of
    a movie .

    init()
    takes Movie title, storyline, link of img,
    link of youtube trailer.

    show_trailer()
    used to show a trailer of a movie using link
    '''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image = poster_image
        self.trailer = youtube_trailer

    def show_trailer(self):
        webbrowser.get("""google-chrome""").open_new_tab(self.trailer)
