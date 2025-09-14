#!/usr/bin/env python3
"""
Stock Portfolio Tracker - CodeAlpha Python Internship Project
=============================================================

A simple stock tracker that calculates total investment based on manually defined stock prices.

Author: CodeAlpha Intern
Date: September 2025
"""

import csv
import os
from datetime import datetime


class StockPortfolioTracker:
    """A class to manage and track stock portfolios."""
    
    def __init__(self):
        """Initialize the portfolio tracker with predefined stock prices."""
        # Hardcoded stock prices (in USD)
        self.stock_prices = {
            "AAPL": 180.50,   # Apple Inc.
            "TSLA": 250.75,   # Tesla Inc.
            "GOOGL": 2750.30, # Alphabet Inc.
            "MSFT": 415.20,   # Microsoft Corporation
            "AMZN": 3380.90,  # Amazon.com Inc.
            "META": 305.15,   # Meta Platforms Inc.
            "NFLX": 485.60,   # Netflix Inc.
            "NVDA": 470.85,   # NVIDIA Corporation
            "PYPL": 285.40,   # PayPal Holdings Inc.
            "ADBE": 620.75    # Adobe Inc.
        }
        
        self.portfolio = {}  # Dictionary to store user's portfolio
    
    def display_available_stocks(self):
        """Display all available stocks and their current prices."""
        print("\n" + "=" * 60)
        print("           📈 AVAILABLE STOCKS & PRICES 📈")
        print("=" * 60)
        print(f"{'Stock Symbol':<12} {'Company':<25} {'Price (USD)':<12}")
        print("-" * 60)
        
        stock_info = {
            "AAPL": "Apple Inc.",
            "TSLA": "Tesla Inc.",
            "GOOGL": "Alphabet Inc.",
            "MSFT": "Microsoft Corp.",
            "AMZN": "Amazon.com Inc.",
            "META": "Meta Platforms Inc.",
            "NFLX": "Netflix Inc.",
            "NVDA": "NVIDIA Corp.",
            "PYPL": "PayPal Holdings Inc.",
            "ADBE": "Adobe Inc."
        }
        
        for symbol, price in self.stock_prices.items():
            company = stock_info.get(symbol, "Unknown Company")
            print(f"{symbol:<12} {company:<25} ${price:<11.2f}")
        
        print("=" * 60)
    
    def add_stock_to_portfolio(self):
        """Add a stock to the user's portfolio."""
        while True:
            self.display_available_stocks()
            
            stock_symbol = input("\nEnter stock symbol (or 'back' to return): ").strip().upper()
            
            if stock_symbol.lower() == 'back':
                return
            
            if stock_symbol not in self.stock_prices:
                print(f"❌ Stock symbol '{stock_symbol}' not found in our database.")
                print("Please choose from the available stocks listed above.")
                continue
            
            try:
                quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
                if quantity <= 0:
                    print("❌ Quantity must be a positive number.")
                    continue
                
                # Add to portfolio (if stock exists, add to existing quantity)
                if stock_symbol in self.portfolio:
                    self.portfolio[stock_symbol] += quantity
                    print(f"✅ Added {quantity} more shares of {stock_symbol}")
                    print(f"Total {stock_symbol} shares: {self.portfolio[stock_symbol]}")
                else:
                    self.portfolio[stock_symbol] = quantity
                    print(f"✅ Added {quantity} shares of {stock_symbol} to your portfolio")
                
                break
                
            except ValueError:
                print("❌ Please enter a valid number for quantity.")
    
    def remove_stock_from_portfolio(self):
        """Remove a stock from the user's portfolio."""
        if not self.portfolio:
            print("❌ Your portfolio is empty. Nothing to remove.")
            return
        
        print("\n📋 Your Current Portfolio:")
        self.display_portfolio()
        
        stock_symbol = input("\nEnter stock symbol to remove (or 'back' to return): ").strip().upper()
        
        if stock_symbol.lower() == 'back':
            return
        
        if stock_symbol not in self.portfolio:
            print(f"❌ {stock_symbol} not found in your portfolio.")
            return
        
        try:
            current_quantity = self.portfolio[stock_symbol]
            print(f"Current quantity of {stock_symbol}: {current_quantity}")
            
            quantity_to_remove = int(input(f"Enter quantity to remove (max {current_quantity}): "))
            
            if quantity_to_remove <= 0:
                print("❌ Quantity must be a positive number.")
                return
            
            if quantity_to_remove > current_quantity:
                print(f"❌ Cannot remove {quantity_to_remove} shares. You only have {current_quantity}.")
                return
            
            if quantity_to_remove == current_quantity:
                del self.portfolio[stock_symbol]
                print(f"✅ Removed all {stock_symbol} shares from portfolio")
            else:
                self.portfolio[stock_symbol] -= quantity_to_remove
                print(f"✅ Removed {quantity_to_remove} shares of {stock_symbol}")
                print(f"Remaining {stock_symbol} shares: {self.portfolio[stock_symbol]}")
        
        except ValueError:
            print("❌ Please enter a valid number.")
    
    def calculate_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        if not self.portfolio:
            return 0.0
        
        total_value = 0.0
        for stock, quantity in self.portfolio.items():
            stock_value = self.stock_prices[stock] * quantity
            total_value += stock_value
        
        return total_value
    
    def display_portfolio(self):
        """Display the current portfolio with values."""
        if not self.portfolio:
            print("📭 Your portfolio is empty.")
            return
        
        print("\n" + "=" * 70)
        print("                  💼 YOUR PORTFOLIO 💼")
        print("=" * 70)
        print(f"{'Stock':<8} {'Quantity':<10} {'Price/Share':<12} {'Total Value':<15}")
        print("-" * 70)
        
        total_portfolio_value = 0.0
        
        for stock, quantity in self.portfolio.items():
            price_per_share = self.stock_prices[stock]
            total_value = price_per_share * quantity
            total_portfolio_value += total_value
            
            print(f"{stock:<8} {quantity:<10} ${price_per_share:<11.2f} ${total_value:<14.2f}")
        
        print("-" * 70)
        print(f"{'TOTAL PORTFOLIO VALUE:':<45} ${total_portfolio_value:<14.2f}")
        print("=" * 70)
    
    def save_portfolio_to_file(self, filename=None):
        """Save the portfolio to a CSV or TXT file."""
        if not self.portfolio:
            print("❌ Portfolio is empty. Nothing to save.")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"portfolio_{timestamp}"
        
        # Ask user for file format
        while True:
            file_format = input("Save as (1) CSV or (2) TXT? Enter 1 or 2: ").strip()
            if file_format in ['1', '2']:
                break
            print("❌ Please enter 1 for CSV or 2 for TXT.")
        
        if file_format == '1':
            filename += '.csv'
            self._save_as_csv(filename)
        else:
            filename += '.txt'
            self._save_as_txt(filename)
    
    def _save_as_csv(self, filename):
        """Save portfolio as CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header
                writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
                
                total_value = 0.0
                
                # Write portfolio data
                for stock, quantity in self.portfolio.items():
                    price = self.stock_prices[stock]
                    value = price * quantity
                    total_value += value
                    writer.writerow([stock, quantity, f"${price:.2f}", f"${value:.2f}"])
                
                # Write total
                writer.writerow(['', '', 'TOTAL:', f"${total_value:.2f}"])
            
            print(f"✅ Portfolio saved successfully as {filename}")
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    def _save_as_txt(self, filename):
        """Save portfolio as TXT file."""
        try:
            with open(filename, 'w', encoding='utf-8') as txtfile:
                txtfile.write("STOCK PORTFOLIO TRACKER - CodeAlpha\n")
                txtfile.write("=" * 50 + "\n")
                txtfile.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                txtfile.write(f"{'Stock':<8} {'Quantity':<10} {'Price/Share':<12} {'Total Value':<15}\n")
                txtfile.write("-" * 50 + "\n")
                
                total_value = 0.0
                
                for stock, quantity in self.portfolio.items():
                    price = self.stock_prices[stock]
                    value = price * quantity
                    total_value += value
                    txtfile.write(f"{stock:<8} {quantity:<10} ${price:<11.2f} ${value:<14.2f}\n")
                
                txtfile.write("-" * 50 + "\n")
                txtfile.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
            
            print(f"✅ Portfolio saved successfully as {filename}")
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    def load_demo_portfolio(self):
        """Load a demo portfolio for testing purposes."""
        demo_portfolio = {
            "AAPL": 10,
            "TSLA": 5,
            "GOOGL": 2
        }
        
        self.portfolio = demo_portfolio.copy()
        print("✅ Demo portfolio loaded!")
        print("Demo includes: 10 AAPL, 5 TSLA, 2 GOOGL shares")
    
    def clear_portfolio(self):
        """Clear the entire portfolio."""
        if not self.portfolio:
            print("📭 Portfolio is already empty.")
            return
        
        confirm = input("⚠️  Are you sure you want to clear your entire portfolio? (y/n): ").strip().lower()
        if confirm in ['y', 'yes']:
            self.portfolio.clear()
            print("✅ Portfolio cleared successfully.")
        else:
            print("Portfolio clearing cancelled.")
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("     📊 STOCK PORTFOLIO TRACKER - CodeAlpha 📊")
        print("=" * 50)
        print("1. 👀 View Available Stocks")
        print("2. ➕ Add Stock to Portfolio")
        print("3. ➖ Remove Stock from Portfolio")
        print("4. 📋 View My Portfolio")
        print("5. 💾 Save Portfolio to File")
        print("6. 🧪 Load Demo Portfolio")
        print("7. 🗑️  Clear Portfolio")
        print("8. 🚪 Exit")
        print("=" * 50)
    
    def run(self):
        """Main application loop."""
        print("🎉 Welcome to Stock Portfolio Tracker!")
        print("Track your investments with real-time calculations!")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-8): ").strip()
                
                if choice == '1':
                    self.display_available_stocks()
                    input("\nPress Enter to continue...")
                
                elif choice == '2':
                    self.add_stock_to_portfolio()
                
                elif choice == '3':
                    self.remove_stock_from_portfolio()
                
                elif choice == '4':
                    self.display_portfolio()
                    input("\nPress Enter to continue...")
                
                elif choice == '5':
                    self.save_portfolio_to_file()
                
                elif choice == '6':
                    self.load_demo_portfolio()
                
                elif choice == '7':
                    self.clear_portfolio()
                
                elif choice == '8':
                    print("\n👋 Thank you for using Stock Portfolio Tracker!")
                    print("Happy investing! 📈")
                    break
                
                else:
                    print("❌ Invalid choice. Please enter a number between 1-8.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using Stock Portfolio Tracker!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                print("Please try again.")


def main():
    """Main function to run the Stock Portfolio Tracker."""
    tracker = StockPortfolioTracker()
    tracker.run()


if __name__ == "__main__":
    main()