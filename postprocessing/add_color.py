def add_color(data,column_to_map, annotation_file, group_tag, color_tag):
    to_map = dict(zip(annotation_file[group_tag], annotation_file[color_tag]))
    data['color'] = data[column_to_map].map(to_map)
    return data