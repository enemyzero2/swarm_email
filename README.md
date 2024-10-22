# 📧 swarm_email 🐝

![Build Status](https://img.shields.io/github/workflow/status/enemyzero2/swarm_email/CI) ![License](https://img.shields.io/github/license/enemyzero2/swarm_email) ![Dependencies](https://img.shields.io/librariesio/github/enemyzero2/swarm_email)

Private email sender with a touch of fun! 🎉

## ✨ Features

- Send personalized emails with ease 📧
- Schedule emails to be sent at specific times ⏰
- Add attachments to your emails 📎
- Use OpenAI's API to generate email content 🤖

## 🚀 Installation Instructions

1. Clone the repository: `git clone https://github.com/enemyzero2/swarm_email.git` 🐙
2. Navigate to the project directory: `cd swarm_email` 📂
3. Install the dependencies: `pip install -r requirements.txt` 📦

## 🛠️ Usage Instructions

1. Run the application: `python app.py` 🚀
2. Follow the prompts to send your emails with ease! 📧

## 🛠️ New Agent: ela

A new agent named `ela` has been added to manage the database. This agent will track email content and add necessary events and schedules to the database.

## 🛠️ Configuring MySQL Database Connection

To configure the MySQL database connection, add the following environment variables to your configuration:

- `MYSQL_HOST`: The hostname of your MySQL server
- `MYSQL_USER`: The username to connect to the MySQL server
- `MYSQL_PASSWORD`: The password to connect to the MySQL server
- `MYSQL_DB`: The name of the database to use

## 🤝 Contributing Guidelines

We welcome contributions! Feel free to open issues or submit pull requests. Let's make this project even better together! 🌟

## 📚 Project principle

This project is a private email sender written in Python. It generates email content by calling OpenAI's API and sends emails using the SMTP protocol. The main functions of the project include reading local files, generating email content, and sending emails. 🎉
