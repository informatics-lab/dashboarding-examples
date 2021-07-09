# Plotly & Dash Examples

Example code for creating a simple dashboard with [Plotly](https://plotly.com/) and [Dash](https://plotly.com/dash/).

## Overview

Dash creates an app that is served by dash server. The app is made up of an html layout, with elements added as html tags. The order the tags are defined in sets the order they are displayed within the app. The app is made up of a `Graph` and two `Slider`s, with a callback registered on the app that links the values in the sliders to the plot that is drawn.

## Usage

To run this example:

```bash
$ python dash_spirograph.py
```

## Python Environment

To run this demo you will need a Python environment containing `Dash`, `Plotly` and `NumPy`. Dash and Plotly will both be installed by installing dash. You can also install dash with extra `jupyter` support. For example:

```bash
pip install numpy jupyter-dash
```