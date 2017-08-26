from afterwill.__main__ import main
import pytest as pt
from conftest import data_args, data_output


@pt.mark.parametrize("cli_params,expected", zip(data_args, data_output))
def test_main(parser, cli_params, expected, capfd):
    args = parser.parse_args(cli_params)
    main(args)
    out, err = capfd.readouterr()
    assert out == expected
