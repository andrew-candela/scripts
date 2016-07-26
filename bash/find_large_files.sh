if [ -z $1 ]; then
    dir=.
else
    dir=$1
fi

find $dir -type f -exec du -ah {} + | sort -h -r
