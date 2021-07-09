# bokeh Examples

Example code for creating a simple dashboard with [bokeh](https://bokeh.org/).

## Overview

This is an example of embedding a bokeh plot (a 'bokeh document') in a templated html file. To see this in action, run the code provided below. More information on this can be found [in the bokeh docs](https://docs.bokeh.org/en/latest/docs/user_guide/embed.html#standard-template).

## Usage

To run this example:

```bash
$ bokeh serve . --show
```

Alternatively, the Python file can be served in a standalone fashion without the html document. You will notice the extra html elements added by the templated html file are missing in this case, and only the plot is served:

```bash
$ bokeh serve main.py --show
```

## Python Environment

To run this demo you will need a Python environment containing `bokeh` and `NumPy`. For example:

```bash
conda install -c conda-forge bokeh numpy
```