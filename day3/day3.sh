sed -n 's/.*\(mul([0-9]\+,[0-9]\+)\).*/\1/p' data.txt | \
awk -F'[(),]' '{sum += $2 * $3} END {print sum}'