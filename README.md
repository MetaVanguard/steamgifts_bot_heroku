# steamgifts_bot_heroku

### About
Bot for steamgifts.com deployable to heroku to run on schedule in cloud.
Based on [stilManiac/steamgifts-bot](https://github.com/stilManiac/steamgifts-bot/)

### How to run
Sign in on SteamGifts.com by Steam.
Find PHPSESSID cookie in your browser.
Create [Heroku](https://heroku.com/) account.
Create newa app.
Copy this repository to it.
In settings create variables:
cookie with value of your steamgifts PHPSESSID cookie
pages with number of pages you want bot to go through
Use Scheduler ADD-on to run it on your preffered schedule.
Bot will go through wishlist and if you will have more than 80 points left, then it will spend them in All games list.
