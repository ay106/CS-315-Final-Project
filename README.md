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

RUNNING TRANSCRIPTION NOTEBOOK ON A MAC
1. Download ffmpeg-n5.1-latest-linux64-gpl-5.1.tar.xz from this link https://github.com/BtbN/FFmpeg-Builds/releases
2. Unzip and put it into the folder with the notebook
3. go into the folder -> bin -> ffmpeg and put ffmpeg into the same folder with the notebook
4. in the terminal type 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

5. run the following on the terminal: 
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mirayagupta/.zprofile

6. run ths on the terminal: 
eval "$(/opt/homebrew/bin/brew shellenv)"

7. run this on the terminal (this takes a while)
brew install ffmpeg

8. Now run the notebook
