from sklearn.model_selection import train_test_split

def split_df(df, value_x, value_y, test_size, random_state):    
    return train_test_split(
        df[value_x].values, df[value_y].values, test_size=test_size,
        random_state=random_state)