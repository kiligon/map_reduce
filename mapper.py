import sys
import re
import argparse


def get_args_pars():
    parser = argparse.ArgumentParser()

    parser.add_argument("-genres", dest="genres",
                        help="filter by genre, can be multiple.", default='+')
    parser.add_argument("-year_from",  dest="year_from",
                        help="year from which the films were released", default=0)
    parser.add_argument("-year_to",  dest="year_to",
                        help="year before which the films were released", default=9999)
    parser.add_argument("-reg_ex",  dest="regex",
                        help="filter (regular expression) on the movie title.", default="")

    return parser.parse_args()


def year_filter(year, year_from, year_to):
    return year and year_from <= int(year) <= year_to


def genre_filter(genre, arg_genre):
    return genre != '(no genres listed)' and (genre == arg_genre or '+' == arg_genre)


def title_filter(title, reg_ex):
    if re.search(reg_ex, title):
        return True
    else:
        return False


def map(line):
    year = re.findall(r'[0-9]{4}', ",".join(line.split(",")[1:-1]))[0] if len(
        re.findall(r'[0-9]{4}', ",".join(line.split(",")[1:-1]))) == 1 else False
    title = re.sub(r'\([0-9]{4}\)', "", ",".join(line.split(",")[1:-1]))
    line = str(line[:-2])
    if year_filter(year, args.year_from, args.year_to) and title_filter(title, args.regex):
        for genre in line.split(",")[-1].split("|"):
            if genre_filter(genre, args.genres):
                yield re.sub('\r\n', '', genre), (title, year)


# read_splits -> map
def main():
    for line in sys.stdin:
        for key, value in map(line):
            print("{}\t{}".format(key, value))


if __name__ == "__main__":
    args = get_args_pars()
    main()
