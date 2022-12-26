# Mizun
A service connected to a Telegram bot that generates fake upload. Usually used to bypass the 1/10 traffic raito limit in some datacenters 🤷🏻‍♂️

<div align="left">
  <p> <img src="bot.png?raw=true "bot"" width="500"> </p>  
</div>

1. Create a bot in @BotFather and place the token in docker-compose.yml (BOT_TOKEN)
2. Find your Telegram uid wih @GetIDsBot, then place it in docker-compose.yml (ADMIN_UID)
3. Place your main NIC name (the interface that you want to monitor) and place it in docker-compose.yml (NIC_NAME)
4. Run ```docker-compose build .``` to biuld.
5. Run ```docker-compose up -d``` to run.
