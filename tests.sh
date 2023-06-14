echo ~~~~ Runing Pipeline ~~~~
cd data
python pipeline.py
cd ..
echo  ~~~~ Executing automated tests for the project. ~~~~ 
cd project
python tests.py
cd ..
echo ~~~~ Testing done. ~~~~