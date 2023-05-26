def get_data(symbols, dates, addSPY=True, colname="Adj Close"):  		  	   		  		 			  		 			 	 	 		 		 	
    """Read stock data (adjusted close) for given symbols from CSV files."""  		  	   		  		 			  		 			 	 	 		 		 	
    df = pd.DataFrame(index=dates)  		  	   		  		 			  		 			 	 	 		 		 	
    if addSPY and "SPY" not in symbols:  # add SPY for reference, if absent  		  	   		  		 			  		 			 	 	 		 		 	
        symbols = ["SPY"] + list(  		  	   		  		 			  		 			 	 	 		 		 	
            symbols  		  	   		  		 			  		 			 	 	 		 		 	
        )  # handles the case where symbols is np array of 'object'  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    for symbol in symbols:  		  	   		  		 			  		 			 	 	 		 		 	
        df_temp = pd.read_csv(  		  	   		  		 			  		 			 	 	 		 		 	
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
  		  	   		  		 			  		 			 	 	 		 		 	
    """Plot stock prices with a custom title and meaningful axis labels."""  		  	   		  		 			  		 			 	 	 		 		 	
    ax = df.plot(title=title, fontsize=12)  		  	   		  		 			  		 			 	 	 		 		 	
    ax.set_xlabel(xlabel)  		  	   		  		 			  		 			 	 	 		 		 	
    ax.set_ylabel(ylabel)  		  	   		  		 			  		 			 	 	 		 		 	
    plt.show()  		  	 