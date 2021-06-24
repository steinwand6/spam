FILE_NAME='./cli.py'
#FILE_NAME='players/abanlin.filler'
ENEMY='./nop.py'
#ENEMY='players/abanlin.filler'

rm -rf result
for ((i = 0; i < 5; i++))
do
    ./filler_vm -p2 $ENEMY -p1 $FILE_NAME -f maps/map00
    cat filler.trace | grep -e 'won' >> result
done

for ((i = 0; i < 5; i++))
do
    ./filler_vm -p1 $ENEMY -p2 $FILE_NAME -f maps/map00
    cat filler.trace | grep -e 'won' >> result
done

ALL=$(cat result | wc -l)
echo '+++++++++++++++++++++++++++++++' >> result
cat result | grep -c "$FILE_NAME won" >> result
echo "all $ALL" >> result
