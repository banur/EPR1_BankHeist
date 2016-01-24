""" Bank heist

Console grid game to simulate a bank heist
Player is required to navigate a random bank layout, find the code for the safe
and open the safe - all while not stepping into the securities sight.

"""

import random
import unittest

__author__ = "6224961: Marie-Luise Katzer, 6192860: Georg Schuhardt"
__copyright__ = "Copyright 2015/2016 – EPR-Goethe-Uni"
__credits__ = "nothing"
__email__ = "georg.schuhardt@gmail.com"
__github__ = "https://github.com/banur/EPR1_BankHeist"


class Bank():
    """ Bank class. """

    bank = []
    objects = {}
    rooms = []
    alert_state = 0

    def create_map(self):
        """ Create the bank layout and fill with objects. """
        pass

    def print_map(self):
        """ Print the map to console. """
        pass

    def compute_turn(self):
        """ Wait for player input, then compute the turn for all objects. """
        pass

    def get_pos(self, position):
        """ Return the content of position.

        position = (x, y) """
        pass

    def move(self, position, direction):
        """ Move an entity into the direction.

        position = (x, y)
        direction = (a, 0) or (0, b)
        """
        pass


class Security():
    """ Security class. """

    symbol = "!"
    move_speed = 1
    sight = 2

    def perform_action(self):
        """ Determine and perform the objects action. """
        pass

    def end_round(self):
        """ Detect player and end the round. """
        pass


class Robber():
    """ Robber class. """

    symbol = "#"

    def perform_action(self):
        """ Determine and perform the objects action. """
        pass

    def get_code(self):
        """ Read the code. """
        pass

    def open_safe(self):
        """ Input code into safe. """
        pass


class Safe():
    """ Safe class. """

    value = None
    symbol = "T"

    def generate_value(self):
        """ Generate random value. """
        pass

    def open_safe(self, code):
        """ Accept user input, return safe value if right code. Heighten alert state otherwise. Requires nearby player.

        code = 5 random non-zero digits
        """
        pass


class Code():
    """ Code class. """

    code = None
    symbol = "C"

    def generate_code(self):
        """ Generate a new random code. """
        pass

    def read_code(self):
        """ Print the code for the user to read. Requires nearby player. """
        pass

    def compare_code(self, code):
        """ Return True if the input matches the code, False otherwise.

        code = 5 random non-zero digits
        """
        pass


class Test(unittest.TestCase):
    """ Test all classes and functions. """

    def test_bank_class(self):
        """ Create a new bank class and test functions. """
        test_bank = Bank()
        position = (0, 0)
        direction = (1, 0)

        self.assertTrue(test_bank.create_map())
        self.assertTrue(test_bank.print_map())
        self.assertTrue(test_bank.compute_turn())
        self.assertTrue(test_bank.get_pos(position))
        with self.assertRaises(KeyError):
            self.assertTrue(test_bank.get_pos())
        self.assertTrue(test_bank.move(position, direction))
        with self.assertRaises(KeyError):
            self.assertTrue(test_bank.move())

    def test_security_class(self):
        """ Create a new security class and test functions. """
        test_security = Security()
        self.assertTrue(test_security.perform_action())
        self.assertTrue(test_security.end_round())

    def test_robber_class(self):
        """ Create a new robber class and test functions. """
        test_robber = Robber()
        self.assertTrue(test_robber.perform_action())
        self.assertTrue(test_robber.get_code())
        self.assertTrue(test_robber.open_safe())

    def test_safe_class(self):
        """ Create a new safe class and test functions. """
        test_safe = Safe()
        test_code = Code()
        test_code.generate_code()
        code = test_code.code

        self.assertTrue(test_safe.generate_value())
        self.assertTrue(test_safe.open_safe(code))
        with self.assertRaises(KeyError):
            self.assertTrue(test_safe.open_safe())

    def test_code_class(self):
        """ Create a new code class and test functions. """
        test_code = Code()
        test_code.generate_code()
        code = test_code.code

        self.assertTrue(test_code.generate_code())
        self.assertTrue(test_code.read_code())
        self.assertTrue(test_code.compare_code(code))
        with self.assertRaises(KeyError):
            self.assertTrue(test_code.compare_code())
