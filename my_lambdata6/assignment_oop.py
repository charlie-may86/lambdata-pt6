from pandas import DataFrame


class DataFrameProcessor():
    def __init__(self, df):
        """[This Class takes a df and returns a df with the option to apply the
        add_state_names_column() method]

        Args:
            my_df ([DataFrame]): [a DataFrame with a column called abbrev that has
            state abbreviations]
        """
        self.df = df


    def add_state_names_column(self):
        """[This method adds a column of corresponding state names to a the df class
        that has state abbrv]

        Args:
            self ([DataFrame]): [a DataFrame with a column called abbrev that has
            state abbreviations]

        Return:
            A copy of the orginal dataframe, but with an extra column containing
            full state names.
        """

        names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Conn',
        'DC': 'Washington, D.C.', 'TX': 'Texas'}

        #this wal will return a transformed copy of the df
        # new_df = self.df.copy()
        # new_df['name'] = my_df['abbrev'].map(names_map)

        #this way will mutate the exisiting df
        self.df['name'] = self.df['abbrev'].map(names_map)

        # return new_df


if __name__ == "__main__":

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())

    # mapped_df = add_state_names_column(df)
    # print(mapped_df.head())

    processor = DataFrameProcessor(df=df)
    print(processor.df.head())

    processor.add_state_names_column()
    print(processor.df.head())

    # new_df = processor.add_state_names_column()
    # print(new_df.head())


   
    