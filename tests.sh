echo ~~~~ Runing Pipeline ~~~~
cd data
python pipeline.py
if [ -n "$exit_status" ] && [ "$exit_status" -ne 0 ]; then
  echo "Error: Python script encountered an error."
  exit $exit_status
f
cd ..
echo  ~~~~ Executing automated tests for the project. ~~~~ 
cd project
python tests.py
if [ -n "$exit_status" ] && [ "$exit_status" -ne 0 ]; then
  echo "Error: Python script encountered an error."
  exit $exit_status
f
cd ..
echo ~~~~ Testing done. ~~~~