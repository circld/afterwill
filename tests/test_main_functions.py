from afterwill.__main__ import format_tasks, print_tasks
import pytest as pt
from conftest import data_args, data_formatted, data_output


@pt.mark.parametrize("cli_params,expected", zip(data_args, data_formatted))
def test_format_tasks(parser, cli_params, expected):
    args = parser.parse_args(cli_params)
    assert list(format_tasks(args.task_set)) == expected


@pt.mark.parametrize("formatted,expected", zip(data_formatted, data_output))
def test_print_tasks(formatted, expected, capfd):
    print_tasks(formatted)
    out, err = capfd.readouterr()
    assert out == expected
