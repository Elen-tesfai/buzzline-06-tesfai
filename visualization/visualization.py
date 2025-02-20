import matplotlib.pyplot as plt 
import numpy as np

# Sample Data (Feel free to replace this with your actual data from Kafka)
categories = ['Health', 'Technology', 'Sports', 'Entertainment', 'Education', 'Business', 'Science']
sentiment_scores = [0.75, 0.60, 0.80, 0.65, 0.70, 0.90, 0.85]  # Example sentiment scores (Blue Bars)
message_lengths = [120, 140, 110, 130, 150, 160, 145]  # Example message lengths (Green Bars)

# Pie chart data (replace with your actual sentiment data)
sentiment_dist = {'Positive': 45, 'Neutral': 40, 'Negative': 15}

# Scaling factor to increase the length of sentiment scores for better visibility
scale_factor = 300  # Increased the scaling factor for better visibility
scaled_sentiment_scores = [score * scale_factor for score in sentiment_scores]

# Create the Bar and Line Chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar Chart for sentiment scores and message lengths
bar_width = 0.35  # Adjusting width to make bars more distinct
index = np.arange(len(categories))

bar1 = ax1.bar(index, scaled_sentiment_scores, bar_width, label='Sentiment Score (Blue)', color='blue')
bar2 = ax1.bar(index + bar_width, message_lengths, bar_width, label='Message Length (Green)', color='green')

ax1.set_xlabel('Categories')
ax1.set_ylabel('Average Values')
ax1.set_title('Average Sentiment Score and Message Length by Category')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(categories, rotation=45)
ax1.legend(loc='upper left')

# Adjust y-axis to accommodate sentiment scores and message lengths
ax1.set_ylim(0, max(scaled_sentiment_scores) + 50)  # Increase y-axis limit to make room for sentiment scores

# Line Chart for sentiment scores and message lengths
ax2 = ax1.twinx()  # Create a second y-axis sharing the same x-axis

# Plot both lines, keeping both the blue and green lines
ax2.plot(categories, sentiment_scores, label='Sentiment Score (Line)', color='blue', marker='o', linewidth=2, markersize=8)
ax2.plot(categories, message_lengths, label='Message Length (Line)', color='green', marker='x', linewidth=2, markersize=8)

# Adjusting the line chart's y-axis to make it appear above the bars
ax2.set_ylabel('Values (Line Chart)')
ax2.set_ylim(0, max(message_lengths) + 50)  # Ensure Message Length line is above the bars
ax2.legend(loc='upper right')

# Save the bar/line chart as PNG
plt.tight_layout()
plt.savefig('C:/Users/su_te/buzzline-06-tesfai/images/sentiment_bar_line_chart.png')  # Save to folder

# Pie chart for sentiment distribution with Blue for Neutral
fig2, ax3 = plt.subplots(figsize=(7, 7))
ax3.pie(sentiment_dist.values(), labels=sentiment_dist.keys(), autopct='%1.1f%%', startangle=90,
        colors=['green', 'blue', 'red'])  # Changed Neutral to Blue
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.set_title('Sentiment Distribution')

# Save the pie chart as PNG
fig2.tight_layout()
fig2.savefig('C:/Users/su_te/buzzline-06-tesfai/images/sentiment_pie_chart.png')  # Save pie chart to folder

# Add table with descriptions for bar, line, and pie charts
table_data = [
    ['Sentiment Score (Blue)', 'Bar Chart: Average Sentiment Score'],
    ['Message Length (Green)', 'Bar Chart: Average Message Length'],
    ['Sentiment Score (Blue)', 'Line Chart: Sentiment Score by Category'],
    ['Message Length (Green)', 'Line Chart: Message Length by Category'],
    ['Sentiment Distribution (Pie)', 'Pie Chart: Distribution of Sentiment (Positive, Neutral, Negative)']
]
columns = ['Description', 'Chart Type']

# Create a table outside the plot to describe bar, line, and pie chart info
plt.figure(figsize=(10, 2))  # Small figure to hold the table
plt.table(cellText=table_data, colLabels=columns, loc='center', cellLoc='center')
plt.axis('off')  # Hide axes for the table plot

# Save the table as PNG
plt.tight_layout()
plt.savefig('C:/Users/su_te/buzzline-06-tesfai/images/sentiment_table.png')  # Save table to folder

# Show the plots
plt.show()