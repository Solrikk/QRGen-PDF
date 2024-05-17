import qrcode
from fpdf import FPDF

data_list = [
    f"More extensive information content for QR Code {i+1}" for i in range(20)
]

for i, data in enumerate(data_list):
  qr = qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=2,
                     border=2)
  qr.add_data(data)
  qr.make(fit=True)

  img = qr.make_image(fill="black", back_color="white")
  img.save(f"qr_code_{i+1}.png")


class PDF(FPDF):

  def header(self):
    self.set_font('Arial', 'B', 12)
    self.cell(0, 10, 'QR Codes', 0, 1, 'C')

  def add_qr_codes(self, data_list):
    self.add_page()
    qr_size = 20
    margin = 5
    x_start = margin
    y_start = margin + 10
    x = x_start
    y = y_start

    for i in range(len(data_list)):
      if i % 5 == 0 and i != 0:
        x = x_start
        y += qr_size + margin
      self.image(f'qr_code_{i+1}.png', x, y, qr_size, qr_size)
      x += qr_size + margin


pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)
pdf.add_qr_codes(data_list)
pdf.output('qr_codes.pdf')
