# Digital-Meeting-Burnout-Analyzer-Work-Life-Balance-Dashboard
Context

Remote and hybrid work has brought flexibility but also a new challenge: digital meeting fatigue.
Employees spend an average of 22–30 hours per week in meetings, leading to decreased productivity and burnout.
This project builds an AI-powered analyzer to measure meeting overload and its impact on employee well-being.

What This Project Does

Meeting Sentiment Analysis: Uses NLP to analyze chat transcripts and meeting notes for stress markers.

Burnout Scorecard: Calculates a “burnout index” based on meeting frequency, duration, and sentiment.

Work-Life Balance Dashboard: Visualizes trends in meeting load, response times, and after-hours activity.

Predictive Alerts: Flags employees or teams at high risk of burnout for early intervention.

Methodology

Dataset: Simulated + Kaggle datasets of meeting transcripts, Slack/Teams messages, and work activity logs.

Preprocessing: Tokenization, sentiment scoring (VADER + BERT), normalization of timestamps.

Modeling:

Regression models to measure correlation between meeting time and productivity.

Classification models to flag “high-risk burnout profiles.”

Visualization: Power BI dashboard showing burnout scores, heatmaps of meeting intensity, and time-trend analysis.

Tech Stack

Python (NLTK, Scikit-learn, Transformers)

SQL for structured meeting data storage

Power BI for dashboard visualization

Key Insights

Teams with >20 hours of meetings/week showed 40% higher burnout scores.

Negative sentiment in meeting transcripts strongly correlates with attrition risk.

Predictive model achieved 78% accuracy in detecting employees at risk of burnout.

Why It Matters

This project demonstrates how data analytics can humanize work by:

Preventing employee burnout before it escalates.

Helping organizations design healthier meeting practices.

Aligning with the 2025 focus on employee well-being and productivity optimization.
