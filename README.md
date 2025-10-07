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
10. sudo update-alternatives --install /us/bin/gcc gcc /ust/bin/gcc-7 0
    
--In case the GCC and G++ is already present in /usr/bin (run ./gcc-7 -v in /usr/bin), install the alternative and set it using

1. sudo update-alternatives --config g++
2. sudo update-alternatives --config gcc



## Task-1 Related Updates

1. For Offset based L2 Prefetcher, 3 exectable with name "champsim-offset_prefetcher_32 ", "champsim-offset_prefetcher_64" and "champsim-offset_prefetcher_128 " are created for region table sizes: 32, 64, 128 entries.

2. To generate log files run ./exec_Champsim.sh it will overwrite existing logfile in results folder.

3. To generate log file for offset based L2 prefetcher only run ./exec_Champsim_only_offset_prefetcher.sh it will overwrite existing logfile in results/offset_prefetcher folder.

4. Log files already generated in results folder

5. Speedup plot is inside Plots folder with name speedup_comparison.png

6. Report created with file name PA2_Report_Task1.pdf
