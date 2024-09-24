from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Define the data
data = [
    ["Parameter", "Titan", "Kalyan Jewelers"],
    ["Market Cap", "₹3,02,362 Cr.", "₹59,126 Cr."],
    ["Current Price", "₹3,406", "₹574"],
    ["High / Low", "₹3,887 / ₹2,882", "₹634 / ₹163"],
    ["Stock P/E", "86.5", "99.3"],
    ["Book Value", "₹106", "₹40.7"],
    ["Dividend Yield", "0.32 %", "0.21 %"],
    ["ROCE", "22.7 %", "14.0 %"],
    ["ROE", "32.9 %", "15.2 %"],
    ["Face Value", "₹1.00", "₹10.0"],
    ["PEG Ratio", "4.28", "0.57"],
    ["Sales Growth (3 Years)", "33.1 %", "29.3 %"],
    ["Profit Var (3 Years)", "53.8 %", "367 %"],
    ["Price to Book Value", "32.2", "14.1"],
    ["EPS", "₹39.4", "₹5.80"],
    ["Industry PE", "27.4", "27.4"],
    ["Sales Growth", "25.9 %", "31.8 %"],
    ["Debt", "₹15,528 Cr.", "₹4,486 Cr."],
    ["Promoter Holding", "52.9 %", "60.6 %"],
    ["Change in Prom. Hold", "0.00 %", "-0.04 %"],
    ["Earnings Yield", "1.66 %", "1.86 %"],
    ["Profit Growth", "7.50 %", "30.6 %"],
    ["CMP / FCF", "877", "86.0"],
    ["Return over 3 Months", "-4.99 %", "36.8 %"],
    ["Net Worth", "₹9,393 Cr.", "₹4,189 Cr."],
    ["Net CF", "₹177 Cr.", "₹36.8 Cr."],
    ["EPS Growth (3 Years)", "53.8 %", "367 %"],
    ["EPS Last Year", "₹39.4", "₹5.80"]
]

# Define the PDF file name
pdf_file = "company_comparison.pdf"

# Create a PDF
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Set up font and size
c.setFont("Helvetica", 10)

# Define starting position
x = inch
y = height - 2 * inch

# Define column widths
col_widths = [2 * inch, 2.5 * inch, 2.5 * inch]

# Draw table headers
for i, header in enumerate(data[0]):
    c.drawString(x + sum(col_widths[:i]), y, header)

# Draw table rows
row_height = 0.4 * inch
for row in data[1:]:
    for i, cell in enumerate(row):
        c.drawString(x + sum(col_widths[:i]), y - row_height, cell)
    y -= row_height

# Save the PDF
c.save()

print(f"PDF saved as {pdf_file}")
