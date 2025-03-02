int maxProfit(int* prices, int pricesSize) {
    int temp, min_price, profit;

    if (!prices || !pricesSize)
        return 0;
    profit = 0;
    min_price = prices[0];
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < min_price) {
            min_price = prices[i];
        } else {
            temp = prices[i] - min_price;
            if (temp > profit)
                profit = temp;
        }
    }
    return profit;
}
