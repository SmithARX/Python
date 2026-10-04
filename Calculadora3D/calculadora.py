# Create a simple 3D printing cost calculator Excel file using openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Calculadora"

# Headers
ws["A1"] = "Calculadora de Impressão 3D"

# Input section
ws["A3"] = "Peso da peça (g)"
ws["B3"] = 0

ws["A4"] = "Tempo de impressão (h)"
ws["B4"] = 0

# Constants
ws["D3"] = "Custo PLA por g (R$)"
ws["E3"] = 0.10

ws["D4"] = "Energia por hora (R$)"
ws["E4"] = 0.1236  # 0.12 kWh * 1.03

ws["D5"] = "Preço sugerido por g (R$)"
ws["E5"] = 0.50

# Calculations
ws["A6"] = "Custo do material"
ws["B6"] = "=B3*E3"

ws["A7"] = "Custo de energia"
ws["B7"] = "=B4*E4"

ws["A8"] = "Custo total"
ws["B8"] = "=B6+B7"

ws["A9"] = "Preço sugerido de venda"
ws["B9"] = "=B3*E5"

# Adjust column widths
ws.column_dimensions["A"].width = 28
ws.column_dimensions["B"].width = 15
ws.column_dimensions["D"].width = 28
ws.column_dimensions["E"].width = 15

file_path = "C:\Users\Eric Smith\Documents\GitHub\Python\Calculadora3D\calculadora_impressao_3d.xlsx"
wb.save(file_path)

file_path