"""Models for AI Sentiment Analysis Provider."""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class SentimentType(str, Enum):
    """Sentiment type enumeration."""

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class SentimentTrend(str, Enum):
    """Sentiment trend enumeration."""

    IMPROVING = "improving"
    STABLE = "stable"
    DECLINING = "declining"


class NewsItem(BaseModel):
    """News item model with sentiment score."""

    source: str = Field(..., description="Source of the news")
    title: str = Field(..., description="News title")
    url: str = Field(..., description="URL to the news article")
    published_at: datetime = Field(..., description="Publication timestamp")
    sentiment_score: float = Field(..., description="Sentiment score between -1.0 and 1.0")
    sentiment_type: SentimentType = Field(..., description="Sentiment type classification")


class SentimentAnalysisResponse(BaseModel):
    """Response model for sentiment analysis."""

    symbol: str = Field(..., description="Stock symbol or asset identifier")
    timestamp: datetime = Field(..., description="Timestamp of the analysis")
    overall_sentiment_score: float = Field(..., description="Overall sentiment score between -1.0 and 1.0")
    overall_sentiment_type: SentimentType = Field(..., description="Overall sentiment type")
    sentiment_trend: SentimentTrend = Field(..., description="Sentiment trend over time")
    news_items: List[NewsItem] = Field(..., description="List of analyzed news items")
    social_media_sentiment: Optional[float] = Field(None, description="Social media sentiment score")
    average_confidence: float = Field(..., description="Average confidence of sentiment predictions")
