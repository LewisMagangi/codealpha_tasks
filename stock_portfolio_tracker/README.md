# Stock Portfolio Tracker - CodeAlpha Internship Project

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

A comprehensive stock portfolio tracker that calculates total investment value based on predefined stock prices, created as part of the CodeAlpha internship program.

## 📈 Application Description

The Stock Portfolio Tracker is a console-based application that allows users to manage their stock investments. Users can add stocks to their portfolio, track their total investment value, and save their portfolio data to files. The application features:

- **10 predefined stocks** with realistic prices
- **Portfolio management** (add/remove stocks)
- **Real-time value calculations**
- **File export** (CSV and TXT formats)
- **User-friendly interface** with clear menus
- **Demo portfolio** for testing

## 🚀 Features

- ✅ **Stock Management**: Add and remove stocks from portfolio
- ✅ **Real-time Calculations**: Automatic portfolio value computation
- ✅ **Multiple File Formats**: Export to CSV or TXT files
- ✅ **Data Validation**: Input validation and error handling
- ✅ **Demo Mode**: Pre-loaded portfolio for testing
- ✅ **Clear Interface**: Organized menu system with emojis
- ✅ **Portfolio Display**: Detailed view with individual and total values

## 🏢 Available Stocks

| Symbol | Company | Price (USD) |
|--------|---------|-------------|
| AAPL | Apple Inc. | $180.50 |
| TSLA | Tesla Inc. | $250.75 |
| GOOGL | Alphabet Inc. | $2,750.30 |
| MSFT | Microsoft Corp. | $415.20 |
| AMZN | Amazon.com Inc. | $3,380.90 |
| META | Meta Platforms Inc. | $305.15 |
| NFLX | Netflix Inc. | $485.60 |
| NVDA | NVIDIA Corp. | $470.85 |
| PYPL | PayPal Holdings Inc. | $285.40 |
| ADBE | Adobe Inc. | $620.75 |

## 🛠️ Installation & Setup

1. **Clone/Download the project**:

   ```bash
   git clone https://github.com/YourUsername/CodeAlpha_StockPortfolioTracker.git
   cd CodeAlpha_StockPortfolioTracker
   ```

2. **Requirements**:
   - Python 3.6 or higher
   - No external dependencies required

## 🎯 How to Use

1. **Run the application**:

   ```bash
   python stock_tracker.py
   ```

2. **Main Menu Options**:
   - **View Available Stocks**: See all stocks and their current prices
   - **Add Stock to Portfolio**: Add stocks with specified quantities
   - **Remove Stock from Portfolio**: Remove stocks or reduce quantities
   - **View My Portfolio**: Display current portfolio with values
   - **Save Portfolio to File**: Export portfolio data
   - **Load Demo Portfolio**: Load sample data for testing
   - **Clear Portfolio**: Remove all stocks from portfolio
   - **Exit**: Close the application

3. **Example Usage**:

   ```text
   📊 STOCK PORTFOLIO TRACKER - CodeAlpha 📊
   
   1. 👀 View Available Stocks
   2. ➕ Add Stock to Portfolio
   3. ➖ Remove Stock from Portfolio
   4. 📋 View My Portfolio
   5. 💾 Save Portfolio to File
   6. 🧪 Load Demo Portfolio
   7. 🗑️  Clear Portfolio
   8. 🚪 Exit
   
   Enter your choice (1-8): 2
   ```

## 📁 Project Structure

```text
stock_portfolio_tracker/
│
├── stock_tracker.py    # Main application file
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
└── sample_outputs/     # Example output files
    ├── portfolio_sample.csv
    └── portfolio_sample.txt
```

## 🔧 Key Python Concepts Demonstrated

This project showcases important Python programming concepts:

- **Classes and OOP**: `StockPortfolioTracker` class with organized methods
- **Dictionaries**: For storing stock prices and portfolio data
- **File Handling**: CSV and TXT file creation and writing
- **Input/Output**: Console interaction and data formatting
- **Exception Handling**: Try-catch blocks for error management
- **Data Validation**: Input checking and sanitization
- **String Formatting**: Professional output presentation
- **DateTime Module**: Timestamp generation for files
- **CSV Module**: Structured data export
- **Loops and Conditionals**: Program flow control

## 💾 File Export Examples

### CSV Output

```csv
Stock Symbol,Quantity,Price per Share,Total Value
AAPL,10,$180.50,$1805.00
TSLA,5,$250.75,$1253.75
GOOGL,2,$2750.30,$5500.60
,,TOTAL:,$8559.35
```

### TXT Output

```text
STOCK PORTFOLIO TRACKER - CodeAlpha
==================================================
Generated on: 2025-09-14 15:30:45

Stock    Quantity   Price/Share  Total Value    
--------------------------------------------------
AAPL     10         $180.50      $1805.00      
TSLA     5          $250.75      $1253.75      
GOOGL    2          $2750.30     $5500.60      
--------------------------------------------------
TOTAL PORTFOLIO VALUE: $8559.35
```

## 🎮 Application Flow

```text
Start Application
    ↓
Display Main Menu
    ↓
User Selection
    ↓
Process User Choice
    ├── View Stocks → Display Stock List
    ├── Add Stock → Get Input → Validate → Add to Portfolio
    ├── Remove Stock → Select Stock → Validate → Remove from Portfolio
    ├── View Portfolio → Calculate Values → Display
    ├── Save to File → Choose Format → Generate File
    ├── Load Demo → Load Sample Data
    ├── Clear Portfolio → Confirm → Clear Data
    └── Exit → End Application
```

## 📊 Sample Code Snippets

### Portfolio Value Calculation

```python
def calculate_portfolio_value(self):
    if not self.portfolio:
        return 0.0
    
    total_value = 0.0
    for stock, quantity in self.portfolio.items():
        stock_value = self.stock_prices[stock] * quantity
        total_value += stock_value
    
    return total_value
```

### CSV Export Function

```python
def _save_as_csv(self, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
        
        for stock, quantity in self.portfolio.items():
            price = self.stock_prices[stock]
            value = price * quantity
            writer.writerow([stock, quantity, f"${price:.2f}", f"${value:.2f}"])
```

## 🏆 Learning Outcomes

After completing this project, you will have experience with:

- Object-oriented programming in Python
- Dictionary manipulation and data structures
- File I/O operations (CSV and TXT)
- User input validation and error handling
- Menu-driven console applications
- Data formatting and presentation
- Real-world problem solving with code

## 🧪 Testing the Application

1. **Run the application**: `python stock_tracker.py`
2. **Load demo portfolio**: Choose option 6 to load sample data
3. **View portfolio**: Choose option 4 to see the loaded data
4. **Add more stocks**: Try adding different stocks with various quantities
5. **Save portfolio**: Export your data to see file generation
6. **Test validation**: Try invalid inputs to see error handling

## 🤝 Contributing

This is an internship project, but feedback and suggestions are welcome!

## 📄 License

This project is licensed under the MIT License.

## 👥 About CodeAlpha

CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This project is part of their Python internship program.

---

## Happy Investing! 📈

Built with ❤️ in Python
