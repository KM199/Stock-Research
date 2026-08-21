---
title: Apple Inc. (AAPL)
layout: stock
---

## Real-Time Stock Data

<script>
function initializeStockData() {
    const symbol = 'AAPL'; // Change this to the stock symbol you want

    async function fetchStockData() {
        try {
            const response = await fetch(`http://localhost:3000/stock/price/${symbol}`);
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            const data = await response.json();
            updateStockData(data);
        } catch (error) {
            console.error('Error fetching stock data:', error);
        }
    }

    function updateStockData(data) {
        // Update the title with the current price
        const articleTitle = document.querySelector('.article-title');
        articleTitle.textContent = `Apple Inc. (AAPL) - $${data.price}`;
    }

    fetchStockData();
}

// Run the function directly when the page loads
initializeStockData();

// Use MutationObserver to detect when navigating to this page
const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
        if (mutation.type === 'childList') {
            if (document.querySelector('.article-title')) {
                initializeStockData();
                observer.disconnect();
                break;
            }
        }
    }
});

observer.observe(document.body, { childList: true, subtree: true });
</script>
