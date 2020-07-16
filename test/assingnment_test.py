

import unittest
from pandas import DataFrame
from my_lambdata6.assignment import add_state_names_column


class TestMyAssignment(unittest.TestCase):

    def test_add_state_names(self):

        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

        self.assertEqual(list(df.columns), ['abbrev'])
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(df.iloc[0]['abbrev'], 'CA')

        mapped_df = add_state_names_column(df)

        self.assertEqual(list(mapped_df.columns), ['abbrev', 'name'])
        self.assertEqual(len(mapped_df.columns), 2)
        self.assertEqual(mapped_df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(mapped_df.iloc[0]['name'], 'California')


if __name__ == '__main__':
    unittest.main()