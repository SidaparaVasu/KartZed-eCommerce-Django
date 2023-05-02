
def download_report(request): 
    resonse = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Users.pdf"'
    # Create a new PDF document and write to the response
    pdf = canvas.Canvas(response)
    pdf.setTitle("Top 5 Costliest Games Report")
    # Define the table headers
    headers = ['Rank','Product Key','Game Name','Game Price']
    # Define the table data
    data = [[g.product_key, g.game_name, g.game_price] for g in Games.objects.order_by(F('game_price').desc())[:5]]
    # Define the width and height of each column
    col_widths = [pdf.stringWidth(h) + 10 for h in headers]
    row_height = 20
    # Draw the table headers
    for i, header in enumerate(headers):
        pdf.drawString(sum(col_widths[:i]), 750, header)
    # Draw the table data
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))
    # Save the PDF document and close the canvas
    pdf.save()

    return response
