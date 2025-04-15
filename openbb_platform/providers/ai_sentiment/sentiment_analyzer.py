"""AI-powered sentiment analyzer for financial markets."""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

import numpy as np
import pandas as pd
from openbb_platform.core.openbb_core.provider.abstract.data import Data

from openbb_platform.providers.ai_sentiment.models import (
    NewsItem,
    SentimentAnalysisResponse,
    SentimentTrend,
    SentimentType,
)

logger = logging.getLogger(__name__)


class SentimentAnalyzer(Data):
    """AI-powered sentiment analyzer for financial market news and social media."""

    def get_sentiment(
        self,
        symbol: str,
        start_date: Optional[Union[str, datetime]] = None,
        end_date: Optional[Union[str, datetime]] = None,
        source: str = "all",
    ) -> SentimentAnalysisResponse:
        """
        Get sentiment analysis for a specific symbol.

        Parameters
        ----------
        symbol : str
            Stock symbol or asset identifier
        start_date : Optional[Union[str, datetime]], optional
            Start date for analysis, by default 7 days ago
        end_date : Optional[Union[str, datetime]], optional
            End date for analysis, by default current date
        source : str, optional
            Source of data to analyze ('news', 'social', 'all'), by default 'all'

        Returns
        -------
        SentimentAnalysisResponse
            Sentiment analysis results

        Examples
        --------
        >>> from openbb_platform.providers.ai_sentiment import SentimentAnalyzer
        >>> analyzer = SentimentAnalyzer()
        >>> sentiment = analyzer.get_sentiment("AAPL")
        >>> print(sentiment.overall_sentiment_type)
        SentimentType.POSITIVE
        """
        # Set default dates if not provided
        if not end_date:
            end_date = datetime.now()
        elif isinstance(end_date, str):
            end_date = pd.to_datetime(end_date)

        if not start_date:
            start_date = end_date - timedelta(days=7)
        elif isinstance(start_date, str):
            start_date = pd.to_datetime(start_date)

        # In a real implementation, this would fetch data from news APIs and social media
        # For this example, we'll simulate the result
        
        # Simulate fetching news data
        mock_news_items = [
            NewsItem(
                source="Financial Times",
                title=f"Market analysis for {symbol} shows promising trends",
                url=f"https://example.com/news/{symbol.lower()}/1",
                published_at=datetime.now() - timedelta(days=1),
                sentiment_score=0.78,
                sentiment_type=SentimentType.POSITIVE,
            ),
            NewsItem(
                source="Market Watch",
                title=f"{symbol} quarterly results exceed expectations",
                url=f"https://example.com/news/{symbol.lower()}/2",
                published_at=datetime.now() - timedelta(days=2),
                sentiment_score=0.65,
                sentiment_type=SentimentType.POSITIVE,
            ),
            NewsItem(
                source="Bloomberg",
                title=f"Analysts remain neutral on {symbol} outlook",
                url=f"https://example.com/news/{symbol.lower()}/3",
                published_at=datetime.now() - timedelta(days=3),
                sentiment_score=0.05,
                sentiment_type=SentimentType.NEUTRAL,
            ),
        ]
        
        # Calculate overall sentiment
        sentiment_scores = [item.sentiment_score for item in mock_news_items]
        overall_score = np.mean(sentiment_scores)
        
        # Determine sentiment type
        if overall_score > 0.3:
            overall_type = SentimentType.POSITIVE
        elif overall_score < -0.3:
            overall_type = SentimentType.NEGATIVE
        else:
            overall_type = SentimentType.NEUTRAL
            
        # Determine trend (this would normally be calculated from historical data)
        trend = SentimentTrend.IMPROVING
        
        return SentimentAnalysisResponse(
            symbol=symbol,
            timestamp=datetime.now(),
            overall_sentiment_score=overall_score,
            overall_sentiment_type=overall_type,
            sentiment_trend=trend,
            news_items=mock_news_items,
            social_media_sentiment=0.45 if source in ["social", "all"] else None,
            average_confidence=0.85,
        )
    
    def get_market_sentiment(
        self, 
        symbols: List[str],
        sector: Optional[str] = None,
    ) -> Dict[str, SentimentAnalysisResponse]:
        """
        Get sentiment analysis for multiple symbols or a sector.

        Parameters
        ----------
        symbols : List[str]
            List of stock symbols
        sector : Optional[str], optional
            Sector to analyze, by default None

        Returns
        -------
        Dict[str, SentimentAnalysisResponse]
            Dictionary of sentiment analysis results by symbol

        Examples
        --------
        >>> from openbb_platform.providers.ai_sentiment import SentimentAnalyzer
        >>> analyzer = SentimentAnalyzer()
        >>> sentiment_dict = analyzer.get_market_sentiment(["AAPL", "MSFT", "GOOGL"])
        >>> print(sentiment_dict["AAPL"].overall_sentiment_type)
        SentimentType.POSITIVE
        """
        result = {}
        for symbol in symbols:
            result[symbol] = self.get_sentiment(symbol)
        
        return result
