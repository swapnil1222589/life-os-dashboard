# 🧠 Life-OS Dashboard   

> **Measure your habits. Understand your patterns. Improve your day.**

Life-OS Dashboard is a **Python + Streamlit digital wellbeing dashboard** that transforms screen-time data into useful personal insights.

The project analyzes application usage, tracks daily screen-time goals, visualizes usage trends, breaks usage down by category, and provides a foundation for **Gemini-powered AI lifestyle coaching**.    
 
---    

## 🚀 Overview

Digital habits can be difficult to understand when usage data is scattered across different applications and devices.

Life-OS Dashboard provides a simple interface for analyzing this data in one place.  

The application currently supports:
                                                     
* 📊 Screen-time analytics
* 🎯 Daily usage goals
* 📈 14-day usage trends
* 📱 Most-used application detection
* 🗂️ Category-wise usage analysis
* 🤖 AI coaching integration foundation
* 🧑‍💻 Dynamic avatar generation
* 📋 CSV-based data processing

---

## ✨ Features

### 📊 Screen-Time Analytics

Analyze application usage using a CSV dataset containing:

* Date
* Application name
* Category
* Minutes used
   
---

### 🎯 Daily Screen-Time Goal

Set a personal daily screen-time target using an interactive slider.

The dashboard compares your actual usage with your selected goal.

```text
Daily Goal
    ↓
Actual Screen Time
    ↓
Goal Difference
    ↓
Personal Insight
```

---

### 📱 Most-Used App

The dashboard automatically identifies the application with the highest usage for the selected date.

Example:

```text
Most Used App
      ↓
VS Code
      ↓
180 minutes
```

---

### 📈 14-Day Usage Trend

Visualize how screen time changes across the available 14-day dataset.

This makes it easier to identify:

* Increasing usage
* Decreasing usage
* High-usage days
* Consistent usage patterns

---

### 🗂️ Category Breakdown

Screen time is grouped into categories such as:

* Social Media
* Coding
* Education
* Entertainment

This provides a clearer view of **where your digital time is going**.                    
 
---

### 🤖 AI Life Coach

The project includes a Gemini-ready AI coaching architecture.

The intended AI system can analyze screen-time summaries and generate:

* Productivity score
* Positive habits
* Negative habits
* Actionable recommendations
* Motivational guidance

Example workflow:

```text
Screen-Time Data
       ↓
Data Analysis
       ↓
Category Summary
       ↓
AI Prompt
       ↓
Gemini
       ↓
Personalized Coaching
```

> The current application contains the AI prompt/integration foundation; the complete live Gemini coaching workflow can be extended further.

---

### 🧑‍💻 Dynamic Avatar

The project includes an avatar helper that can generate an external image URL from a text prompt.

This can be used to create a personalized visual identity for the AI coach.

---

# 🧠 Application Workflow

```text
                    User Data
                       │
                       ↓
                 screentime.csv
                       │
                       ↓
                  Pandas
                       │
                       ↓
              Data Processing
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      KPI Metrics    Trends     Categories
          │            │            │
          └────────────┼────────────┘
                       ↓
                Daily Summary
                       │
                       ↓
                 AI Coach
                       │
                       ↓
              Personal Insights
```

---

# 🛠️ Tech Stack

| Technology       | Purpose                 |
| ---------------- | ----------------------- |
| 🐍 Python        | Application logic       |
| 🎈 Streamlit     | Interactive dashboard   |
| 🐼 Pandas        | Data processing         |
| 🤖 Google Gemini | AI coaching integration |
| 🔐 python-dotenv | Environment variables   |
| 🌐 Requests      | HTTP/API requests       |

---

# 📂 Project Structure

```text
life-os-dashboard/
│
├── app.py
├── avatar.py
├── prompts.py
├── utils.py
├── screentime.csv
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### `app.py`

Main Streamlit dashboard.

Responsible for:

* Loading data
* Date selection
* Goal selection
* KPI calculations
* Usage analysis
* Charts
* Dashboard UI

### `avatar.py`

Helper for generating an avatar image URL from a text prompt.

### `prompts.py`

Contains the AI life-coach prompt template.

### `utils.py`

Contains reusable data-processing and category-summary functionality.

### `screentime.csv`

Sample screen-time dataset used by the dashboard.

### `requirements.txt`

Contains the Python packages required to run the project.

---

# 📊 Dataset

The included dataset follows this structure:

```csv
Date,App_Name,Category,Minutes_Used
2026-07-15,Instagram,Social Media,90
2026-07-15,VS Code,Coding,180
2026-07-15,Chrome,Education,60
2026-07-15,YouTube,Entertainment,70
```

### Required Columns

| Column         | Description               |
| -------------- | ------------------------- |
| `Date`         | Usage date                |
| `App_Name`     | Application name          |
| `Category`     | Application category      |
| `Minutes_Used` | Usage duration in minutes |

You can replace the sample dataset with your own data while maintaining these column names.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/swapnil1222589/life-os-dashboard.git
```

