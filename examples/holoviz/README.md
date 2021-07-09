# HoloViz Examples

Example code for creating a simple dashboard with [HoloViz](https://holoviz.org/) tools; specifically [HoloViews](https://holoviews.org/) for creating a line plot and [Panel](https://panel.holoviz.org/) for converting the line plot into an interactive dashboard.

## Overview

This is an example of creating a simple plot with Holoviews and making it interactive and served as a dashboard using Panel. Two panel sliders are created to make interactive inputs to control the plot. The dashboard is composed of the plot and the sliders combined into a layout, which is marked as `servable` to indicate that Panel should serve it using the code below.

## Usage

To run this example:

```bash
$ panel serve holoviz_spirograph.ipynb --show
```

## Python Environment

To run this demo you will need a Python environment containing `HoloViews`, `Panel` and `NumPy`. For example:

```bash
conda install -c conda-forge numpy holoviews panel
```