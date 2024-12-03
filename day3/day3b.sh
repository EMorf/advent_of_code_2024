grep -o 'do()\|don'\''t()\|mul([0-9]\+,[0-9]\+)' data.txt | \
awk '
BEGIN { enabled = 1; sum = 0 }
{
    if ($0 == "do()") enabled = 1;
    else if ($0 == "don'\''t()") enabled = 0;
    else if (enabled && match($0, /mul\(([0-9]+),([0-9]+)\)/, groups)) {
        sum += groups[1] * groups[2];
    }
}
END { print sum }
'