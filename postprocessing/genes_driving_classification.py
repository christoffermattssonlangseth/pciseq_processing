def genes_driving_classification(cellData, cellxgene, polygon_file):
    
    from shapely.geometry import Polygon, Point,LineString,  mapping
    import json
    import geojson
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sb
    
    all_genes = [] 
    for i, cell in enumerate(cellData.Genenames):
        all_genes.extend(cell)
    all_genes = np.unique(all_genes)
    all_genes = list(all_genes)

    all_cells = cellxgene.dropna()
    
    with open(polygon_file,'r') as r:
        shapejson = geojson.load(r)
    
    #last element in the geojson file is the column axis, so ignore it for now
    layer_annotations = shapejson
    cell_is_in_layer = {p["name"]:[Polygon(p["coordinates"][0]).intersects(Point(a))  for a  in cellxgene[["x","y"]].values] for ii,p in enumerate(layer_annotations)}
    
    cellxgene["layer"] = "outside_VISp"
    for k in cell_is_in_layer.keys():
        cellxgene.loc[cell_is_in_layer[k],["layer"]] = k
        
    #color_dataframe_2 = pd.DataFrame.from_dict(reference_cluster_color_dict,orient='index').sort_index()
    all_cells_no_nan = all_cells.dropna()
    all_cells_no_nan_index_only_genes = all_cells_no_nan.filter(all_genes).transpose().astype(float)
    all_cells_no_nan_index_only_genes_mean = all_cells_no_nan_index_only_genes.groupby(by=all_cells_no_nan_index_only_genes.columns, axis=1).mean()
    all_cells_no_nan_index_only_genes_tranposed_mean_log2_tranposed = np.log2(all_cells_no_nan_index_only_genes_mean+1).transpose()

    x_axis = all_cells_no_nan_index_only_genes_tranposed_mean_log2_tranposed.columns
    y_axis = all_cells_no_nan_index_only_genes_tranposed_mean_log2_tranposed.index
    plt.rcParams["figure.figsize"] = (50,50)
    sb.set(font_scale=0.4)
    ax = sb.clustermap(all_cells_no_nan_index_only_genes_tranposed_mean_log2_tranposed, xticklabels=x_axis, yticklabels=y_axis,cmap="YlGnBu") #metric="correlation"
    #ax.set_title('HCA09_1')
    plt.rcParams['figure.dpi'] = 500

    plt.show()