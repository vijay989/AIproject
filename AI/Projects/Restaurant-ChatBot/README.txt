--------------------------------------------------------------------------
--------------------------------------------------------------------------
For Dependencies installation

##For Windows:

#To check the Python environment is already installed or not
C:\> python3 --version

#If not, then install it using
C:\> pip3 install -U pip

#To create a virtual environment:
C:\> python3 -m venv --system-site-packages ./venv


#To activate the virtual environment:
C:\> .\venv\Scripts\activate


#Install both Rasa and Rasa X using the following code:
C:\>  pip install -r REQUIREMENT.txt

#To install Rasa NLU and Spacy:
C:\> pip install rasa_nlu[spacy]
C:\> python -m spacy download en_core_web_md
C:\> python -m spacy link en_core_web_md en


#If the system prompts you to upgrade pip, then use the following commands:
C:\> python -m pip install --upgrade pip

#If you don't have IDE to run python code install anaconda from below link:
https://docs.anaconda.com/anaconda/install/windows/


--------------------------------------------------------------------------
--------------------------------------------------------------------------
For Configuring the action.py in bot.


1. "Foodie-bot" is the main directory for bot. Please run all the rasa commands in that directory only.
2. Please configure your sender gmail id and password in action.py file. Please update the "sender_email" and "sender_email_pwd" Global variables. It'll not send email without this configuration.
3. Run the action server on one command prompt using "rasa run actions"
4. Run the rasa shell on another  command prompt.



Software used during the Chatbot assignment 

conda==4.7.12
gast==0.2.2
jupyter==1.0.0
python ==3.7.6
platform == windows 10
rasa==1.10.2
rasa-sdk==1.10.1
rasa-x==0.28.6
spacy==2.1.9
tensorflow==2.1.1





