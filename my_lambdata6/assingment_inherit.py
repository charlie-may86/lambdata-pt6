
from pandas import DataFrame

class CustomFrame(DataFrame):
    """[summary]

    Args:
        DataFrame ([df]): [A df with a column called 'abbrev' that contains
        state abbreviations]

    Returns:
        [type]: [description]
    """
    pass

    # def __init__(self):
    #     super().__init__()
    

    def add_state_names_column(self):
        """[This Class takes a df and returns a df with the option to apply the
        add_state_names_column() method]

        Args:
            my_df ([DataFrame]): [a DataFrame with a column called abbrev that has
            state abbreviations]
        """

        names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Conn',
        'DC': 'Washington, D.C.', 'TX': 'Texas'}

        self['name'] = self['abbrev'].map(names_map)



if __name__ == "__main__":

    # df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())

    # mapped_df = add_state_names_column(df)
    # print(mapped_df.head())

    dictionary = ({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(dictionary)

    custom_frame = CustomFrame(dictionary)
    print(custom_frame.head())

    custom_frame.add_state_names_column()
    print(custom_frame.head())

    




    