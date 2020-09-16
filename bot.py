from instapy import InstaPy

session = InstaPy(username="", password="")
session.login()

session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(
    ["Buenisimo!", "Me encantaaa!", "Que buenooo :heart_eyes:"])
session.like_by_tags(["3dprint", "impresion3d"], amount=5)

session.end()
