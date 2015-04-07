from datetime import datetime
from google.appengine.api import memcache
from google.appengine.ext import ndb
from random import choice


_LAST_GET_KEY_PREFIX = 'lastget'
_LAST_POST_KEY = 'lastpost'


class Remark(ndb.Model):

  user = ndb.StringProperty(required=True) # ID of the user who sent this.
  text = ndb.StringProperty(required=True) # The text the user entered.

  timestamp = ndb.DateTimeProperty(auto_now_add=True, required=True)


def ReadRemarks(user_id):
  start_time = memcache.get(_MakeLastGetKey(user_id))

  LogLastGet(user_id)

<<<<<<< HEAD
  remark_infos = []
  for remark in Remark.query(
      Remark.timestamp >= start_time).order(Remark.timestamp).fetch():
    user = remark.user
    text = remark.text
    color_range = ['pink', 'black', 'red', 'blue', 'orange', 'purple', 'yellow', 'green']
    color = choice(color_range)  # TODO(pep-students) Make messages appear a random color.
    remark_infos.append((user, text, color))
=======
  # TODO(pep-students) Make messages appear a random color.
  remark_infos = [
      (remark.user, remark.text, 'black')
      for remark
      in Remark.query(
          Remark.timestamp >= start_time).order(Remark.timestamp).fetch()]
>>>>>>> 57282b9619da05a4b5dca3bf35a82c55f8f5acd4
  return remark_infos


def PostRemark(user, text):
  Remark(user=user, text=text).put()


def _MakeLastGetKey(user_id):
  return ';'.join([_LAST_GET_KEY_PREFIX, user_id])


def LogLastGet(user_id):
  memcache.set(_MakeLastGetKey(user_id), datetime.now())
