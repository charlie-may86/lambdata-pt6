
from pandas import DataFrame
from my_lambdata6.assignment import add_state_names_column



def test_add_state_names():

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    assert list(df.columns) == ['abbrev']
    assert len(df.columns) == 1
    assert df.iloc[0]['abbrev'] == 'CA'

    mapped_df = add_state_names_column(df)

    assert list(mapped_df.columns) == ['abbrev', 'name']
    assert len(mapped_df.columns) == 2
    assert mapped_df.iloc[0]['abbrev'] == 'CA'
    assert mapped_df.iloc[0]['name'] == 'California'


# if __name__ == '__main__':
#     unittest.main()