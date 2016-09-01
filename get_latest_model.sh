for i in $(ls | grep dim100.test)
do
    ls -Art $i | tail -n 1 | xargs echo $i
done
