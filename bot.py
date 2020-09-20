
from instapy import InstaPy
from instapy import set_workspace
import os

# Setea la carpeta donde guardaremos los registros y la info
set_workspace(os.getcwd())

# crea una sesion
# headless = True es sin abrir el navegador

session = InstaPy(username="yourprints3d", password="megapolo10",headless_browser=True, geckodriver_path='./geckodriver')

# se loguea a instagram
session.login()

# seteamos los parametros que vamos a utilizar
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=50)
session.set_quota_supervisor(
    enabled=True, peak_comments_daily=15, peak_comments_hourly=2, peak_follows_daily=70, peak_follows_hourly=4, peak_likes_daily=300, peak_likes_hourly=20)

session.set_comments(
    ["Buenisimo!", "Me encantaaa!", "Que buenooo :heart_eyes:", "Epico"])
session.set_relationship_bounds(enabled=True,
                                delimit_by_numbers=True,
                                max_followers=5000,
                                min_followers=20,
                                min_following=77)


# comenzamos a usar el bot
session.like_by_feed(amount=10, randomize=True, unfollow=False, interact=False)
session.like_by_tags(["3dprint", "impresion3d"], amount=50)
session.follow_user_followers(['3ntre.detalles', 'instan3d', 'crazynozzlesba'],
                              randomize=False, interact=True)

""" First step of Unfollow action - Unfollow not follower users..."""
session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                       style="FIFO",
                       unfollow_after=60, sleep_delay=601)
#    unfollow_after=12 * 60 * 60, sleep_delay=601)
session.end()
