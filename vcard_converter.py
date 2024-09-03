from http.server import BaseHTTPRequestHandler
import pandas as pd
import zipfile
from io import BytesIO


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Read CSV from POST data
        df = pd.read_csv(BytesIO(post_data))

        # Create ZIP file in memory
        memory_file = BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for index, row in df.iterrows():
                vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{row['Last Name']};{row['First Name']}
FN:{row['First Name']} {row['Last Name']}
TEL;TYPE=CELL:{row['Phone Number']}
EMAIL:{row['Email Address']}
END:VCARD
                """
                zf.writestr(
                    f"{row['First Name']}_{row['Last Name']}.vcf", vcard)

        memory_file.seek(0)
        zip_content = memory_file.read()

        self.send_response(200)
        self.send_header('Content-type', 'application/zip')
        self.send_header('Content-Disposition',
                         'attachment; filename="vcards.zip"')
        self.end_headers()
        self.wfile.write(zip_content)
