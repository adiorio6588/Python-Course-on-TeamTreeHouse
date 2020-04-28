movies = [
    "The Phathom Menace",
    "Attack of the Clone",
    "Revenge of the Sith",
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi"
]

video_games = [
    "Shadow of the Empire",
    "Rogue Squadron",
    "The Force Unleashed"
]

#=======> Original Code Below <========
# print("Suggested gift: {}".format(movies[0]))

# print("Movies:  ")
# for movie in movies:
#     print("*  " + movie)

# print("Star Wars Games: ")
# for game in video_games:
#     print("*: " + game)

def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("=====>", suggested_gift, "<=====")
    for item in items:
        print("* " + item)
    print()

display_wishlist("Movies", movies)
display_wishlist("Video Games", video_games)