for i in $(ls | grep base_line[0-9] | grep -v txt)
do
    ls -Art $i | tail -n 1 | xargs echo $i
done
