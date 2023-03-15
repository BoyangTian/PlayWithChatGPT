package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	stock_utils "github.com/boyangtian/PlayWithChatGPT/StockSelection/lib"
)

func main() {
    // Define the stock symbol to retrieve
	stockSymbol := "AAPL"

	// Build the URL for the stock symbol
	url := fmt.Sprintf("https://query1.finance.yahoo.com/v10/finance/quoteSummary/%s?modules=price", stockSymbol)

	// Make a GET request to the Yahoo Finance API
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	// Parse the response JSON into a struct
	var data map[string]interface{}
	err = json.NewDecoder(resp.Body).Decode(&data)
	if err != nil {
		log.Fatal(err)
	}

	// Extract the current price of the stock from the response struct
	price, err := stock_utils.GetCurrentStockPrice(data)
	if err != nil {
		log.Fatal(err)
	}

	// Print the current price of the stock
	fmt.Printf("Current price of %s: $%.2f\n", stockSymbol, price)
}