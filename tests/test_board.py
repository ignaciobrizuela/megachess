import unittest
import show_board as sb

class boardTest(unittest.TestCase):

    def test_show_board(self):
        board_not_split = ('rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp' 
        '                                                                ' 
        '                                                                ' 
        'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')
        board_split = ['rrhhbbqqkkbbhhrr',
                 'rrhhbbqqkkbbhhrr',
                 'pppppppppppppppp',
                 'pppppppppppppppp',
                 '                ',
                 '                ',
                 '                ',
                 '                ',
                 '                ',
                 '                ',
                 '                ',
                 '                ',
                 'PPPPPPPPPPPPPPPP',
                 'PPPPPPPPPPPPPPPP',
                 'RRHHBBQQKKBBHHRR',
                 'RRHHBBQQKKBBHHRR']
        
        self.assertEqual(sb.show_board(board_not_split), board_split, "Must be a standar board")

if __name__ == "__main__":
     unittest.main()
            