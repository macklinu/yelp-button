from yelp import Yelp


def main():
    yelp = Yelp()
    random_business = yelp.get_random_business()
    details = yelp.get_business_details(random_business)
    print details.name + ": " + str(details.rating) + " stars"


if __name__ == '__main__':
    main()