import pandas as pd

def read_csv(string):
    df = pd.read_csv(string)
    return df

def remove_column(dataframe,string):
    if string in dataframe.columns.tolist():
        dataframe = dataframe.drop(string, axis = 1)
    return dataframe

def add_column(dataframe,string):
    if string not in dataframe.columns.tolist():
        dataframe[string] = [i*0 for i in range(0,dataframe.shape[0])]
    return dataframe

def get_columns_dict(dataframe,column_1,column_2):
    empty_dict = {}
    a = dataframe[column_1].values.tolist()
    b = dataframe[column_2].values.tolist()
    for i in range(0,dataframe.shape[0]):
        empty_dict[a[i]] = b[i]
    return empty_dict

def insert_note(dataframe,column,array,note):
    ind = []
    if column in dataframe.columns.tolist():
        #print('Hasta aquí llegó')
        for i in array:
            if i in dataframe.cuenta.unique():
                #print('llegó hasta aquí')
                ind.append(dataframe.index[dataframe.cuenta == i].tolist()[0])
    else:
        print(f'There is not a column named {column}.')
    
    #print(ind)

    for i in ind:
        dataframe[column][i] = note

    return dataframe
    
def insert_activ(dataframe,column,dic_t):
    if column in dataframe.columns.tolist():
            for i in dic_t:
                if i in dataframe.email_institucional.unique():
                    k = dataframe.index[dataframe.email_institucional == i].tolist()[0]
                    dataframe[column][k] = dic_t[i]
    else:
        print(f'There is not a column named {column}.')

    return dataframe
            
