def create_cellxgene_matrix(cellData, most_probable_call):
    
    import numpy as np
    import pandas as pd
    # create cellxgene matrix
    all_genes = [] 
    for i, cell in enumerate(cellData.Genenames):
        all_genes.extend(cell)
    all_genes = np.unique(all_genes)
    all_genes = list(all_genes)
    all_genes_column = list(all_genes)
    
    cellxgene = pd.DataFrame(index=np.arange(len(most_probable_call)), columns=np.arange(len(all_genes)))
    cellxgene.columns=all_genes
    coordinates_x = []
    coordinates_y = []
    highest_probability = []
    for i, cell in enumerate(cellData.Cell_Num):
        intermediate_x = cellData.X[i]
        intermediate_y = cellData.Y[i]
        coordinates_x.append(intermediate_x)
        coordinates_y.append(intermediate_y)

        cell_prob = cellData.Prob[i]
        max_prob = max(cell_prob)
        highest_probability.append(max_prob)

        for j, gene in enumerate(all_genes):
            gene_count_dict = dict(zip(cellData.Genenames[i], cellData.CellGeneCount[i]))
            try: 
                count = gene_count_dict[gene]
            except KeyError:
                count = 0
            cellxgene.loc[cellxgene.index[i], gene] = count
    cellxgene.insert(0, 'subclass', most_probable_call.ClassName)
    cellxgene['x'] = coordinates_x
    cellxgene['y'] = coordinates_y
    cellxgene['highest_probability'] = highest_probability
    cellxgene_no_zero = cellxgene[cellxgene['subclass'] != 'Zero']
    cellxgene_no_zero_withIndex = cellxgene_no_zero.set_index('subclass')
    return cellxgene_no_zero_withIndex