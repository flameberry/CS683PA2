#!/bin/bash
TRACE_NAME="trace1.champsimtrace.xz"
echo "Generating Log files for trace file: ${TRACE_NAME}"
./run_trace.sh ${TRACE_NAME}

TRACE_NAME="trace2.champsimtrace.xz"
echo "Generating Log files for trace file: ${TRACE_NAME}"
./run_trace.sh ${TRACE_NAME}

TRACE_NAME="trace3.champsimtrace.xz"
echo "Generating Log files for trace file: ${TRACE_NAME}"
./run_trace.sh ${TRACE_NAME}

TRACE_NAME="trace4.champsimtrace.xz"
echo "Generating Log files for trace file: ${TRACE_NAME}"
./run_trace.sh ${TRACE_NAME}

echo "All log files generated for all traces"
