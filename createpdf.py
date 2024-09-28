from fpdf import FPDF
from datetime import datetime


title = 'Container Inspection Report'

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, container_id, iso_code, timestamp, grade):
        self.set_font('Arial', '', 10)
        self.cell(150, 10, f'Customer Ref : ', 0, 0, 'L')
        self.cell(50, 10, f'Surveyor : ', 0, 1, 'L')
        self.cell(150, 10, f'Container No. : {container_id} ({iso_code})', 0, 0, 'L')
        self.cell(50, 10, f'Currency : MYR', 0, 1, 'L')
        self.cell(0, 10, f'M.G.W : {grade}', 0, 1)
        self.cell(0, 10, f'Gate In Date : {timestamp}', 0, 1)
        self.cell(0, 10, f'Grade : {grade}', 0, 1)
        # Mention in italics
        self.set_font('', 'I')

    def print_chapter(self, num, title, container_id, iso_code, timestamp, grade):
        self.add_page()
        self.line_info()
        self.chapter_body(container_id, iso_code, timestamp, grade)

    def damage_table(self, damage_info):
         # Add a line break
        self.ln(10)

        # Middle half: Damage info table
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Damage Information', 0, 1)
        self.set_font('Arial', 'B', 8)

        # Column headers
        y = self.get_y()
        self.line(10, y, 200, y)
        self.cell(30, 10, 'No', 0)
        self.cell(30, 10, 'Comp. Code', 0)
        self.cell(30, 10, 'LOC.', 0)
        self.cell(30, 10, 'Damage', 0)
        self.cell(0, 10, '', 0, 1)  # New line
        y = self.get_y()
        self.line(10, y, 200, y)

        self.set_font('Arial', '', 8)
        # Populate the damage info table
        for i, damage in enumerate(damage_info):
            self.cell(30, 10, str(i), 0)
            self.cell(30, 10, 'PAA', 0)
            self.cell(30, 10, damage[4], 0)
            self.cell(30, 10, damage[3], 0)
            self.ln()

        # Add a line break
        self.ln()


    def line_info(self):
        self.set_font('Arial', 'B', 8)

        self.ln(10)
        self.cell(0, 5, 'LINE 9 DEPOT', 0 ,1)
        self.cell(0, 5, 'JLN PARANG OFF JLN PELABUHAN UTARA', 0, 1)
        self.cell(0, 5, '42000 PELAUBUHAN KLANG', 0, 1)
        self.cell(0, 5, 'SELANGOR MALAYSIA', 0, 1)
        self.cell(0, 5, 'Tel No: 016-4442926', 0, 1)
        self.ln(30)
        self.dashed_line(10, 70, 200, 70, dash_length = 1, space_length = 1)




    def container_image(self, imgpath):
        self.add_page()
        try:
            self.image(imgpath, x=10, w=190)  # Adjust width as needed
        except Exception as e:
            print(f"Could not add image: {e}")

def report(container_id, timestamp, df):
    '''
    container_iso = 'TCNU6215065'
    code = '45G1'
    timestamp = '20240809124530'
    time = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
    time = time.date()
    imgpath = '../20240902230430.png'
    container_grade = 'B'
    damage_info = [
            {"type": "Dent", "location": "LT12", "comp": "PAA"},
            ]
    '''
           
    damage_info = df.values.tolist()
    print(damage_info)
    time = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
    time = time.strftime('%Y-%m-%d %H:%M:%S')
    pdf = PDF()
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'A RUNAWAY REEF', container_id, '45G1', time, 'B')
    pdf.damage_table(damage_info)
    #pdf.container_image(imgpath)
    pdf.output('report.pdf', 'F')

if __name__ == "__main__":
    print('hi')
    #report()
