# 911 Call Sentinel

## Overview
**911 Call Sentinel** is a system designed to enhance emergency call analytics by distinguishing between genuine and prank calls, ultimately optimizing resource allocation and response times. This project delves into the intricate dynamics of 911 emergency call recordings, offering insights that go beyond mere words.

---

## Features
1. **Audio Trimming**: Standardizes call durations for uniform analysis.
2. **Audio Enhancement**: Separates vocals using Spleeter for focused analyses.
3. **Feature Extraction**: Derives acoustic features like MFCC, spectral properties, and polynomial representations for classification.
4. **Data Cleaning & Labeling**: Cleans metadata and labels calls using regex for pattern-based classification.
5. **Correlation Analysis**: Explores feature relationships using heatmaps and statistical measures.
6. **Anomaly Detection**: Identifies suspicious patterns using Isolation Forests.
7. **Keyword Extraction & Sentiment Analysis**:
   - Uses Latent Dirichlet Allocation (LDA) for topic modeling.
   - Applies VADER for sentiment scoring.

---

## Dataset
- **Audio Data**: 700 call recordings, each 42-45 minutes long.
- **Metadata**: Details like state, potential deaths, call titles, and descriptions.

---

## Libraries and Tools
- **Audio Processing**: PyDub, Spleeter
- **Feature Extraction**: Librosa
- **Data Cleaning**: regex
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: scikit-learn (LDA, Isolation Forests)
- **Sentiment Analysis**: NLTK (VADER)

---

## Approach
### 1. Audio Processing
- Trimmed audio to 2 minutes.
- Enhanced audio by isolating vocal tracks.

### 2. Data Handling
- Cleaned metadata using imputation techniques.
- Labeled calls based on patterns in metadata.

### 3. Analysis
- Explored correlations and anomalies in data.
- Extracted keywords and performed sentiment analysis.

### 4. Classification
- Differentiated genuine and prank calls using extracted features.

---

## Future Scope
1. **Real-time Streaming Integration**: Apply the system to live 911 call streams.
2. **Speaker Diarization**: Separate and analyze individual speakers in calls.
3. **Healthcare Applications**: Extend to mental health monitoring and diagnostics.

---

## Conclusion
By tackling the issue of fraudulent emergency calls, **911 Call Sentinel** enhances public safety, optimizes emergency resource allocation, and provides actionable insights for decision-makers. This project not only aims to save lives but also instills greater trust in emergency services.

---

## Acknowledgements
Project by:
- **Dhwani Bhavankar**  
- **Deeksha Mandal** 


---
