echo ~~~~ Runing Pipeline ~~~~
cd data
python pipeline.py
if [ $exit_status -ne 0 ]; then
  echo "Error: Python script encountered an error."
  exit $exit_status
fi
cd ..
echo  ~~~~ Executing automated tests for the project. ~~~~ 
cd project
python tests.py
if [ $exit_status -ne 0 ]; then
  echo "Error: Python script encountered an error."
  exit $exit_status
fi
cd ..
echo ~~~~ Testing done. ~~~~