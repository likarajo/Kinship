## Introduction:  
Twitter users tweet (post status) about any topic within the character limit, making it a powerful medium of information sharing. ‘Kinship’ is a simple tool that finds out what are the related words (kins) to a particular word that twitter users have twitted.  
For example, if we take into account the word Wimbledon, this tool will fetch the twitter stream of all tweets containing the word Wimbledon, and display the top n most related words - like Federer, Tennis, Champion, record etc. expectedly.

## Requirements:  
### Twitter API:  
- Visit https://apps.twitter.com
- Create New App
- Generate and save the credentials

### Python 3.6.3
- Visit https://www.python.org/downloads/release/python-363
- Download and install Python
- Set environment and path variables

## Libraries:
### twitter  
Install twitter library into **%PYTHON_HOME%\Lib\site-packages**  
`>>> pip install twitter`

### json  
Python 3.6 has json library at **%PYTHON_HOME%\Lib\json**

### nltk  
Install nltk (NLP and tokenizer) library into **%PYTHON_HOME%\Lib\site-packages**. 
`>>> pip install nltk`  
Download and unzip nltk stopwords into **%PYTHON_HOME%\Lib\nltk_data**  
```
>>> import nltk
>>> nltk.download('stopwords')
```

### re  
Python 3.6 has re (regular expressions) module **at %PYTHON_HOME%\Lib\re.py**

### string  
Python 3.6 has string module at **%PYTHON_HOME%\Lib\string.py**

### os  
Python 3.6 has os (operating system) module at **%PYTHON_HOME%\Lib\os.py**

### matplotlib  
Install matplotlib library into **%PYTHON_HOME%\Lib\site-packages**  
`>>> pip install matplotlib`

### datetime  
Python 3.6 has datetime module at **%PYTHON_HOME%\Lib\datetime.py**

### collections  
Python 3.6 has collections library at **%PYTHON_HOME%\Lib\collections**

### tkinter  
Python 3.6 has tkinter library (for GUI development) at **%PYTHON_HOME%\Lib\tkinter**

### pyinstaller  
For creating executable, pyinstaller library needs to be installed into %PYTHON_HOME%\Lib\site-packages. 
`>>> pip install pyinstaller`  
This also installs ** *pypiwin32* ** utilities library of python extension for windows.  
The executable file is created using the following command:  
`> pyinstaller.exe –onefile –windowed –icon=kinship.ico kinship-gui.py`

## Inputs
+ ACCESS_TOKEN
+ ACCESS_SECRET
+ CONSUMER_KEY
+ CONSUMER_SECRET
+ ‘word’
+ No. of ‘kin’ words required (n)
+ Total no. of tweets to be fetched from Twitter Stream for the data corpus  

![alt text](https://raw.githubusercontent.com/likarajo/kinship/master/assets/demo-input.png "input")  

## Output:
A plot displaying the ‘n’ most closely related ‘kins’ that Twitter users use with the given ‘word’  
![alt text](https://raw.githubusercontent.com/likarajo/kinship/master/assets/demo-output.png "input")
