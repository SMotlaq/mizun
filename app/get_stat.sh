bmon -p ens192 -o 'ascii:diagram=detailed;quitafter=1' | grep --line-buffered Bytes | awk '{print $2 " " $3}'
