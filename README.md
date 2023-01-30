# PySiSP - Python's Simple Stock Plotter

This script generates a graph of the specified stock symbol using data from the [Yahoo Finance API](https://finance.yahoo.com/). The graph includes a line plot of the `price_type` and a bar plot of the volume of the stock over the specified `start` and `end` dates.

## Example
![Example output (.png and .html available)](/AAPL_Close_2022-01-01-2022-12-31.png)

## Requirements

- yfinance
- plotly

## Usage

To use the script, specify the following input parameters:
- `symbol`: Ticker symbol of the stock to graph
- `start`: Start date for the graph in the format `YYYY-MM-DD`
- `end`: End date for the graph in the format `YYYY-MM-DD`
- `price_type`: Type of stock price to plot (`Open`, `High`, `Low`, `Close`)

## Output

The script generates a graph in an interactive Plotly format. The user can choose to save the graph as a PNG and HTML file in the `output` folder. The file names will be in the format `[symbol]_[price_type]_[start]-[end]`.
