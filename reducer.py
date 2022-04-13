import argparse
import sys
import ast


def get_args_pars():

    parser = argparse.ArgumentParser(description='displays the top movies by rating ',
                                     epilog='Example: python3 get_movies.py -N 60 -reg_ex Alien')
    parser.add_argument("-N", type=int, dest="number",
                        help="number of top-rated movies")

    return parser.parse_args()


def shuffle(num_reducers=1):
    shuffled_items = []

    prev_key = None
    values = []

    try:
        for line in sys.stdin:
            key, value = line.split("\t")
            if key != prev_key and prev_key is not None:
                shuffled_items.append((prev_key, values))
                values = []
            prev_key = key
            values.append(value)
    except:
        pass
    finally:
        if prev_key is not None:
            shuffled_items.append((key, values))

    result = []
    num_items_per_reducer = len(shuffled_items) // num_reducers
    if len(shuffled_items) / num_reducers != num_items_per_reducer:
        num_items_per_reducer += 1
    for i in range(num_reducers):
        result.append(
            shuffled_items[num_items_per_reducer*i:num_items_per_reducer*(i+1)])

    return result


def reduce(key, values, limit=None):
    count = 0
    for value in values:
        value = ast.literal_eval(value)
        year = value[0]
        title = value[1]
        print('{};{};{}'.format(key, year, title))
        count += 1
        if count == limit:
            break

    return count


def main():
    args = get_args_pars()
    if args.number:
        count = 0
        limit = args.number
        for group in shuffle():
            for key, values in group:
                count = reduce(key, values, limit)
                if (limit := limit - count) == 0:
                    break
    else:
        for group in shuffle():
            for key, values in group:
                reduce(key, values)


if __name__ == '__main__':
    main()
