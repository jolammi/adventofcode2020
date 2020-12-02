echo "This script runs all the days in order. It helps to check whether all the solutions work."

for i in {1..24}
do
    if [ -d "day$i" ]
    then
        cd day$i
        echo -e "\n\n-------- Current directory: day$i --------"
        echo -e "\n--- Puzzle 1 ---\n"
        python3 puzzle1.py
        echo -e "\n--- Puzzle 2 ---\n"
        python3 puzzle2.py
        cd ..
    fi
done
