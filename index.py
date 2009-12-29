from google.appenigne.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Artist(db.Model):
  name = db.StringProperty()

class Root(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    query = db.GqlQuery('SELECT * FROM Artist WHERE name >= :1 AND name < :2',
                        u'front', u'front ')
    for result in query:
      self.response.out.write('Name: %s', result.name)


application = webapp.WSGIApplication(
    [('/', Root)],
    debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
