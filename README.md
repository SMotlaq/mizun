# Mizun
A service connected to a Telegram bot that generates fake upload. Usually used to bypass the 1/10 traffic raito limit in some datacenters 🤷🏻‍♂️

<div align="left">
  <p> <img src="bot.png?raw=true "bot"" width="500"> </p>  
</div>

## Run

1. Create a bot in @BotFather and place the token in docker-compose.yml (BOT_TOKEN)
2. Find your Telegram uid wih @GetIDsBot, then place it in docker-compose.yml (ADMIN_UID)
3. Place your main NIC name (the interface that you want to monitor) and place it in docker-compose.yml (NIC_NAME)
4. Run ```docker-compose build .``` to biuld.
5. Run ```docker-compose up -d``` to run.

## Bot usage

1. Hit `/get_stat` to get the TX (upload), RX (download), and Ratio (upload / download)
2. The `/upload SIZE SPEED_LIMIT DESTINATION` command need 3 parameters:
 1. SIZE: The amount of bytes you want to upload (in MiB)
 2. SPEED_LIMIT: The maximum rate of transfer. Foe example 10m (10MiB/s) or 250k (250KiB/s)
 3. DESTINATION: The desination host. For example twitch.tv
 
 ***NOTE: It's not an attack!*** The random data will send to the port 53. It will be droped at the edge because this port is closed (probably!) in the destinaion host
