import webapp2
import cgi
import codecs
from google.appengine.ext.webapp.util import run_wsgi_app

form="""
<form method="post" action="/">
Enter some test to ROT13:
<br>

<textarea name="text" cols="80" rows="20">
%s
</textarea>

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
        t_val = self.request.get("text")
        t_rot = self.rot13(t_val)
        t_san = self.sanitize(t_rot)
        self.response.out.write(self.getForm(t_san))

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
