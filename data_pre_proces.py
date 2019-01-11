import copy
def get_colum_with_nan(data):
    df_nan = pd.isnull(data)
    lst = []
    for col in df_nan:
        for i, row_value in df_nan[col].iteritems():
            if row_value and col not in lst:            
                lst.append(col)
    return lst

nans = lambda df: df[df.isnull().any(axis=1)]
get_rows_which_are_NOT_in_other_dataframe = lambda df1, df2 :df1[~df1.index.isin(df2.index)]


def get_col_with_number_elements(data,number_elements):
    data_new = copy.deepcopy(data)
    lst_col = [i for i in data_new]
    data_histogram = data_new.T.apply(lambda x: x.nunique(), axis=1)
    number_of_elem = [i for i in data_histogram.values]
    return [lst_col[i] for i in range(len(number_of_elem)) if number_of_elem[i] == number_elements]    
        
def two_elements_col_to_int(data,col_name):
    data.loc[data[col_name] == data[col_name].loc[0], col_name] = 1
    data.loc[data[col_name] != data[col_name].loc[0], col_name] = 0
    return data


def get_lst_of_elem(data,col_name,number):
    lst_elem = []
    for i in data[col_name].values:
        if i not in lst_elem:
            lst_elem.append(i)
        if len(lst_elem) == number:
            break
    return lst_elem

def number_in_col(data,col_name):
    data_new = copy.deepcopy(data)
    data_histogram = data_new.T.apply(lambda x: x.nunique(), axis=1)
    return data_histogram.loc[[col_name]][0]
    

def elements_col_to_int(data,col_name):
    data_new = copy.deepcopy(data)
    data_histogram = data_new.T.apply(lambda x: x.nunique(), axis=1)
    number = data_histogram.loc[[col_name]][0]
    lst_of_elem = get_lst_of_elem(data,col_name,number)
    for i in range(len(lst_of_elem)):
        data.loc[data[col_name] == lst_of_elem[i], col_name] = i
    return data
######################################################################################!
# Deal with measing values  
######################################################################################!
#TODO! numeric imputation        
def data_pre_proces_for_two_elements(data):
    lst_of_two = get_col_with_number_elements(data,2)
    if lst_of_two != []:
        for i in lst_of_two:
            data = two_elements_col_to_int(data,i)       
    return data      
