import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Load data
df = pd.read_csv('task3_sweep.csv')
df['DeltaV_mV'] = df['DeltaV'] * 1000

# Sort values by VDD ascending for clean linear interpolation
df = df.sort_values('VDD')

# 2. Interpolate the exact VDD value where DeltaV = 25 mV
vdd_limit = np.interp(25.0, df['DeltaV_mV'], df['VDD'])

# 3. Create Plot
plt.figure(figsize=(10, 6))
plt.plot(df['VDD'], df['DeltaV_mV'], marker='o', color='tab:blue', label='Simulated ΔV')

# Add 25mV threshold line
plt.axhline(y=25, color='red', linestyle='--', label='25mV Sense-Amp Offset Threshold')

# 4. Highlight the limit point
plt.plot(vdd_limit, 25, marker='o', color='red', markersize=8, zorder=5) # Red dot at intersection

# Vertical guide line down to x-axis
plt.axvline(x=vdd_limit, color='red', linestyle=':', alpha=0.7)

# Annotation Box
plt.annotate(
    f'Limit VDD ≈ {vdd_limit:.2f}V',
    xy=(vdd_limit, 25),
    xytext=(vdd_limit + 0.08, 45),
    arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5),
    fontsize=10,
    weight='bold'
)

# Formatting
plt.xlabel('Supply Voltage VDD (V)', fontsize=11)
plt.ylabel('Bitline Differential ΔV (mV)', fontsize=11)
plt.title('SRAM Read Differential vs VDD', fontsize=13)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

plt.savefig('task3_plot_highlighted.png', dpi=300, bbox_inches='tight')
plt.show()