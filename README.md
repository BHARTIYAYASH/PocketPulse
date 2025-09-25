<div align="center">

# 💳 PocketPulse

**AI-Powered Personal Finance Assistant**

*Track income and expenses using natural language, get smart categorization, and view clear analytics instantly.*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-orange.svg)](https://developers.google.com/sheets)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple.svg)](https://ai.google.dev)

</div>

---

## 🌟 Overview

PocketPulse is an intelligent personal finance management application that revolutionizes how you track your money. Instead of complex forms and manual categorization, simply describe your transactions in natural language, and let AI handle the rest.

### 🎯 Key Benefits

- **🤖 Conversational Input**: Describe transactions naturally - "Spent $50 on groceries yesterday"
- **🧠 Smart Categorization**: AI automatically assigns categories and subcategories
- **📊 Rich Analytics**: Comprehensive financial insights with beautiful visualizations
- **☁️ Cloud Storage**: Secure data persistence with Google Sheets integration
- **📱 Mobile Friendly**: Responsive design works perfectly on all devices

---

## ✨ Features

### 🗣️ Natural Language Processing
- **Conversational Transaction Entry**: Input transactions using everyday language
- **Auto-Date Detection**: Automatically extracts dates from conversational text
- **Smart Categorization**: AI-powered category assignment and subcategory mapping
- **Context Awareness**: Understands transaction context for better accuracy

### 💰 Transaction Management
- **Multiple Transaction Types**:
  - 💸 **Expenses**: Regular spending transactions
  - 💵 **Income**: Earnings and revenue
  - ⏳ **To Pay**: Pending payments and bills
  - 📈 **To Receive**: Expected income and receivables

- **Advanced Features**:
  - 🏷️ Hierarchical category system with unlimited subcategories
  - 📝 Detailed notes and descriptions
  - 📅 Flexible date handling with due date tracking
  - 🔄 Transaction state management

### 📈 Analytics & Insights

#### 📊 Dashboard Overview
- **Financial Summary**: Total income, expenses, and net worth
- **Quick Metrics**: Monthly trends and key performance indicators
- **Pending Transactions**: Overview of upcoming payments and receivables

#### 📈 Visual Analytics
- **Monthly Trends**: Income vs expense patterns over time
- **Category Breakdowns**: Visual representation of spending categories
- **Top Sources**: Biggest income sources and expense categories
- **Weekly Patterns**: Understanding your spending habits by day of week

#### 💡 Smart Insights
- **Weekday vs Weekend Analysis**: Compare spending patterns
- **Fixed vs Variable Expenses**: Automatic expense type detection
- **Week-of-Month Trends**: Identify spending cycles
- **Anomaly Detection**: Spot unusual spending patterns

#### 📅 Flexible Reporting
- **All-Time View**: Complete financial history
- **Yearly Reports**: Annual financial summaries
- **Monthly Analysis**: Month-by-month breakdowns
- **Custom Date Ranges**: Analyze any specific time period

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Description |
|-------------|---------|-------------|
| **Python** | 3.8+ | Core runtime environment |
| **Google Account** | - | For Google Sheets integration |
| **Gemini API Key** | - | For AI-powered features |

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BHARTIYAYASH/PocketPulse.git
   cd expense_tracker
   ```

2. **Install Dependencies**
   ```bash
   # Install uv package manager
   pip install uv
   
   # Install project dependencies
   uv sync
   ```

3. **Configure Environment**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_SHEETS_CREDENTIALS=path/to/your/credentials.json
   GOOGLE_SHEET_ID=your_google_sheet_id
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the Application**
   ```bash
   uv run streamlit run Home.py
   ```

---

## ⚙️ Detailed Setup Guide

### Google Cloud Platform Setup

#### Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Note your project ID

#### Step 2: Enable Google Sheets API
1. Navigate to **APIs & Services** > **Library**
2. Search for "Google Sheets API"
3. Click **Enable**

#### Step 3: Create Service Account
1. Go to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **Service Account**
3. Fill in service account details:
   - **Name**: `pocketpulse-service`
   - **Description**: `Service account for PocketPulse app`
4. Click **Create and Continue**
5. Skip role assignment (click **Continue**)
6. Click **Done**

#### Step 4: Generate Credentials
1. Find your service account in the credentials list
2. Click on the service account email
3. Go to **Keys** tab
4. Click **Add Key** > **Create New Key**
5. Select **JSON** format
6. Download and save the JSON file securely

#### Step 5: Set Up Google Sheet
1. Create a new Google Sheet
2. Copy the sheet ID from the URL:
   ```
   https://docs.google.com/spreadsheets/d/[SHEET_ID]/edit
   ```
3. Share the sheet with your service account email
4. Grant **Editor** permissions

### Gemini AI Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the generated API key
4. Add it to your `.env` file

---

## 🎨 Usage Examples

### Transaction Input Examples

```text
# Simple expense
"Spent $25 on lunch at McDonald's"

# Income with date
"Received $5000 salary on December 1st"

# Pending payment
"Need to pay $120 for electricity bill due next week"

# Complex transaction
"Bought groceries for $85.50 at Whole Foods yesterday, mostly organic vegetables"
```

### Category Examples

#### Income Categories
- 💼 **Salary**: Regular employment income
- 📈 **Investments**: Returns from investments
- 🏢 **Business**: Business revenue and profits
- 💰 **Other Income**: Freelance, gifts, etc.

#### Expense Categories
- 🍽️ **Food & Dining**: Restaurants, groceries, food delivery
- 🛍️ **Shopping**: Clothing, electronics, general purchases
- 🚗 **Transportation**: Gas, public transport, ride-sharing
- 💡 **Bills & Utilities**: Electricity, water, internet, phone
- 🎬 **Entertainment**: Movies, games, subscriptions
- 🏥 **Health & Wellness**: Medical expenses, gym, supplements
- 📚 **Other Expenses**: Miscellaneous spending

---

## 📁 Project Structure

```
pocket_pulse/
├── 📄 app.py                 # Main Streamlit application
├── 📁 config/
│   ├── __pycache__/         # Python cache files
│   └── constants.py         # Application constants
├── 📄 pyproject.toml        # Project dependencies and configuration
├── 📄 uv.lock              # Dependency lock file
├── 📄 LICENSE              # MIT License
└── 📄 README.md            # This file
```

---

## 🛠️ Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GOOGLE_SHEETS_CREDENTIALS` | Path to Google service account JSON | `./credentials.json` |
| `GOOGLE_SHEET_ID` | Google Sheet ID from URL | `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms` |
| `GEMINI_API_KEY` | Gemini AI API key | `AIzaSyBvOkBw...` |

### Customization Options

- **Categories**: Modify `config/constants.py` to add custom categories
- **Date Formats**: Adjust date parsing logic for different formats
- **UI Theme**: Customize Streamlit theme in `app.py`

---

## 🔮 Future Roadmap

### Phase 1: Core Enhancements
- [ ] 🔐 **Multi-user Authentication**: Role-based access control
- [ ] 💳 **Budget Management**: Set and track spending limits
- [ ] 🔔 **Smart Alerts**: Notifications for unusual spending
- [ ] 🔄 **Recurring Transactions**: Automatic recurring entry setup

### Phase 2: Advanced Features
- [ ] 📄 **Receipt OCR**: Upload receipts for automatic processing
- [ ] 🌍 **Multi-Currency Support**: Handle multiple currencies with exchange rates
- [ ] 📱 **Mobile App**: Native iOS/Android applications
- [ ] 🔄 **Offline Mode**: Cache data for offline access

### Phase 3: Intelligence Features
- [ ] 🎯 **Savings Goals**: Track progress toward financial goals
- [ ] 🔍 **Anomaly Detection**: Identify unusual spending patterns
- [ ] 📊 **Financial Forecasting**: Predict future financial trends
- [ ] 🤖 **Chat Assistant**: Advanced conversational AI for financial advice

---

## 👥 Contributing

We welcome contributions from the community! Here's how you can help:

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests and ensure code quality
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add tests for new features
- Update documentation for changes
- Ensure all tests pass before submitting

### Team Structure

| Contributor | Role | Focus Area |
|-------------|------|------------|
| **Sahil** | Backend Developer | Data layer & integrations (`services/`, `pages/`) |
| **Amrin** | Frontend Developer | UI/UX & Analytics (`typings/`, `utils/`) |
| **Yash** | Full-Stack Developer | Core app logic & NLP parsing (remaining files) |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No warranty provided

---

## 🙏 Acknowledgments

### Technologies Used
- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini AI](https://ai.google.dev)** - Natural language processing
- **[Google Sheets API](https://developers.google.com/sheets)** - Data storage
- **[Plotly](https://plotly.com/)** - Data visualization
- **[Python](https://python.org)** - Core programming language

### Special Thanks
- Google AI team for the powerful Gemini API
- Streamlit team for the amazing web framework
- Open source community for inspiration and tools

---

## 💬 Support & Community

### Getting Help
1. 📖 **Check Documentation**: Review this README and inline code comments
2. 🐛 **Report Issues**: Open an issue in the [GitHub repository](https://github.com/BHARTIYAYASH/PocketPulse.git)
3. 💬 **Community Discussion**: Join our discussions for questions and ideas
4. 📧 **Contact Maintainers**: Reach out to the development team

### Common Issues

| Issue | Solution |
|-------|----------|
| Google Sheets API errors | Verify service account permissions and sheet sharing |
| Gemini API rate limits | Check API key validity and quota limits |
| Date parsing issues | Ensure dates are in recognizable format |
| Missing dependencies | Run `uv sync` to install all requirements |

---

## 🔒 Security & Privacy

### Data Protection
- 🔐 **Encrypted Storage**: All data encrypted in Google Sheets
- 🔑 **Secure Authentication**: Service account-based authentication
- 🚫 **No Data Collection**: We don't collect or store personal information
- 🔄 **Regular Updates**: Keep dependencies updated for security patches

### Best Practices
- ❌ **Never commit** `.env` files or credentials to version control
- 🔑 **Keep API keys secure** and rotate them regularly
- 👤 **Use principle of least privilege** for service account permissions
- 🔍 **Regular security audits** of dependencies and code

---

<div align="center">

**Made with ❤️ by the PocketPulse Team**

[⭐ Star this repo] 

</div>