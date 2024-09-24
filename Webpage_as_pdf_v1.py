import pdfkit

# URL of the webpage to convert
url = 'https://mxlinux.org/mx-linux-blog/'

# Output PDF file path
output_path = '/home/jasvir/Music/html/output.pdf'

# Convert URL to PDF
pdfkit.from_url(url, output_path)

print(f'PDF saved as {output_path}')
