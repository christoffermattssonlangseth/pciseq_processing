def confusion_in_calling_normalized(cellData, most_probable):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt 
    import seaborn as sb
    cellxgene_prob = pd.DataFrame(index=np.arange(len(cellData)), columns=np.arange(len(np.unique(list(most_probable.ClassName)))))
    cellxgene_prob.columns=np.unique(list(most_probable.ClassName))
    for i, cell in enumerate(cellData.Cell_Num):
        for j, gene in enumerate(np.unique(list(most_probable.ClassName))):
            gene_count_dict = dict(zip(cellData.ClassName[i], cellData.Prob[i]))
            try: 
                count = gene_count_dict[gene]
            except KeyError:
                count = 0
            cellxgene_prob.loc[cellxgene_prob.index[i], gene] = count
                                  
    cellxgene_prob = cellxgene_prob.fillna(0)
    cellxgene_prob.insert(0,'ClassName', most_probable.ClassName)
    
    cellxgene_prob_index = cellxgene_prob.set_index('ClassName')
    cellxgene_prob_index_mean = cellxgene_prob_index.groupby(by=cellxgene_prob_index.index, axis=0).mean()
    
    sum_probabilites = pd.DataFrame(index=np.arange(len(np.unique(list(most_probable.ClassName)))), columns=np.arange(len(np.unique(list(most_probable.ClassName)))))
    sum_probabilites.columns=np.unique(list(most_probable.ClassName))
    
    NEW_cellxgene_prob = pd.DataFrame(index=np.arange(len(np.unique(list(most_probable.ClassName)))), columns=np.arange(len(np.unique(list(most_probable.ClassName)))))
    NEW_cellxgene_prob.columns=np.unique(list(most_probable.ClassName))
    for i, celltype in enumerate(np.unique(cellxgene_prob_index.index)):
        values = list(cellxgene_prob_index.groupby(by=cellxgene_prob_index.index, axis=0).get_group(celltype).sum(axis = 0))
        values_normalized = np.array(values)/max(values)
        NEW_cellxgene_prob[celltype] = list(values_normalized)
    
    
    x_axis = NEW_cellxgene_prob.index
    y_axis = NEW_cellxgene_prob.columns
    #cellxgene_prob = np.log2(cellxgene_prob+1)
    plt.rcParams["figure.figsize"] = (50,25)
    sb.set(font_scale=1)
    plt.rcParams['figure.dpi'] = 100
    ax = sb.heatmap(NEW_cellxgene_prob, xticklabels=x_axis, yticklabels=y_axis,cmap="YlGnBu")
    return NEW_cellxgene_prob, cellxgene_prob_index
