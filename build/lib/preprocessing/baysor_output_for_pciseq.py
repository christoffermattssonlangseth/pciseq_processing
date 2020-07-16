def baysor_output_for_pciseq(cell_data, spots_data, singleCellMatrix):
    
    import pandas as pd
    import numpy as np
    
    # prepare cells file
    cell_data = cell_data.drop_duplicates()
    cells = cell_stats[['cell','area','x','y']].copy()
    cells['cell_id'] = cell_data['cell']-1
    cells['fov_id'] = 0
    cells.columns = ['label','area','x',
                     'y','cell_id','fov_id']
    cells = cells.fillna(cells.area.mean()) 
    
    # create dictionary to map the x and y coordintes
    #cell_data_df = cells[['cell','x','y']].copy()
    mapx = dict(zip(cells.label.to_list(), cells.x.to_list()))
    mapy = dict(zip(cells.label.to_list(), cells.y.to_list()))
    
    # prepare spots file
    spots = pd.DataFrame()
    spots['x_global'] = spots_data['x']
    spots['y_global'] = spots_data['y']
    spots['fov_id'] = 0
    spots['label'] = spots_data['cell']
    spots['target'] = spots_data['gene']
    
    spots["x_cell"] = spots['label'].map(mapx)
    spots["y_cell"] = spots['label'].map(mapy)
    
    # filter single cell data 
    genes = np.unique(singleCellMatrix.GeneNames)
    genes_to_remove = (list(set(list(np.unique(spots_raw.gene))).difference(genes)))
    spots_filtered = spots[~spots.target.isin(genes_to_remove)]
    return cells, spots_filtered