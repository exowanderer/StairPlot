def stairPlot(data, fig=None, ax=None, clearAx=True, **kwargs):
    
    try:
        num_rows, num_columns = np.shape(data)
    except ValueError:
        raise Exception('Array must 2-dimensional')
    
    if num_rows < num_columns:
        data = np.transpose(data)
        stare_plot(data)
        return
    
    if fig is None or ax is None:
        fig, ax = plt.subplots(num_columns, num_columns)
    
    if clearAx:
        for axNow in np.ravel(ax):
            axNow.clear()
        
        del axNow
    
    for i in range(num_columns):
        for j in range(num_columns):
            # scatter column_j on the x-axis vs colmn_i on the y-axis
            if i > j:
                ax[i][j].scatter(data[:,j], data[:,i], **kwargs)
            if i > j:
                ax[i][j].set_axis(False)
            
            # unless i == j, in which case show the histogram or KDE
            if i == j:
                ax[i][j].hist(data[:,i], bins=data[:,i].size//10, normed=True)
            
            if i < num_columns - 1:
                ax[i][j].xaxis.set_visible(False)
            if j > 0 and i != j:
                ax[i][j].yaxis.set_visible(False)
                
    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    # ax[0][0].set_ylim(ax[0][1].get_ylim())
