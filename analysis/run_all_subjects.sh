#!/bin/bash

declare -a subject_runs=("01 odc" "02 odc1" "03 odc" "04 odc2" "05 odc" "06 odc2" "06 odc3" "07 odc")

for val in "${subject_runs[@]}"; do
    eval '$1 $val';
done
