import argparse as ap
from itertools import izip
import sys


__all__ = ('format_tasks', 'print_tasks')


def initialize_parser():
    """Initialize ArgumentParser object
    Returns: argparse.ArgumentParser instance

    """
    p = ap.ArgumentParser(formatter_class=ap.RawTextHelpFormatter,
                          usage='''\n    $ python main.py  \\
    > --task_set 'grocery shop' meditate vacuum  \\
    > --task_set jog 'eat lunch' 'work on scala course' 'apply to job'

    After I grocery shop, I will meditate
    After I meditate, I will vacuum

    After I jog, I will eat lunch
    After I eat lunch, I will work on scala course
    After I work on scala course, I will apply to job''')
    p.add_argument('--task_set', nargs='+', action='append', metavar='task',
                   help='A set of "After I ___, I will ___" tasks. Can define '
                   'multiple task sets comprised of as many tasks as you want.')
    return p


def format_tasks(task_sets):
    """Convert task sets into "After I ___, I will ___" list of lists.

    Args:
        task_sets (list of lists): task sets,
            e.g., [['eat', 'sleep'], ['work for an hour', 'take a break']]

    Returns: generator of generators

    """
    return (["After I {}, I will {}".format(t1, t2)
             for t1, t2 in izip(s[:-1], s[1:])]
            for s in task_sets)


def print_tasks(tasks, set_sep='\n\n', task_sep='\n'):
    """Prints tasks to stdout.

    Args:
        tasks (generator of generators): e.g., [[task_1, task_2], [task_a, task_b]]
        set_sep (str): separator to print between task sets
        task_sep (str): separator to print between tasks

    Returns: None

    """
    print
    print '\n\n'.join(
        '\n'.join(t for t in task_set)
        for task_set in tasks
    )


def main():

    parser = initialize_parser()
    args = parser.parse_args()

    formatted_tasks = format_tasks(args.task_set)
    print_tasks(formatted_tasks)


if __name__ == '__main__':
    sys.exit(main())
