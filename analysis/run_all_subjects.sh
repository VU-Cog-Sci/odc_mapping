#!/bin/bash

declare -a subject_runs=("bm odc" "de odc1" "eo odc" "ms odc2" "ns odc" "tk odc2" "tk odc3" "tr odc")

for val in "${subject_runs[@]}"; do
    eval '$1 $val';
done
