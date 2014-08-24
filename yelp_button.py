from pprint import PrettyPrinter

from yelp import Yelp


def main():
    pp = PrettyPrinter(indent=2)
    yelp = Yelp()
    details = yelp.get_business()
    pp.pprint(details)


if __name__ == '__main__':
    main()