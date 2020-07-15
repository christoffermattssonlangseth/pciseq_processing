def plot_cell_type_distribution_cortex(data, data_layer_column, data_cluster_column, data_color_column,layer_color, title): 
    
    
    """The point of this function is for me to be able to plot layer statistics in an easy and convenient way. 
    
    INPUT: 
    - The input *DATA* should be pandas dataframes
    - The annotation table should include a color code and a cluster column with names that match the names in the input *DATA*
    """
    
    
    import pandas as pd
    import numpy as np
    import scipy.stats as scipy
    import matplotlib.pyplot as plt 
    
    all_layers = list(np.unique(data[data_layer_column]))
    all_layers.remove('outside_VISp')
    cluster_to_color = dict(zip(data[data_cluster_column], data[data_color_column]))
    layer_color = layer_color.set_index('layer')
    list_of_all_clusters  = list(np.unique(data[data_cluster_column]))
    df1 = pd.DataFrame(index = list_of_all_clusters)

    fig, axs = plt.subplots(6,1, figsize=(10, 10), facecolor='w', edgecolor='k')
    #plt.rcParams['figure.dpi'] = 200

    plt.rc('figure', figsize=(15, 1.5))  
    group_layer = data.groupby(data_layer_column)
    group_cluster = data.groupby(data_cluster_column)
    
    for i, layers in enumerate(all_layers):
        intermediate_df = group_layer.get_group(layers)
        count_list = []
        cluster_list = []
        
        for j, cluster in enumerate(list(np.unique(intermediate_df[data_cluster_column]))):
            group_layer_cluster = intermediate_df.groupby(data_cluster_column)
            intermediate_intermediate_df = group_layer_cluster.get_group(cluster)
            intermediate_original = group_cluster.get_group(cluster)
            cluster_list.append(cluster)
            count_int = len(intermediate_intermediate_df)/len(intermediate_original)
            count_list.append(count_int)

        intermediate_dict = dict(zip(cluster_list, count_list))
        difference = (list(set(list_of_all_clusters) - set(cluster_list)))

        for k, not_there in enumerate(difference):
            intermediate_dict[not_there] = 0

        dataframe_counts = pd.DataFrame.from_dict(intermediate_dict, orient='index')
        dataframe_counts = dataframe_counts.sort_index()
        dataframe_counts['color'] = dataframe_counts.index.map(cluster_to_color)

        df1.insert(i,layers,dataframe_counts[0])

        axs[i].set_ylim([0, 1])
        axs[i].bar(dataframe_counts.index, dataframe_counts[0],color = dataframe_counts['color']) 
        axs[i].set_facecolor(list(layer_color.loc[layers])[0])
        fig.suptitle(title, fontsize=20)
        axs[i].set_ylabel(layers)

        if layers == 'L1_polygon' or layers == 'L2_polygon' or layers == 'L3_polygon' or layers == 'L4_polygon' or layers == 'L5_polygon':   
            axs[i].get_xaxis().set_ticks([])
            axs[i].get_yaxis().set_ticks([])
        else:
            axs[i].get_yaxis().set_ticks([])
            plt.xticks(dataframe_counts.index,list_of_all_clusters, rotation='vertical')
    return df1