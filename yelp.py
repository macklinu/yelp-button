import random
import os

from yelpapi import YelpAPI

from json_response import JsonResponse


class Yelp(YelpAPI):
    def __init__(self):
        super(Yelp, self).__init__(os.environ.get('YELP_CONSUMER_KEY'),
                                   os.environ.get('YELP_CONSUMER_SECRET'),
                                   os.environ.get('YELP_TOKEN'),
                                   os.environ.get('YELP_TOKEN_SECRET'))

    def get_random_business(self):
        query = JsonResponse(**self.search_query(term='food',
                                                 bounds='42.293654,-83.114049|42.416322,-83.060834',
                                                 sort=0,
                                                 limit=20)
        )
        return JsonResponse(**random.choice(query.businesses))

    def get_business_details(self, business):
        return JsonResponse(**self.business_query(business.id))