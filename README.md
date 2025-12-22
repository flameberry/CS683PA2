# CS683 (Advanced Computer Architecture) - Programming Assignment 2

## Problem Statement

### Task 1: Implement a region-based offset prefetcher at the L2 cache.

- Where the region corresponds to an OS page.

- The design should utilise a table that is indexed by a signature that uniquely represents each page. (Hint: Think of IP-stride prefetcher)

- The table should store the offsets observed within that page. Each table entry should maintain up to five offsets, tracking their frequencies to prioritise which offsets should be used for prefetching.

- Ensure prefetch requests remain within the same page region.

- Implement an accuracy checker as a part of your prefetcher that evaluates the usefulness of prefetches and determines which offset(s) to fetch and to what level of aggressiveness in terms of prefetch degree.

- The overall objective is to design a prefetcher that dynamically adapts to the memory access patterns within each page, balancing coverage, accuracy, and overhead while avoiding useless prefetches.

### Task 2: Implement an exclusive cache hierarchy instead of the existing non-inclusive one.

- At any point of time, a cache block must exist in atmost 1 level of the entire cache hierarchy.

### Task 3: Combine the implementations of task 1 and task 2.

- In this task, we need to extend our L2-based offset prefetcher to work with an exclusive cache hierarchy. As stated in task 2, in an exclusive cache hierarchy, the higher-level cache acts as a victim cache for lines evicted from the lower-level cache. As a result, the accesses observed by your L2 prefetcher will include load requests raised due to L1D misses, as well as the writeback of all evicted lines (both dirty and clean). Task is to update our L2 prefetcher to observe and learn from these additional accesses due to writeback lines.

## Report on the Assignment

[You can view the assignment report here.](./CS683PA2_Summary.pdf)

## ChampSim Instructions

<details>
<summary>Below is the README of how this version of ChampSim can be compiled and run.</summary>

<p align="center">
  <h1 align="center"> ChampSim </h1>
  <p> ChampSim is a trace-based simulator for a microarchitecture study. You find the required trace files at (https://drive.google.com/drive/folders/1S24pPoTCJZkC8cYOv2QsDS5dPjT05fEQ) <p>
</p>

# Compile

To makes things simper, you are only required to specify three parameters: L1D prefetcher, STLB prefetcher, and the number of cores.
For example, `./build_champsim.sh no` builds a single-core processor with no L2 data prefetcher .

```
$ ./build_champsim.sh ip_stride

$ ./build_champsim.sh ${L2_PREFETCHER}
```

NOTE : For exclusive cache hierarchy use "build_champsim_exclusive.sh"

# Run simulation

**Single-core simulation**

```
./[BINARY] -warmup_instructions [N_WARM] -simulation_instructions [N_SIM] -traces [TRACE_DIR]/[TRACE]
$ ./champsim-no -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../traces/trace1.champsimtrace.xz

${BINARY}: ChampSim binary compiled by "build_champsim.sh" (champsim_no)
${N_WARM}: number of instructions for warmup (25 million)
${N_SIM}:  number of instructinos for detailed simulation (25 million)
${TRACE_DIR}: directory where the trace is located (../traces/)
${TRACE}: trace name (trace1.champsimtrace.xz)
```

# Evaluate Simulations

ChampSim measures the IPC (Instruction Per Cycle) value as a performance metric. <br>
There are some other useful metrics printed out at the end of simulation. <br>

# Evaluate Simulations

ChampSim measures the IPC (Instruction Per Cycle) value as a performance metric. <br>
There are some other useful metrics printed out at the end of simulation. <be>

## Steps to download gcc version 7 in ubuntu:

1. sudo apt update
2. sudo add-apt-repository ppa:ubuntu-toolchain-r/test
3. vim /etc/apt/sources.list or sudo nano /etc/apt/sources.list
4. Update the last line with "deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main universe"
5. sudo add-apt-repository ppa:ubuntu-toolchain-r/test
6. sudo apt-get install gcc-7
7. sudo apt-get install g++-7
8. sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 0
9. sudo update-alternatives --install /us/bin/gcc gcc /ust/bin/gcc-7 0

--In case the GCC and G++ is already present in /usr/bin (run ./gcc-7 -v in /usr/bin), install the alternative and set it using

1. sudo update-alternatives --config g++
2. sudo update-alternatives --config gcc

## Task-1 Related Updates

1. For Offset based L2 Prefetcher, 3 exectable with name "champsim-offset_prefetcher_32 ", "champsim-offset_prefetcher_64" and "champsim-offset_prefetcher_128 " are created for region table sizes: 32, 64, 128 entries.

2. To generate log files run ./exec_Champsim.sh it will overwrite existing logfile in results folder.

3. To generate log file for offset based L2 prefetcher only run ./exec_Champsim_only_offset_prefetcher.sh it will overwrite existing logfile in results/offset_prefetcher folder.

4. Log files already generated in results folder

5. Speedup plot is inside Plots folder with name speedup_comparison.png

6. Report created with file name PA2_Report_Task1.pdf.

7. Report word document link is https://docs.google.com/document/d/1ZNq191BENL2XivH-ldjXcak9XHE1RQHVuHQw-04ubBo
</details>
