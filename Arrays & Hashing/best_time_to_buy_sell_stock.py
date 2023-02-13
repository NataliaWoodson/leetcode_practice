def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Time complexity: O(n)
        # Space complexity: O(1)
        max_p = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_p = max(max_p, prices[i] - min_price)

        return max_p