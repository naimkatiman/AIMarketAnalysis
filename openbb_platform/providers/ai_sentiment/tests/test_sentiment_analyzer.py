"""Tests for the AI Sentiment Analyzer provider."""

import pytest
from datetime import datetime, timedelta

from openbb_platform.providers.ai_sentiment.models import SentimentType, SentimentTrend
from openbb_platform.providers.ai_sentiment.sentiment_analyzer import SentimentAnalyzer


class TestSentimentAnalyzer:
    """Tests for the SentimentAnalyzer class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.analyzer = SentimentAnalyzer()

    def test_get_sentiment_returns_valid_response(self):
        """Test that get_sentiment returns a valid response structure."""
        response = self.analyzer.get_sentiment("AAPL")
        
        # Check response structure
        assert response.symbol == "AAPL"
        assert isinstance(response.timestamp, datetime)
        assert isinstance(response.overall_sentiment_score, float)
        assert response.overall_sentiment_score >= -1.0 and response.overall_sentiment_score <= 1.0
        assert isinstance(response.overall_sentiment_type, SentimentType)
        assert isinstance(response.sentiment_trend, SentimentTrend)
        assert len(response.news_items) > 0
        assert isinstance(response.average_confidence, float)
        
    def test_get_sentiment_with_date_range(self):
        """Test get_sentiment with specified date range."""
        start_date = datetime.now() - timedelta(days=10)
        end_date = datetime.now() - timedelta(days=2)
        
        response = self.analyzer.get_sentiment(
            symbol="MSFT",
            start_date=start_date,
            end_date=end_date
        )
        
        assert response.symbol == "MSFT"
        # In a real test, we would verify that the data falls within the specified range
        
    def test_get_market_sentiment_returns_dict(self):
        """Test that get_market_sentiment returns a dictionary of results."""
        symbols = ["AAPL", "MSFT", "GOOGL"]
        results = self.analyzer.get_market_sentiment(symbols)
        
        assert isinstance(results, dict)
        assert len(results) == len(symbols)
        
        for symbol in symbols:
            assert symbol in results
            assert results[symbol].symbol == symbol
