    echo $1 
    stateFile="./state/SBP-level1.txt"
    
    echo "********************************************************"
    echo "**********************${stateFile}**********************"
    echo "********************************************************"
    python3 ./main.py $stateFile
    echo "********************************************************"
    echo "**********************  COMPLETE  **********************"
    echo "********************************************************"