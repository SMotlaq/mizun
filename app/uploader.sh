dd if=/dev/urandom bs=1048576 count=$1 | pv -q -L $2 | nc -w 5 -u $3 53
echo "Done"