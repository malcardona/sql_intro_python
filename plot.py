    
    
def plot_31(x1, x2, x3, y1, y2, y3) :    
    fig = plt.figure()
    # ax = fig.add_subplot(nrows, ncols, index)
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.scatter(x1, y1, s = 1, color='b', marker='^')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title("tranquila")
    ax1.set_ylabel("Pulso")
    ax1.set_ylim([50, 65])
    ax1.set_xlim([0, 14800])
    
    ax2.scatter(x2, y2, s = 1, color='c', marker='+')
    ax2.set_facecolor('whitesmoke')
    ax2.set_title("entusiasmada")
    ax2.set_ylabel("Pulso")
    ax2.set_ylim([85, 140])
    ax2.set_xlim([0, 14800])
    
    ax3.scatter(x3, y3, s = 1, color='g', marker='.')
    ax3.set_facecolor('whitesmoke')
    ax3.set_title("aburrida")  
    ax3.set_ylabel("Pulso")
    ax3.set_xlabel("[i]")
    ax3.set_ylim([63, 86])
    ax3.set_xlim([0, 14800])
    
    plt.show() 

def plot_3in1(x1, x2, x3, y1, y2, y3) :    
    fig = plt.figure()
    # ax = fig.add_subplot(nrows, ncols, index)
    ax = fig.add_subplot(3, 1, 1)
    
    ax.scatter(x1, y1, s = 1, color='b', marker='^')
    ax.scatter(x2, y2, s = 1, color='c', marker='+')
    ax.scatter(x3, y3, s = 1, color='g', marker='.')
    ax.set_facecolor('whitesmoke')
    ax.set_xlabel("[i]")
    ax.set_ylabel("Pulso")
    ax.set_ylim([50, 140])
    ax.set_xlim([0, 14800])
    plt.show() 