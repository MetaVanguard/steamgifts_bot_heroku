# steamgifts_bot_heroku

### About
Bot for steamgifts.com deployable to heroku to run on schedule in cloud.
Based on [stilManiac/steamgifts-bot](https://github.com/stilManiac/steamgifts-bot/)

### How to run
1. Sign in on SteamGifts.com by Steam.
2. Find PHPSESSID cookie in your browser.
3. Create [Heroku](https://heroku.com/) account.
4. Create new app.
5. Copy this repository to it.
6. In settings create variables:
`cookie` with value of your steamgifts `PHPSESSID` cookie
`pages` with number of pages you want bot to go through
7. Use Scheduler ADD-on to run it on your preffered schedule.
8. Bot will go through wishlist and if you will have more than 80 points left, then it will spend them in All games list.
