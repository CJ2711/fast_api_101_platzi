

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "It",
        "overview": "Bla bla bla...",
        "year": "2021",
        "rating": 9,
        "category": "Terror"
    }
]

def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            print(item)
            # return item
        return []
get_movie(2)