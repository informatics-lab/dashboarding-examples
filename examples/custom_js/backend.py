import numpy as np

from tornado.escape import json_decode
import tornado.ioloop
import tornado.web


class SpirographHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        """
        If running both server and client locally, you need to enable CORS requests.
        See https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin.

        Code from: https://stackoverflow.com/a/35259440/6676985.

        """
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST')

    def post(self):
        """
        Handle a POST request.

        This should come with a request body containing a JSON-isable string
        of arguments, one with a value for `n` and one with a value for `m`.

        """
        self.args = json_decode(self.request.body)
        print(f"Decoded args: {self.args}")
        plot_dict = self.spirograph()
        self.write(plot_dict)
        self.flush()

    def spirograph(self):
        """Make x and y values for a spirograph plot."""
        n = self.args["n"]
        m = self.args["m"]
        rnx = rny = self.args["rn"]
        rmx = rmy = self.args["rm"]
        kn = km = 1

        t_ring = np.linspace(0, 2*np.pi, n*m)
        t_circle = np.linspace(0, 2*np.pi, m)
        
        x_ring = rnx * np.sin(t_ring*kn).reshape(n, m)
        y_ring = rny * np.cos(t_ring*kn).reshape(n, m)
        xp = rmx * np.sin(t_circle*km) + x_ring
        yp = rmy * np.cos(t_circle*km) + y_ring

        return {"x": list(xp.reshape(-1)), "y": list(yp.reshape(-1))}


def make_app():
    """
    Make a tornado web application to run as a web server.
    
    This links routes in your web application to handlers that
    process requests arriving from web clients. These we can expect
    to be HTTP verb requests (most commonly GET or POST).

    """
    return tornado.web.Application([
        (r"/plot", SpirographHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
