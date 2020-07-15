def from_polygon_to_labels(data, x, y, polygon_file, output_prefix):
    """
    The input files needed are the pciSeq output data and annotated polygons for the layers
    """
    from shapely.geometry import Polygon, Point,LineString,  mapping
    import json
    import geojson
    import numpy as np
    
    with open(polygon_file,'r') as r:
        shapejson = geojson.load(r)
    
    #last element in the geojson file is the column axis, so ignore it for now
    layer_annotations = shapejson
    cell_is_in_layer = {p["name"]:[Polygon(p["coordinates"][0]).intersects(Point(a))  for a  in data[[x,y]].values] for ii,p in enumerate(layer_annotations)}
    
    data["layer"] = "outside_VISp"
    for k in cell_is_in_layer.keys():
        data.loc[cell_is_in_layer[k],["layer"]] = k
    data.to_csv(output_prefix + '_all_cells_with_layer_labels.csv', index = False )
    return data