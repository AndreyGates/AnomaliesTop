def str_to_list_lens(s):
    '''Converting a column with strings into a column with their corresponding lists'lengths'''
    if s == '' or s == 'nan':
        return 0
    elif ';' not in s:
        return 1
    else:
        return len(s.split(';'))

def data_prep(df):
    '''Data preprocessing and "special" columns extention'''
    # Step 1: delete columns of low analytic importance
    df = df.drop(columns=['#', 'id', 'uid', 'domain', 'cn', 'department', 'title', 'who'])
 
    # Step 2: convert each "special" column' string into the list's length
    df['member_of_indirect_groups_ids'] = df['member_of_indirect_groups_ids'].astype(str).apply(str_to_list_lens)
    df['member_of_groups_ids'] = df['member_of_groups_ids'].astype(str).apply(str_to_list_lens)

    # Step 3: impute "is_admin" column's missing values
    df['is_admin'].fillna(df['is_admin'].mode()[0], inplace=True)

    return df
