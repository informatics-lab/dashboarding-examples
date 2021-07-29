# Custom JavaScript Examples

An example of producing a simple webpage that uses custom JavaScript to create a dashboard.

## Overview

This example application is composed of two parts: a webpage frontend that displays a spirograph plot and a Python (webserver) backend that calculates the values for the plot.

The webpage is a simple html page, with CSS for styling and JavaScript for interacting with the Python server, and producing the spirograph plot. The JavaScript code makes use of the [JQuery](https://jquery.com/) library to simplify interactions with the webpage and making the POST request to the Python server.

The Python server uses [tornado](https://www.tornadoweb.org/en/stable/index.html) to stand up a simple web server to handle POST requests from the JavaScript code. The body of the POST request contains a JSONisable string of key-value pairs for four values used to calculate the spirograph plot. The server calculates the `(x, y)` points for the spirograph plot from the input values, and these are returned in JSON form in the body of the response from the POST request.

### The flow of a request

The JavaScript code on the website makes a POST request to the Python server, supplying input values for calculating the points for the spirograph plot. These points are passed back to the JavaScript code as the POST response body, and are plotted by the JavaScript in the html `canvas` element on the webpage.

## Usage

The whole application (web frontend and Python backend) is served from the Python tornado webserver. To run this you will need a Python environment containing `tornado` and `NumPy`. For example:

```bash
conda install -c conda-forge tornado numpy
```

To run the webserver and serve the application:

```
python backend.py
```

This will run the Python server at `http://localhost:8000`.

The endpoint for the Python backend that calculates the points for the plot is at `http://localhost:8000/plot`. This is referenced in the JavaScript code.