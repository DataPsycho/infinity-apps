from app import State, City, Venue, Artist, Gener, Show
from app import db

"""
Relation:
    Parent          Child
    State           City
    City            Artist, Venue
    Venue, Artist   Shows
    Artist          Gener

State and Gener class if independent of foreign key.
"""

# Insert Data City, State
# state_data = State(state="NY")
# city_data = City(city="New York")
# city_data._state = state_data
# db.session.add(state_data)
# db.session.commit()

# Insert Data Venue
venue_list = [
    # {
    # "id": 1,
    # "name": "The Musical Hop",
    # "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    # "address": "1015 Folsom Street",
    # "city": "San Francisco",
    # "state": "CA",
    # "phone": "123-123-1234",
    # "website": "https://www.themusicalhop.com",
    # "facebook_link": "https://www.facebook.com/TheMusicalHop",
    # "seeking_talent": True,
    # "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    # "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
    # },
    {
    "id": 2,
    "name": "The Dueling Pianos Bar",
    "genres": ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "website": "https://www.theduelingpianos.com",
    "facebook_link": "https://www.facebook.com/theduelingpianos",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
    },
    {
    "id": 3,
    "name": "Park Square Live Music & Coffee",
    "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "website": "https://www.parksquarelivemusicandcoffee.com",
    "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
    }
]


def insert_venue_data(venues):
    for item in venues:
        venue = Venue(
            name=item.get("name"),
            address=item.get("address"),
            phone=item.get("phone"),
            website=item.get("website"),
            image_link=item.get("image_link"),
            facebook_link=item.get("facebook_link"),
            seeking_talent=item.get("seeking_talent"),
            seeking_description=item.get("seeking_description")
            )

        gener_list = [Gener(gener=i) for i in item.get("genres")]
        state = State.query.filter_by(state=item.get("state")).first()
        city = City.query.filter_by(city=item.get("city")).first()
        if state:
            if city:
                venue.city_id = city.id
            else:
                city = City(city=item.get("city"))
                city.state_id = state.id
        else:
            state = State(state=item.get("state"))
            city = City(city=item.get("city"))
            city._state = state
            venue._city = city


        venue.geners = gener_list
        db.session.add(venue)
        db.session.commit()
        print("Inserted {}".format(item.get("name")))
    return print("All Venue Inserted")

if __name__ == "__main__":
    insert_venue_data(venue_list)
