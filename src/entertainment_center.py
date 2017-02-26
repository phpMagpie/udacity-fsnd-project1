import fresh_tomatoes
import media

movie1 = media.Movie(
    "Star Wars",
    "Civil war had struck the galaxy, which was ruled by an Empire",
    "https://i.kinja-img.com/gawker-media/image/upload/s--S24cks6n--/c_scale,f_auto,fl_progressive,q_80,w_800/19fk32sw3nt1wjpg.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XHk5kCIiGoM"
    )

movie2 = media.Movie(
    "A Knights Tale",
    "The film takes its title from Chaucer's \"The Knight's Tale\" "
    "in his Canterbury Tales, though the plot is not especially similar",
    "https://s-media-cache-ak0.pinimg.com/originals/33/08/34/33083498b1b305db6e818d31dfa9fa41.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zH6U5y086hw"
    )

movie3 = media.Movie(
    "Elf",
    "Buddy was a baby in an orphanage who stowed away in Santa's "
    "sack and ended up at the North Pole",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg",
    "https://www.youtube.com/watch?v=gW9wRNqQ_P8"
    )

movie4 = media.Movie(
    "Up",
    "Carl Fredricksen as a boy wanted to explore South America and "
    "find the forbidden Paradise Falls",
    "https://vignette3.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",  # NOQA
    "https://www.youtube.com/watch?v=pkqzFUhGPJg"
    )

movie5 = media.Movie(
    "Monty Python's Life of Brian",
    "A 1979 British religious satire comedy film starring and written "
    "by the comedy group Monty Python",
    "https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=TKPmGjVFbrY"
    )

movie6 = media.Movie(
    "Lethal Weapon",
    "LAPD Homicide Sergeant Roger Murtaugh, is partnered with "
    "Sergeant Martin Riggs, a transfer from narcotics",
    "https://reggiestake.files.wordpress.com/2014/02/lethal-weapon-3-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=GUorM4nTX7k"
    )

movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# Generate and open HTML file using list of movies
fresh_tomatoes.open_movies_page(movies)
