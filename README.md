# ReportBuilder-Agent
A ReAct Agent with Data Analyzing and Visualization tools to answer questions of the user and eventually generate a report with the information gathered over the conversation. 

# Data EDA Assistant

A generative AI web application that can answer questions using Data Analysis and Visualization tools. By default, Kaggles, titanic disaster passengers dataset is used and tools around that data are generated. If the user wishes to use personal data, it can be uploaded to the application and question answering can be carried out.

# Titanic Data EDA Demo

![Logo](https://github.com/gowriks12/ReportBuilder-Agent/blob/main/static/titanic-EDA-video-ezgif.com-video-to-gif-converter.gif)

# Personal Data EDA Demo

![Logo](https://github.com/gowriks12/ReportBuilder-Agent/blob/main/static/personaldataEDA.gif)

# Example Reports

[Titanic Data Report](https://github.com/gowriks12/ReportBuilder-Agent/blob/main/Reports/report_20240826_211247.docx)
[Personal Data Report](https://github.com/gowriks12/ReportBuilder-Agent/blob/main/Reports/report_20240826_211943.docx)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/gowriks12/ReportBuilder-Agent.git
```

Go to the project directory

```bash
  cd ReportBuilder-Agent
```

Create a new virtual environment and install dependencies 

```bash
  pip install -r requirements.txt
```

This command will download the dependencies into the environment


Start the flask server

```bash
  streamlit run app.py
```

In the web application window if you wish to carry out EDA for titanic passenger data, ask in the chat box directly. Add personal data in the form of csv file and ask questions with respect to that. After querying, if necessary, generate the report and download it.

