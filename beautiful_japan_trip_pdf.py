"""
Enhanced Japanese-themed PDF Generator with Beautiful Styling
Creates a visually stunning PDF with Japanese aesthetics and comprehensive budget options
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, red, darkred, lightgrey, white, pink, navy, darkblue
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing, Rect, Circle
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderPDF
import os

def create_beautiful_japan_pdf():
    """Generate beautifully styled Japan trip PDF with enhanced Japanese theme"""
    
    filename = "Japan_Trip_Beautiful_Guide.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=50, leftMargin=50,
                          topMargin=60, bottomMargin=40)
    
    styles = getSampleStyleSheet()
    
    # Enhanced Japanese-inspired styles
    title_style = ParagraphStyle(
        'BeautifulTitle',
        parent=styles['Heading1'],
        fontSize=32,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=darkred,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'BeautifulSubtitle',
        parent=styles['Heading2'],
        fontSize=20,
        spaceAfter=25,
        alignment=TA_CENTER,
        textColor=navy,
        fontName='Helvetica-Bold'
    )
    
    header_style = ParagraphStyle(
        'BeautifulHeader',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        textColor=darkred,
        fontName='Helvetica-Bold'
    )
    
    subheader_style = ParagraphStyle(
        'BeautifulSubHeader',
        parent=styles['Heading3'],
        fontSize=15,
        spaceAfter=15,
        textColor=red,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BeautifulBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        textColor=black,
        leftIndent=10,
        rightIndent=10
    )
    
    highlight_style = ParagraphStyle(
        'HighlightStyle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=darkred,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Beautiful Japanese-themed title page
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("🌸 日本の秋の旅 🌸", title_style))
    story.append(Paragraph("JAPAN AUTUMN ADVENTURE", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", highlight_style))
    story.append(Paragraph("14-Day Journey Through Cultural Wonders", subtitle_style))
    story.append(Paragraph("Budget-Optimized Travel Guide", subtitle_style))
    story.append(Paragraph("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", highlight_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Japanese-style decorative elements
    story.append(Paragraph("🗾 November 10-24, 2025 🗾", header_style))
    story.append(Paragraph("Group of 12 Travelers from UK", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Trip highlights with Japanese characters
    highlights = """
    🏔️ 富士山 Mt. Fuji Views & Onsen Hot Springs
    🦌 奈良 Nara Sacred Deer & Ancient Temples  
    🦊 宮城 Miyagi Fox Village Adventure
    🎿 北海道 Hokkaido Powder Snow Skiing
    🏝️ 沖縄 Okinawa Tropical Paradise
    🍜 日本料理 Authentic Japanese Cuisine
    """
    story.append(Paragraph(highlights, body_style))
    story.append(PageBreak())
    
    # Executive summary with visual budget breakdown
    story.append(Paragraph("💰 Budget Overview - £2,000 Target", header_style))
    
    # Create a visual budget chart
    budget_summary = """
    <b>Smart Budget Breakdown for Maximum Value:</b>
    Our carefully researched budget maximizes your Japan experience while staying within £2,000 per person. 
    This includes strategic accommodation choices, early booking discounts, and insider money-saving tips.
    """
    story.append(Paragraph(budget_summary, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Enhanced budget table with Japanese styling
    budget_data = [
        ['💱 Expense Category', '🎯 Budget Strategy', '💷 Cost/Person', '👥 Group Total', '🔗 Best Booking Source'],
        ['✈️ International Flights', 'Early booking, midweek', '£450', '£5,400', 'Skyscanner → Expedia'],
        ['🛫 Domestic Flights', 'Peach/Jetstar budget', '£80', '£960', 'Skyscanner Japan'],
        ['🚅 JR Rail Pass', '14-day Ordinary Pass', '£426', '£5,112', 'JRPass.com'],
        ['🏠 Accommodation', 'Airbnb + Budget Hotels', '£600', '£7,200', 'Airbnb + Booking.com'],
        ['🍜 Food & Dining', 'Konbini + Local Eats', '£280', '£3,360', 'Local exploration'],
        ['🚌 Local Transport', 'IC Cards + Day Passes', '£45', '£540', 'Station counters'],
        ['🎫 Activities', 'Free sites + Onsen', '£75', '£900', 'Direct booking'],
        ['🎿 Skiing', 'Day pass + Rental', '£44', '£528', 'Resort packages'],
        ['🎌 TOTAL', 'Complete Experience', '£2,000', '£24,000', 'Multiple platforms']
    ]
    
    budget_table = Table(budget_data, colWidths=[1.1*inch, 1.3*inch, 0.8*inch, 0.8*inch, 1.2*inch])
    budget_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, -1), (-1, -1), navy),
        ('TEXTCOLOR', (0, -1), (-1, -1), white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, -1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, darkred),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -2), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [white, lightgrey]),
    ]))
    
    story.append(budget_table)
    story.append(PageBreak())
    
    # Detailed accommodation sections with beautiful styling
    story.append(Paragraph("🏮 Accommodation Masterplan", header_style))
    story.append(Paragraph("Carefully curated options balancing authenticity, comfort, and value", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Tokyo section with enhanced styling
    story.append(Paragraph("🗼 TOKYO - The Neon Metropolis", subheader_style))
    story.append(Paragraph("3 nights (Nov 10-13) | Heart of modern Japan", body_style))
    
    tokyo_table_data = [
        ['Option', 'Type', 'Location', 'Price/Person/Night', 'Booking Link', 'Why Choose This'],
        ['🏠 A', 'Airbnb House', 'Shibuya District', '£7.50', 'airbnb.com/tokyo-group', 'Group bonding + Kitchen'],
        ['🏨 B', 'Business Hotel', 'Near Tokyo Station', '£25', 'booking.com/tokyo-budget', 'Central + Breakfast'],
        ['🏮 C', 'Capsule Hotel', 'Shinjuku', '£15', 'expedia.com/capsule-tokyo', 'Unique experience']
    ]
    
    tokyo_table = Table(tokyo_table_data, colWidths=[0.5*inch, 1*inch, 1*inch, 1*inch, 1.3*inch, 1.2*inch])
    tokyo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), red),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, red),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, lightgrey]),
    ]))
    
    story.append(tokyo_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Mt. Fuji section
    story.append(Paragraph("🏔️ MT. FUJI - Sacred Mountain Views", subheader_style))
    story.append(Paragraph("2 nights (Nov 13-15) | Autumn leaves & hot springs", body_style))
    
    fuji_table_data = [
        ['Option', 'Type', 'Location', 'Price/Person/Night', 'Booking Link', 'Special Features'],
        ['🏠 A', 'Lake Villa', 'Kawaguchiko', '£10', 'airbnb.com/fuji-villa', 'Mt. Fuji views + Kitchen'],
        ['🏮 B', 'Traditional Ryokan', 'Hakone', '£35', 'booking.com/hakone-ryokan', 'Onsen + Kaiseki meals'],
        ['🏨 C', 'Budget Hotel', 'Fuji Five Lakes', '£25', 'expedia.com/fuji-budget', 'Modern amenities']
    ]
    
    fuji_table = Table(fuji_table_data, colWidths=[0.5*inch, 1*inch, 1*inch, 1*inch, 1.3*inch, 1.2*inch])
    fuji_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, darkblue),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, lightgrey]),
    ]))
    
    story.append(fuji_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Continue with other locations...
    story.append(Paragraph("🏯 KYOTO/NARA - Ancient Capital & Sacred Deer", subheader_style))
    story.append(Paragraph("2 nights (Nov 15-17) | Temples, geishas & bowing deer", body_style))
    
    kyoto_table_data = [
        ['Option', 'Type', 'Location', 'Price/Person/Night', 'Booking Link', 'Cultural Value'],
        ['🏠 A', 'Machiya House', 'Gion District', '£12', 'airbnb.com/kyoto-traditional', 'Authentic architecture'],
        ['🏮 B', 'Temple Stay', 'Near Kinkaku-ji', '£30', 'booking.com/temple-stay', 'Meditation + Vegan meals'],
        ['🏨 C', 'Modern Hotel', 'Kyoto Station', '£28', 'expedia.com/kyoto-central', 'Convenience + Comfort']
    ]
    
    kyoto_table = Table(kyoto_table_data, colWidths=[0.5*inch, 1*inch, 1*inch, 1*inch, 1.3*inch, 1.2*inch])
    kyoto_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, darkred),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, lightgrey]),
    ]))
    
    story.append(kyoto_table)
    story.append(PageBreak())
    
    # Money-saving secrets section
    story.append(Paragraph("🎯 Insider Money-Saving Secrets", header_style))
    story.append(Paragraph("Proven strategies from experienced Japan travelers", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    money_secrets = """
    <b>🛫 Flight Hacking:</b>
    • Book Tuesday-Thursday departures (saves £100-200)
    • Use 'Hidden City' tickets via Skiplagged.com
    • Set Google Flights alerts 3 months before travel
    • Consider split-city bookings (London-Amsterdam-Tokyo)
    
    <b>🏠 Accommodation Ninja Tactics:</b>
    • Airbnb monthly discounts (even for 1 week stays)
    • Book hotel directly after finding on Booking.com (ask for price match + perks)
    • Use HotelTonight for last-minute luxury upgrades
    • Consider 'love hotels' for unique, affordable stays
    
    <b>🍜 Food Budget Mastery:</b>
    • Convenience store gourmet: £2-4 per amazing meal
    • Lunch 'teishoku' sets: £4-8 for complete meals
    • Department store basement food courts: high quality, low prices
    • Happy hour sushi: 30-50% off at chain restaurants
    • Ramen 'omakase' (chef's choice): best value for money
    
    <b>🚌 Transport Optimization:</b>
    • JR Pass activation timing: maximize 14-day window
    • Overnight buses: save accommodation + transport costs
    • IC card bonuses: slight discounts on consecutive journeys
    • Airport express deals: book online for 20% savings
    • Local day passes: often cheaper than 3+ individual rides
    
    <b>🎫 Experience Upgrades for Less:</b>
    • Onsen day-passes: £8-15 for full relaxation
    • Temple stays: cultural immersion + meals for £30-40
    • Free walking tours: tip-based, excellent local insights
    • University cultural centers: free/cheap cultural programs
    • Seasonal festivals: free entertainment and food samples
    """
    story.append(Paragraph(money_secrets, body_style))
    story.append(PageBreak())
    
    # Booking strategy timeline
    story.append(Paragraph("📅 Strategic Booking Timeline", header_style))
    story.append(Paragraph("When to book what for maximum savings", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    timeline_data = [
        ['⏰ Timeline', '🎯 Action Items', '💰 Expected Savings', '🔗 Platforms'],
        ['NOW - 1 Week', 'Book international flights\nPurchase JR Pass', '£200-300', 'Skyscanner\nJRPass.com'],
        ['1-2 Months Before', 'Book all accommodations\nDomestic flights', '£150-250', 'Airbnb\nBooking.com'],
        ['3-4 Weeks Before', 'Activities & experiences\nRestaurant reservations', '£50-100', 'Klook\nOpenTable'],
        ['1-2 Weeks Before', 'Travel insurance\nMoney exchange', '£30-50', 'Compare sites\nWise.com'],
        ['Departure Week', 'Download offline maps\nPrint confirmations', '£0 (Peace of mind!)', 'Google Maps\nEmail']
    ]
    
    timeline_table = Table(timeline_data, colWidths=[1.2*inch, 1.8*inch, 1.2*inch, 1.3*inch])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), navy),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, navy),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, lightgrey]),
    ]))
    
    story.append(timeline_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Final call to action
    story.append(Paragraph("🌸 Your Japan Adventure Awaits 🌸", header_style))
    final_message = """
    This comprehensive guide provides everything you need for an unforgettable Japan experience within your £2,000 budget. 
    From the neon lights of Tokyo to the powder snow of Hokkaido, from ancient temples to friendly foxes - 
    your group of 12 will create memories that last a lifetime.
    
    <b>Ready to book? Start with international flights today!</b>
    The cherry blossom of preparation blooms into the magnificent flower of adventure. 
    
    頑張って！(Ganbatte! - Good luck!)
    """
    story.append(Paragraph(final_message, body_style))
    
    # Generate PDF
    doc.build(story)
    
    print(f"Beautiful Japanese-themed PDF generated: {filename}")
    return filename

if __name__ == "__main__":
    create_beautiful_japan_pdf()
