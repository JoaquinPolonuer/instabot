
from instapy import InstaPy
from instapy import set_workspace
from sys import platform
import os
import time

# Setea la carpeta donde guardaremos los registros y la info
set_workspace(os.getcwd())

# crea una sesion
# headless = True es sin abrir el navegador
user = input("ingresar usuario: ")
passwd = input("ingresar contraseña: ")
etiquetas = input("ingresar hashtags separados por un espacio: ").split()
accounts = input("ingresar cuentas similares separadas por un espacio:").split()
comentarios = input("ingresar comentarios separados por guiones bajos: ").split("_")

if platform == "linux" or platform=="linux2":
    session = InstaPy(username=user, password=passwd,headless_browser=True, geckodriver_path='./geckodriver')
else:
    session = InstaPy(username=user, password=passwd,headless_browser=True)

# se loguea a instagram
session.login()

# seteamos los parametros que vamos a utilizar
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=50)
session.set_quota_supervisor(
    enabled=True, peak_comments_daily=15, peak_comments_hourly=2, peak_follows_daily=70, peak_follows_hourly=4, peak_likes_daily=300, peak_likes_hourly=20)

session.set_comments(comentarios)
session.set_relationship_bounds(enabled=True,
                                delimit_by_numbers=True,
                                max_followers=5000,
                                min_followers=20,
                                min_following=77)


# comenzamos a usar el bot
for i in range(3):
    session.like_by_feed(amount=10, randomize=True, unfollow=False, interact=False)
    session.like_by_tags(etiquetas, amount=50)
    session.follow_user_followers(accounts,
                                randomize=False, interact=True)

    """ First step of Unfollow action - Unfollow not follower users..."""

    session.unfollow_users(amount=500, instapy_followed_enabled=True, 
                            instapy_followed_param="nonfollowers",
                            style="FIFO",
                            unfollow_after=1, sleep_delay=601)
    time.sleep(60)
session.end()
