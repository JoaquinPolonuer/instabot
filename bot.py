from instapy import InstaPy

session = InstaPy(username="", password="")
session.login()
a = session.like_by_tags(["3dprint", "impresion3d"], amount=5)
print(a)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
