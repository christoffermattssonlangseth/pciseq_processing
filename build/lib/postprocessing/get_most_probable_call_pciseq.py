def get_most_probable_call_pciseq(cellData):
    # create dataframe with most probable cell types
    append_data = pd.DataFrame(columns=['Cell_Num', 'X', 'Y', 'ClassName', 'Prob'])
    
    # create dataframe with most probable cell types
    for i, cell in enumerate(cellData.Cell_Num):
        cell_names = cellData.ClassName[i]
        cell_prob = cellData.Prob[i]
        max_prob = max(cell_prob)
        index = [i for i, j in enumerate(cell_prob) if j == max_prob]
        cellname = cell_names[index[0]]
        X = cellData.X[i]
        Y = cellData.Y[i]
        data = [cell, X, Y, cellname, max_prob]
        append_data.loc[i] = data
    return append_data