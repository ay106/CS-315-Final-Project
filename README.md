# CS-315-Final-Project
CS 315 Final Project  <br />

Pyktok File <br />
2. cd cs-315-final-project/pyktok_code <br />
3. python -m venv .project2  (You'll create a new virtual environment to collect data with pyktok) <br />
4. source .project2/bin/activate (activate it) <br />
5. pip install -r pyktok_code/requirements.txt (will install all packaged you need) <br />

Now you are ready to start collecting data. For you to test, I have included the sample JSON file. But you can use your own JSON file that has the same format. <br />

In the command line: <br />

python3 pyktok-collect.py pyktok_test.json results.csv

Updated what worked for me instead:
python3 pyktok_code/pyktok-collect.py Urls_Run/urls[INSERTYR].json_1.json results.csv
