# Made by brz
import unittest
from tests import test_board
from tests import test_pieces
from tests import test_scans
from tests import test_score
from tests import test_player

def create_suite(module):
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    return suite


def create_suite_pack():
    suite_list = []
    suite_list.append(create_suite(test_board))
    suite_list.append(create_suite(test_pieces))
    suite_list.append(create_suite(test_scans))
    suite_list.append(create_suite(test_score))
    suite_list.append(create_suite(test_player))

    return suite_list

if __name__ == '__main__':
    suite_pack = unittest.TestSuite(create_suite_pack())

    runner = unittest.TextTestRunner(descriptions=True, verbosity=3)
    runner.run(suite_pack)