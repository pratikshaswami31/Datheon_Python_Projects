import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set project file paths
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "sales_summary.csv"
CHART_FILE = BASE_DIR / "sales_chart.png"
REPORT_FILE = BASE_DIR / "analysis_report.txt"

try:
    # Read the CSV file
    df = pd.read_csv(INPUT_FILE)

    # Validate required columns
    required_columns = {
        "order_id", "product", "category",
        "quantity", "price", "city"
    }

    if not required_columns.issubset(df.columns):
        raise ValueError("CSV is missing required columns.")

    # Convert numeric columns
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove invalid rows and duplicate orders
    df = df.dropna(subset=["order_id", "product", "quantity", "price"])
    df = df.drop_duplicates(subset=["order_id"])

    # Calculate total sales
    df["total_sales"] = df["quantity"] * df["price"]

    # Save analyzed data
    df.to_csv(OUTPUT_FILE, index=False)

    # Calculate summary
    total_orders = len(df)
    total_revenue = df["total_sales"].sum()
    best_product = (
        df.groupby("product")["total_sales"]
        .sum()
        .idxmax()
    )

    city_sales = df.groupby("city")["total_sales"].sum()
    product_sales = df.groupby("product")["total_sales"].sum()

    # Create sales chart
    product_sales.plot(kind="bar", title="Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales Amount")
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()

    # Generate text report
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write("SALES ANALYSIS REPORT\n")
        file.write("=====================\n")
        file.write(f"Total orders: {total_orders}\n")
        file.write(f"Total revenue: Rs. {total_revenue:,.2f}\n")
        file.write(f"Best-selling product by revenue: {best_product}\n\n")
        file.write("Sales by city:\n")
        file.write(city_sales.to_string())
        file.write("\n\nSales by product:\n")
        file.write(product_sales.to_string())

    print("Data analysis completed successfully!")
    print("Total orders:", total_orders)
    print(f"Total revenue: Rs. {total_revenue:,.2f}")
    print("Best-selling product by revenue:", best_product)
    print("\nGenerated files:")
    print("- sales_summary.csv")
    print("- sales_chart.png")
    print("- analysis_report.txt")

except (OSError, ValueError, pd.errors.ParserError) as error:
    print("Analysis failed:", error)