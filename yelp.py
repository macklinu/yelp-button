import random
import os

from yelpapi import YelpAPI


class Yelp(YelpAPI):
    def __init__(self):
        super(Yelp, self).__init__(os.environ.get('YELP_CONSUMER_KEY'),
                                   os.environ.get('YELP_CONSUMER_SECRET'),
                                   os.environ.get('YELP_TOKEN'),
                                   os.environ.get('YELP_TOKEN_SECRET'))
        self.categories = [
            'breweries',
            'foodtrucks',
            'tradamerican',
            'bbq',
            'breakfast_brunch',
            'burgers',
            'delis',
            'gastropubs',
            'greek',
            'italian',
            'japanese',
            'latin',
            'mediterranean',
            'mexican',
            'mideastern',
            'pizza',
            'salad',
            'sandwiches',
            'soulfood',
            'sushi',
            'tapas',
            'tapasmallplates',
            'tex-mex',
            'vegan',
            'vegetarian'
        ]

    def get_business(self):
        return self.__get_business_details(self.__get_random_business())

    def __get_random_business(self):
        query = self.search_query(term='food',
                                  category_filter=random.choice(self.categories),
                                  bounds='42.293654,-83.114049|42.416322,-83.060834',
                                  sort=0,
                                  limit=20)
        return random.choice(query['businesses'])

    def __get_business_details(self, business):
        return self.business_query(business['id'])