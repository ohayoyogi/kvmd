# ========================================================================== #
#                                                                            #
#    KVMD - The main Pi-KVM daemon.                                          #
#                                                                            #
#    Copyright (C) 2018  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


import os

from typing import Any

import pytest

from kvmd.validators import ValidatorError
from kvmd.validators.fs import valid_abs_path
from kvmd.validators.fs import valid_abs_path_exists
from kvmd.validators.fs import valid_unix_mode


# =====
@pytest.mark.parametrize("arg, retval", [
    ("/..",          "/"),
    ("/root/..",     "/"),
    ("/root",        "/root"),
    ("/f/o/o/b/a/r", "/f/o/o/b/a/r"),
    ("~",            os.path.abspath(".") + "/~"),
    ("/foo~",        "/foo~"),
    ("/foo/~",        "/foo/~"),
    (".",            os.path.abspath(".")),
])
def test_ok__valid_abs_path(arg: Any, retval: str) -> None:
    assert valid_abs_path(arg) == retval


@pytest.mark.parametrize("arg", ["", " ", None])
def test_fail__valid_abs_path(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_abs_path(arg))


# =====
@pytest.mark.parametrize("arg, retval", [
    ("/..",          "/"),
    ("/root/..",     "/"),
    ("/root",        "/root"),
    (".",            os.path.abspath(".")),
])
def test_ok__valid_abs_path_exists(arg: Any, retval: str) -> None:
    assert valid_abs_path_exists(arg) == retval


@pytest.mark.parametrize("arg", [
    "/f/o/o/b/a/r",
    "~",
    "/foo~",
    "/foo/~",
    "",
    None,
])
def test_fail__valid_abs_path_exists(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_abs_path_exists(arg))


# =====
@pytest.mark.parametrize("arg", [0, 5, "1000"])
def test_ok__valid_unix_mode(arg: Any) -> None:
    value = valid_unix_mode(arg)
    assert type(value) == int  # pylint: disable=unidiomatic-typecheck
    assert value == int(str(value).strip())


@pytest.mark.parametrize("arg", ["test", "", None, -6, "-6", "5.0"])
def test_fail__valid_unix_mode(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        print(valid_unix_mode(arg))
