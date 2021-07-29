# Custom JavaScript Examples

An example of producing a simple webpage that uses custom JavaScript to create a dashboard.

## Overview

This example is composed of two parts: a webpage frontend that displays a plot and a Python server backend that calculates the values for a spirograph plot.

The webpage is a simple html page, with CSS for styling and JavaScript for interacting with the Python server, and producing the spirograph plot. The JavaScript code makes use of the [JQuery](https://jquery.com/) library to simplify interactions with the webpage and making the POST request to the Python server.

The Python server uses [tornado](https://www.tornadoweb.org/en/stable/index.html) to stand up a simple web server to handle POST requests from the JavaScript code. The body of the POST request contains a JSONisable string of key-value pairs for four values used to calculate the spirograph plot. The server calculates the `(x, y)` points for the spirograph plot from the input values, and these are returned in JSON form in the body of the response from the POST request.

### The flow of a request

The JavaScript code on the website makes a POST request to the Python server, supplying input values for calculating the points for the spirograph plot. These points are passed back to the JavaScript code as the POST response body, and are plotted by the JavaScript in the html `canvas` element on the webpage.

## Usage

### Python server

To run the Python server part of this demo you will need a Python environment containing `tornado` and `NumPy`. For example:

```bash
conda install -c conda-forge tornado numpy
```

To run the server:

```
python backend.py
```

This will run the Python server at `http://localhost:8000/plot`, which is referenced in the JavaScript code.

### (Optional) Web frontend

The example runs best if you _also_ serve the webpage frontend using a simple http server such as the [http-server](https://www.npmjs.com/package/http-server) node package (see link for install instructions, which assume you have already installed [NPM](https://www.npmjs.com/); the Node Package Manager).

For example:

```bash
npx http-server --cors="*" .
```

You can then navigate to the web frontend at `http://localhost:8080`.

Note the `--cors="*"` flag when running the http server. For security reasons the JavaScript code is blocked from accessing other resources on other servers (we have one for the frontend and one for the backend) on the same host (`localhost`). For more information see this Mozilla developer page on [HTTP Access Control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin).