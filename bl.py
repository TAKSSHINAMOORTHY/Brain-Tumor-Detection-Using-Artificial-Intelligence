import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_block_diagram():
    fig, ax = plt.subplots(figsize=(12, 2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    
    blocks = [
        "Image Input\n(load_model)", 
        "Preprocessing\n(cvtColor)", 
        "Segmentation\n(threshold)", 
        "Feature Extraction\n(findContours)", 
        "Tumor Detection\n(predict)", 
        "Result Display\n(displayImage)"
    ]
    positions = [1, 3, 5, 7, 9, 11]
    
    for pos, text in zip(positions, blocks):
        rect = patches.Rectangle((pos, 0.5), 1.5, 1, edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        ax.text(pos + 0.75, 1, text, fontsize=10, ha='center', va='center')
    
    for i in range(len(positions) - 1):
        ax.arrow(positions[i] + 1.5, 1, 0.5, 0, head_width=0.2, head_length=0.3, fc='black', ec='black')
    
    plt.show()

draw_block_diagram()
