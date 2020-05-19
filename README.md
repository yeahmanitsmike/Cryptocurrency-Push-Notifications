# Cryptocurrency Push Notifications

# Introduction
This project utilizes Slack apps and the CoinMarketCap API to create hourly (or however frequently you desire) push notifications sent to one's phone or computer. The project uses a Python script to work with the API and the JSON, then uses a Bash script to make the curl request to Slack. As of this moment, this script only works in an environment that supports Bash.

# How It Works
Getting Slack Set up
1. After cloning this repo, download Slack on your computer and/or smartphone. https://slack.com/
2. Create an account and a new Workspace. https://slack.com/get-started#/
3. Once you set up a new Workspace, set up a channel for your BTC Notifications. 
4. Click on the "Apps" tab in the left column and click "Browse App Directory." This will redirect your new Workspace's website.
5. Once on the website, click the "Build" button in the top right corner. This will take you to the Slack API page.
6. You then click the "Start Building" button in the center of the page.
7. This will bring up a window that allows you to create your app name and select the Workspace it will reside in. Choose the Workspace that you just made.
8. When the app has been created, you will be redirected to the app's settings webpage. From here, you will click on the "Incoming Webhooks" button in the middle of the page. On the next page, toggle the "Activate Incoming Webhooks" switch to on. 
9. Once the switch is on, you will go to the bottom the page and click the "Add New Webhook to Workspace" button. This will take you to page that allows you to choose the channel the app will be placed in. Place the app in the new channel you made in Step 3.
10. After that, the curl request will now display with your personal Slack channel URL. Copy that curl request.
11. Now, go into the Bash script in this repo and paste it to Line 8 in the Bash Script. You are now set up on the Slack end of things. 

Getting CoinMarketCap API Set Up
1. Navigate to https://coinmarketcap.com/api/ 
2. Do not worry! CoinMarketCap has a free version of their API. 
3. Click the "GET YOUR API KEY NOW" button in the middle of the page and sign up on the next page. Click their "Basic Plan."
4. Once you signed up, you will be redirected to your account's web page. From here move your mouse cursor under the "API Key" section and click "COPY KEY."
5. You now have the API Key. So go into the python script and paste your API key into Line 8. 
6. Congrats you are all set up!

Running the Script
1. From here, all you have to do is run the script!
2. Type "python3 btc_sms.py" and your script will send a notification to your Slack channel every hour. 


