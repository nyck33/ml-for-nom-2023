"""MLT: Utility code.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Copyright 2017, Georgia Tech Research Corporation  		  	   		  		 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332-0415  		  	   		  		 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import os  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import pandas as pd  	
import dask.dataframe as dd
import dask
	  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  	
               
#pathToCsvs = "/mnt/d/fintech/ml4t/ML4T_2023Sum/data"
pathToCsvs = "mnt/d/fintech/ml4t/ML4T_2023Sum/data"
	 			  		 			 	 	 		 		 	  		  	   		  		 			  		 			 	 	 		 		 	
	 			  		 			 	 	 		 		 	  		  	   		  		 			  		 			 	 	 		 		 	
def symbol_to_path(symbol, base_dir=None):  		  	   		  		 			  		 			 	 	 		 		 	
    """Return CSV file path given ticker symbol."""  		  	   		  		 			  		 			 	 	 		 		 	
    if base_dir is None:  		  	   		  		 			  		 			 	 	 		 		 	
        base_dir = os.environ.get("MARKET_DATA_DIR", pathToCsvs) # "../data/")  		  	   		  		 			  		 			 	 	 		 		 	
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def get_data(symbols, dates, addSPY=True, colname="Adj Close"):  		  	   		  		 			  		 			 	 	 		 		 	
    """Read stock data (adjusted close) for given symbols from CSV files."""  		  	   		  		 			  		 			 	 	 		 		 	
    df = dd.DataFrame()
      		  	   		  		 			  		 			 	 	 		 		 	
    if addSPY and "SPY" not in symbols:  # add SPY for reference, if absent  		  	   		  		 			  		 			 	 	 		 		 	
        symbols = ["SPY"] + list(  		  	   		  		 			  		 			 	 	 		 		 	
            symbols  		  	   		  		 			  		 			 	 	 		 		 	
        )  # handles the case where symbols is np array of 'object'  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    for symbol in symbols:  		  	   		  		 			  		 			 	 	 		 		 	
        df_temp = dd.read_csv(  		  	   		  		 			  		 			 	 	 		 		 	
            symbol_to_path(symbol),  		  	   		  		 			  		 			 	 	 		 		 	
            index_col="Date",  		  	   		  		 			  		 			 	 	 		 		 	
            parse_dates=True,  		  	   		  		 			  		 			 	 	 		 		 	
            usecols=["Date", colname],  		  	   		  		 			  		 			 	 	 		 		 	
            na_values=["nan"],  		  	   		  		 			  		 			 	 	 		 		 	
        )  		  	   		  		 			  		 			 	 	 		 		 	
        df_temp = df_temp.rename(columns={colname: symbol})  		  	   		  		 			  		 			 	 	 		 		 	
        df = df.join(df_temp)  		  	   		  		 			  		 			 	 	 		 		 	
        if symbol == "SPY":  # drop dates SPY did not trade  		  	   		  		 			  		 			 	 	 		 		 	
            df = df.dropna(subset=["SPY"])  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    return df  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):  		  	   		  		 			  		 			 	 	 		 		 	
    import matplotlib.pyplot as plt

    df.drop('Date', axis=1, inplace=True) # drop date column
  		  	   		  		 			  		 			 	 	 		 		 	
    """Plot stock prices with a custom title and meaningful axis labels."""  		  	   		  		 			  		 			 	 	 		 		 	
    ax = df.plot(title=title, fontsize=12)  		  	   		  		 			  		 			 	 	 		 		 	
    ax.set_xlabel(xlabel)  		  	   		  		 			  		 			 	 	 		 		 	
    ax.set_ylabel(ylabel)

    ax.legend(title='Daily Prices Comparison')
    plt.show()  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
