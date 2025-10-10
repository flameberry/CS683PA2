import matplotlib.pyplot as plt
import numpy as np

# Data from the tables
traces = ['trace1', 'trace2', 'trace3', 'trace4']

# Speedup values
baseline = [1.0, 1.0, 1.0, 1.0]
ip_stride = [0.901, 0.897, 0.910, 0.905]
#offset_32 = [1.138, 1.114, 1.232, 1.119]
#offset_64 = [1.138, 1.114, 1.232, 1.119]
offset_128 = [0.979, 0.955, 1.092, 0.963]

# Set up the positions
x = np.arange(len(traces))
width = 0.30 # Width of the bars

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot bars for each prefetcher type
ax.bar(x - 0.5*width, ip_stride, width, label='IP-Stride', color='skyblue')
#ax.bar(x - 0.5*width, offset_32, width, label='Offset (32 entries)', color='lightcoral')
#ax.bar(x + 0.5*width, offset_64, width, label='Offset (64 entries)', color='orange')
ax.bar(x + 0.5*width, offset_128, width, label='Offset-prefetcher', color='lightgreen')

# Add horizontal dashed line for baseline
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Baseline (Non exclusive with No Prefetcher)')

# Customize the plot
#ax.set_xlabel('Trace Files')
ax.set_ylabel('Speedup [IPC With Prefetcher exclusive/IPC of non exclusive (No prefetcher)]')
ax.set_title('Speedup Comparison of L2 prefetchers exclusive Over Baseline non inclusive (no prefetching)')
ax.set_xticks(x)
ax.set_xticklabels(traces)
ax.set_ylim(0.8, 1.3)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Add value labels on top of bars
for i, val in enumerate(ip_stride):
    ax.text(i - 0.5*width, val + 0.005, f'{val:.3f}', ha='center', va='bottom')
#for i, val in enumerate(offset_32):
#    ax.text(i - 0.5*width, val + 0.005, f'{val:.3f}', ha='center', va='bottom')
#for i, val in enumerate(offset_64):
#    ax.text(i + 0.5*width, val + 0.005, f'{val:.3f}', ha='center', va='bottom')
for i, val in enumerate(offset_128):
    ax.text(i + 0.5*width, val + 0.005, f'{val:.3f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('speedup_exclusive_baseline_no_prefetcher_non_inclusive.png', dpi=300, bbox_inches='tight')
plt.show()
