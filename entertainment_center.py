#!/usr/bin/env python
"""Create instances of Movie and call open_movies_page to render html"""

import media
import fresh_tomatoes

# Toy Story movie: movie title, storyline, poster image and movie trailer
TOY_STORY = media.Movie(
    "Toy Story",
    "A story of a boy and his toys.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",     # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

# Avatar movie: movie title, storyline, poster image and movie trailer
AVATAR = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",     # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

# Before Sunrise movie: movie title, storyline, poster image and movie trailer
BEFORESUNRISE = media.Movie(
    "Before Sunrise",
    "A young man and woman meet on a train in Europe, and wind up "
    "spending one evening together in Vienna. Unfortunately, "
    "both know that this will probably be their only night together.",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",     # NOQA
    "https://www.youtube.com/watch?v=9v6X-Dytlko"
    )

# Hacksaw Ridge movie: movie title, storyline, poster image and movie trailer
HACKSAWRIDGE = media.Movie(
    "Hacksaw Ridge",
    "WWII American Army Medic Desmond T. Doss, who served during the Battle "
    "of Okinawa, refuses to kill people, and becomes the first man "
    "in American history to receive the Medal of Honor without firing a shot.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Hacksaw_Ridge_poster.png/220px-Hacksaw_Ridge_poster.png",     # NOQA
    "https://www.youtube.com/watch?v=s2-1hz1juBI"
    )

# Pele movie: movie title, storyline, poster image and movie trailer
PELE = media.Movie(
    "Pele: Birth of a legend",
    "Pele's meteoric rise from the slums of Sao Paulo to leading "
    "Brazil to its first World Cup victory at the age of 17 is chronicled "
    "in this biographical drama.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Pel%C3%A9_%28film_poster%29.jpg/220px-Pel%C3%A9_%28film_poster%29.jpg",       # NOQA
    "https://www.youtube.com/watch?v=XBrfxHOXsDE")

# Set list of movies
MOVIES = [
    TOY_STORY,
    AVATAR,
    BEFORESUNRISE,
    HACKSAWRIDGE,
    PELE
    ]

# Create fresh_tomatoes.html file and open it in web-browser
fresh_tomatoes.open_movies_page(MOVIES)
