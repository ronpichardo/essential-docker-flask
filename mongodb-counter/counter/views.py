from flask import Blueprint

from counter.models import Counter

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
  counter = Counter.objects.all().first()
  if counter:
    counter.count += 1
    counter.save()
  else:
    counter = Counter()
    counter.counte = 1
    counter.save()

  return '<h2>Counter: ' + str(counter.count) + '</h2>'