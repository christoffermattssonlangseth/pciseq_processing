def heatmap_layer_count(data, cmap_to_use, title):
    import matplotlib.pyplot as plt
    import seaborn as sb
    data = data.dropna()
    x_axis = data.columns
    y_axis = data.index
    plt.rcParams["figure.figsize"] = (10,10)
    #sb.set(font_scale=2)
    ax = sb.heatmap(data, xticklabels=x_axis, yticklabels=y_axis,cmap=cmap_to_use)
    ax.set_title(title)
    plt.show()