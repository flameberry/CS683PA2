#!/bin/bash

# Check if trace filename is given
if [ -z "$1" ]; then
  echo "Usage: $0 <trace_file_name>"
  exit 1
fi

TRACE=$1
TRACE=$1
TRACE_PATH="../../Traces/$TRACE"

# Check if the trace file exists
if [ ! -f "$TRACE_PATH" ]; then
  echo "Error: Trace file '$TRACE_PATH' not found!"
  exit 1
fi

TRACE_BASENAME=$(basename "$TRACE" .xz)  # Strip .xz for output filenames

mkdir -p results/no
mkdir -p results/ipstride_prefetcher
mkdir -p results/offset_prefetcher
# Run simulations and redirect outputs
bin/champsim-no -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../../Traces/$TRACE > results/no/${TRACE_BASENAME}.txt
bin/champsim-ip_stride -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../../Traces/$TRACE > results/ipstride_prefetcher/${TRACE_BASENAME}.txt
bin/champsim-offset_prefetcher_32 -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../../Traces/$TRACE > results/offset_prefetcher/${TRACE_BASENAME}_32.txt
bin/champsim-offset_prefetcher_64 -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../../Traces/$TRACE > results/offset_prefetcher/${TRACE_BASENAME}_64.txt
bin/champsim-offset_prefetcher_128 -warmup_instructions 25000000 -simulation_instructions 25000000 -traces ../../Traces/$TRACE > results/offset_prefetcher/${TRACE_BASENAME}_128.txt

