package lib

import (
	"fmt"
)

func GetCurrentStockPrice(data map[string]interface{}) (float64, error) {
	// Extract the current price of the stock from the response JSON
	quoteSummary, ok := data["quoteSummary"].(map[string]interface{})
	if !ok {
		return 0, fmt.Errorf("could not find quoteSummary in response")
	}

	result, ok := quoteSummary["result"].([]interface{})
	if !ok || len(result) == 0 {
		return 0, fmt.Errorf("could not find result in response")
	}

	priceData, ok := result[0].(map[string]interface{})
	if !ok {
		return 0, fmt.Errorf("could not find price data in response")
	}

	price, ok := priceData["price"].(map[string]interface{})
	if !ok {
		return 0, fmt.Errorf("could not find price in response")
	}
    
	rawPrice, ok := price["regularMarketPrice"].(map[string]interface{})["raw"].(float64)
	if !ok {
		return 0, fmt.Errorf("could not find current price in response")
	}

	return rawPrice, nil
}