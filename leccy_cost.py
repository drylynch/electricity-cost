import argparse


def print_cost(watts, hours, cpkwh):
    daily_watts = (watts * hours)/1000
    print('{0}w for {1}hrs/day @ €{2:.2f}/KWH'.format(watts, hours, cpkwh))
    print('daily:      €{:.2f}'.format(daily_watts * cpkwh))
    print('weekly:     €{:.2f}'.format(daily_watts * 7 * cpkwh))
    print('monthly:    €{:.2f}'.format(daily_watts * 28 * cpkwh))
    print('yearly:     €{:.2f}'.format(daily_watts * 365 * cpkwh))
    input('--press RETURN--')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('watts', type=int, help='appliance max rated watts')
    parser.add_argument('hours', type=int, help='hours per day appliance is used (round up)')
    parser.add_argument('cpkwh', type=float, help='cost per kwh')
    args = parser.parse_args()
    print_cost(args.watts, args.hours, args.cpkwh)