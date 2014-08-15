import random

from yelpapi import YelpAPI

from json_response import JsonResponse


class Yelp(YelpAPI):
    def __init__(self):
        super(Yelp, self).__init__("rPYK4RMm9kHcqLWHUaJA8Q",
                                   "29wVTMD5UKkZN96wnlY6HFDaWTM",
                                   "rh7RzRVIxJlLGpLeP-o7-nsEcX_T0JO5",
                                   "DSm6t5HoLiYDbSo0syXIdydGrps")

    def get_random_business(self):
        query = JsonResponse(**self.search_query(term='food',
                                                 bounds='42.293654,-83.114049|42.416322,-83.060834',
                                                 sort=0,
                                                 limit=20)
        )
        return JsonResponse(**random.choice(query.businesses))

    def get_business_details(self, business):
        return JsonResponse(**self.business_query(business.id))