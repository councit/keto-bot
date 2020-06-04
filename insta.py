from instapy import InstaPy

session = InstaPy(username='ketocouncil', password='rip19133', want_check_browser=False)
session.login()
session.like_by_tags(['keto'], amount=5)

session.end()