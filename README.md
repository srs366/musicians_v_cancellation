# Data analysis
- PROJECT NAME: Musicians vs. Cancel Culture
- WHAT OUR PROJECT SETS OUT TO DO:
  - Utilised Python, Pandas, Numpy, Matplotlib, Seaborn, Google Cloud, Jupyter Notebook, continuing with RNN, SARIMA, Facebook Prophet, SQL
  - In a team of 4, analysed data comparing musician's listening metrics with public sentiment towards that musician, to see whether backlash would affect consumption of their art.
  - Assumed position of team leader and assigned tasks to teammates.
  - Manually identified 48 artists deemed as cancelled by Twitter.
  - Scraped tweets to then assess their sentiment, utilising Twitter API, a pre-built scraper, and a pre-trained sentiment model to do so.
  - Utilised Chartmetric API to collect artist's daily listeners, radio spins.
  - Stored, cleaned, manipulated datasets containing Tweets, listening metrics for over a years worth of data.
  - Utilising Pandas, MatPlotLib, and Seaborn, graphed and visualised results via Streamlit dashboard.
  - Utilised NLP and NLTK to create wordclouds surrounding artist backlash.
  - Stored data in Google Cloud via buckets.
  - Packaged functions within VS code whilst testing code in Jupyter Notebooks.
  - Now looking to use SARIMA to create machine learning model, RNN to predict artists' listening trends had they not been "cancelled."
  - Now looking to use Facebook Prophet to predict artists' listening trends as mentioned above.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for musicians_v_cancellation in github.com/{group}. If your project is not set please add it:

Create a new project on github.com/{group}/musicians_v_cancellation
Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "musicians_v_cancellation"
git remote add origin git@github.com:{group}/musicians_v_cancellation.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
musicians_v_cancellation-run
```

# Install

Go to `https://github.com/{group}/musicians_v_cancellation` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/musicians_v_cancellation.git
cd musicians_v_cancellation
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
musicians_v_cancellation-run
```
