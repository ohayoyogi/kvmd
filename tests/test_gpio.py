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


from kvmd import gpio


# =====
def test_gpio__loopback_initial_false() -> None:
    # pylint: disable=singleton-comparison
    with gpio.bcm():
        assert gpio.set_output(0) == 0
        assert gpio.read(0) == False  # noqa: E712
        gpio.write(0, True)
        assert gpio.read(0) == True  # noqa: E712


def test_gpio__loopback_initial_true() -> None:
    # pylint: disable=singleton-comparison
    with gpio.bcm():
        assert gpio.set_output(0, True) == 0
        assert gpio.read(0) == True  # noqa: E712
        gpio.write(0, False)
        assert gpio.read(0) == False  # noqa: E712


def test_gpio__input() -> None:
    # pylint: disable=singleton-comparison
    with gpio.bcm():
        assert gpio.set_input(0) == 0
        assert gpio.read(0) == False  # noqa: E712
