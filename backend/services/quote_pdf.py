
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
def build_quote_pdf(quote: dict) -> bytes:
    buf=BytesIO(); c=canvas.Canvas(buf, pagesize=A4); w,h=A4
    def line(y,t,s=11,b=False): c.setFont("Helvetica-Bold" if b else "Helvetica", s); c.drawString(20*mm,y,t)
    y=h-25*mm; line(y,"FreightSense — Quote Summary",16,True); y-=10*mm
    line(y,f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"); y-=8*mm
    lane=f"{quote.get('origin','?')} → {quote.get('destination','?')} ({quote.get('equipment','?')})"; line(y,f"Lane: {lane}",12,True); y-=8*mm
    line(y,f"Predicted base: ${quote.get('predicted_base','-')}"); y-=7*mm
    sur=quote.get('surcharges',{}); 
    if sur: line(y,"Surcharges:",12,True); y-=7*mm; 
    for k,v in sur.items(): line(y,f"• {k}: ${v}"); y-=6*mm
    line(y,f"Total (suggested): ${quote.get('total','-')}",12,True); y-=7*mm
    line(y,f"ETA (days): ~{quote.get('eta_days','-')}"); y-=7*mm
    line(y,f"Margin: {quote.get('margin_pct','-')}%"); y-=10*mm
    if quote.get('warning'): line(y,f"Warning: {quote['warning']}",11,True); y-=8*mm
    c.showPage(); c.save(); return buf.getvalue()
