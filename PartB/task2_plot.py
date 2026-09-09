import matplotlib.pyplot as plt

# Data
capacity_bytes = [262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]
capacity_log2 = [i for i in range(8, 15)]  # log2(capacity in kB): 256kB=8, 512kB=9, etc.
access_time = [2.06194, 2.12662, 2.31353, 2.53575, 3.13418, 3.82213, 5.28284]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(capacity_log2, access_time, marker='o', color='steelblue', linewidth=2, markersize=6)

plt.xlabel('log₂(Cache Capacity in kB)')
plt.ylabel('Access Time (ns)')
plt.title('CACTI Access Time vs. Cache Capacity (45nm, 8-way, corrected config)')
plt.xticks(capacity_log2, ['256kB', '512kB', '1MB', '2MB', '4MB', '8MB', '16MB'])
plt.grid(True)
plt.tight_layout()
plt.show()