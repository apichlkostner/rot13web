import webapp2
import cgi
import codecs
from google.appengine.ext.webapp.util import run_wsgi_app

form="""
<form method="post" action="/">
Enter some test to ROT13:
<br>

<input type="text" name="q" value="%s">

<br>
<input type="submit">
</form>
"""



class MainPage(webapp2.RequestHandler):
    def getForm(self, s=""):
        return form % s
    
    def rot13(self, s):
        return codecs.encode(s, 'rot_13')
    
    def sanitize(self, s):
        return cgi.escape(s, quote = True)
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.getForm())
    
    def post(self):
        q_val = self.request.get("q")
        q_rot = self.rot13(q_val)
        q_san = self.sanitize(q_rot)
        self.response.out.write(self.getForm(q_san))

class TestHandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        if (q=="a"):
            self.response.out.write("Hihi")
        self.response.out.write(q)
        

application = webapp2.WSGIApplication([('/', MainPage), ('/testform', TestHandler)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
