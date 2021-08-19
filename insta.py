import instaloader
bot = instaloader.Instaloader()
username = "pythongrowin"
print(bot.download_profile(username, profile_pic_only=True))