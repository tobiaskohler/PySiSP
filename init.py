import yfinance as yf
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import os


def create_graph(symbol, start, end, price_type):

    stock = yf.Ticker(symbol)
    df = stock.history(start=start, end=end)

    fig = make_subplots(rows=2, cols=1, subplot_titles=(f'{price_type}', "Volume"))

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df[price_type],
        name=price_type,
        line_color='#1e38af', 
        line_width=1
    ), row=1, col=1)

    fig.append_trace(go.Bar(
        x=df.index,
        y=df['Volume'],
        name="Volume",
        marker=dict(color='black')
    ), row=2, col=1)


    fig.update_layout(height=600, width=600, template="plotly_white", hovermode="x unified", title_text=f'{symbol}<br>({start}/{end})', title_x=0.5)

    fig.show()

    save = input("Save graph to the current folder? (y/n)")

    if save.lower() == 'y':
        
        folder_name = "output"
        save_dir = os.path.isdir(folder_name)
        current_dir = os.getcwd()

        if not save_dir:
            os.makedirs(folder_name)
            
        pio.write_image(fig, f"{current_dir}/{folder_name}/{symbol}_{price_type}_{start}-{end}.png")
        fig.write_html(f"{current_dir}/{folder_name}/{symbol}_{price_type}_{start}-{end}.html")
        print(f"Image saved to {current_dir}/{folder_name}.")
        
    else:
        print("Image not saved.")


if __name__ == '__main__':
    
    
    ##############################################
    # Input
    symbol = 'AAPL'
    start = '2022-01-01'
    end = '2022-12-31'
    price_type = 'Close' #Open, High, Low, Close
    ##############################################
    
    create_graph(symbol, start, end, price_type)