Navigate into the project:

```bash
cd life-os-dashboard
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### ⚠️ Security

**Never commit your real API key to GitHub.**

Make sure `.env` is included in `.gitignore`.

For production deployments, use the hosting platform's secret/environment-variable system.

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will normally be available at:


```text
http://localhost:8501
```

---

# 🎯 Example Use Case
 
Suppose a student records:

```text
VS Code       → 180 minutes
Instagram     → 90 minutes
YouTube       → 70 minutes
Chrome        → 60 minutes
```

Life-OS can transform that data into:

```text
Total Screen Time
        ↓
400 minutes

Most Used App
        ↓
VS Code

Category Analysis
        ↓
Coding: 180 min
Social: 90 min
Entertainment: 70 min
Education: 60 min

Daily Goal
        ↓
300 minutes

Goal Difference
        ↓
+100 minutes
```

A future Gemini integration can then turn these metrics into personalized recommendations.

---

# 🤖 AI Coach Architecture

The intended AI coaching pipeline is:

```text
              Screen-Time Dataset
                       ↓
                 Pandas Analysis
                       ↓
                Daily Summary
                       ↓
               Prompt Template
                       ↓
                  Gemini API
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
     Productivity   Habits      Suggestions
        Score
          └────────────┼────────────┘
                       ↓
                AI Life Coach
```

---

# 🔮 Future Roadmap

## 🤖 AI Improvements

* [ ] Live Gemini coaching
* [ ] Daily AI reports
* [ ] Weekly AI summaries
* [ ] Habit detection
* [ ] Personalized recommendations
* [ ] Natural-language questions
* [ ] AI productivity plans

---

## 📱 Data Integrations

* [ ] Android Digital Wellbeing import
* [ ] iOS Screen Time import
* [ ] Browser usage tracking
* [ ] Desktop application tracking
* [ ] Calendar integration
* [ ] Wearable/device data

---

## 📊 Analytics

* [ ] Weekly reports
* [ ] Monthly reports
* [ ] App comparison
* [ ] Category trends
* [ ] Goal streaks
* [ ] Productivity trends
* [ ] Usage anomaly detection

---

## 👤 Personalization

* [ ] User accounts
* [ ] Custom goals
* [ ] Personal profiles
* [ ] Coaching preferences
* [ ] Personalized dashboards
* [ ] Notifications
* [ ] Habit streaks

---

# 🏗️ Future Production Architecture

A future production version could use:

```text
                   Web / Mobile UI
                         │
                         ↓
                    API Gateway
                         │
                         ↓
                Application Backend
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Analytics       Gemini         User
       Service         Service        Service
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                      Database
                         │
                         ↓
                Personalized Insights
```

---

# ⚠️ Current Limitations

The current project is a **prototype / learning project**.

Important limitations:

* The included screen-time data is sample data.
* Live device tracking is not currently implemented.
* Gemini coaching requires API integration/configuration.
* AI-generated recommendations should be treated as guidance rather than objective measurements.
* Avatar generation depends on an external image service.
* There is currently no persistent user database.

---

# 🧪 Learning Outcomes

This project demonstrates practical experience with:

* Python
* Streamlit
* Pandas
* CSV data processing
* Data aggregation
* Interactive dashboards
* Data visualization
* Environment variables
* Prompt engineering
* Generative AI integration
* Modular Python development

---

# 🌐 Deployment

The Streamlit application can be deployed using a Streamlit-compatible hosting platform.

Typical deployment process:

```text
GitHub Repository
       ↓
Connect Repository
       ↓
Configure Python Environment
       ↓
Configure Secrets
       ↓
Install requirements.txt
       ↓
Run app.py
       ↓
Live Dashboard
```

For deployment, store your Gemini API key as a **secret**, not directly inside the source code.

---

# 🤝 Contributing

Contributions are welcome!

### Create a feature branch

```bash
git checkout -b feature/your-feature
```

### Make your changes

```bash
git add .
```

### Commit

```bash
git commit -m "feat: add your feature"
```

### Push

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 👨‍💻 Author

## Swapnil Ghuge

B.Tech Computer Science — Data Science

GitHub:
https://github.com/swapnil1222589

Project Repository:
https://github.com/swapnil1222589/life-os-dashboard

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐.

Feedback, ideas, and contributions are welcome.

---

> **Measure your habits. Understand your patterns. Improve your day. 🧠📊**
