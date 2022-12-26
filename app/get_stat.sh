bmon -p $1 -o 'ascii:diagram=detailed;quitafter=1' | grep --line-buffered Bytes | awk '{print $2 " " $3}'
