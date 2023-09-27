class Movie:
    def __init__(self, data):
        self.directors = self.parse_name_list(data["credits"]["director"])
        self.actors = self.parse_name_list(data["credits"]["star"])
        self.genres = ", ".join(data["metadata"]["genres"])
        self.plot = data["plot"]
        self.title = data["primary"]["title"]
        self.year = int(data["primary"]["year"][0])
        self.rating = data["ratings"]["rating"]
        self.metacritic_score = data["ratings"]["metascore"]

    def __repr__(self):
        return f"{self.title} ({self.year})"

    def __str__(self):
        return f"{self.title} ({self.year})"

    def full_details(self):
        return (
            f"{self.title} ({self.year})\n"
            + f"Genres: {self.genres}\n"
            + f"Plot: {self.plot}\n"
            + f"Directors: {self.directors}\n"
            + f"Actors: {self.actors}\n"
            + f"Rating: {self.rating}\n"
            + f"Metacritic Score: {self.metacritic_score}\n"
        )

    @staticmethod
    def parse_name_list(list_data):
        result = ""
        for i, attr in enumerate(list_data):
            if i > 0:
                result += ", "
            result += attr["name"]
        return result
