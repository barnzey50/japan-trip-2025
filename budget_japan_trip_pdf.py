"""
Budget-Optimized Japan Trip PDF Generator - £2,000 Target
Creates a comprehensive PDF with budget-focused accommodation options
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, red, darkred, lightgrey, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics import renderPDF
import os

def create_budget_japan_trip_pdf():
    """Generate budget-focused Japan trip PDF with Japanese theme"""
    
    filename = "Japan_Trip_Budget_Guide_2000.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=50, leftMargin=50,
                          topMargin=60, bottomMargin=40)
    
    styles = getSampleStyleSheet()
    
    # Japanese-inspired custom styles
    title_style = ParagraphStyle(
        'JapaneseTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=darkred,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'JapaneseSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=red,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'JapaneseHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=darkred,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'JapaneseSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=15,
        textColor=red,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'JapaneseBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        textColor=black
    )
    
    story = []
    
    # Japanese-themed title page
    story.append(Paragraph("🌸 日本の旅 - Japan Adventure 🌸", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("14-Day Autumn Journey", subtitle_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Budget Guide: £2,000 per person", subheading_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("November 10-24, 2025 | Group of 12", body_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Add decorative elements
    story.append(Paragraph("🏔️ 富士山 Mt. Fuji | 🦌 奈良 Nara Deer | 🦊 Fox Village | 🎿 Hokkaido Snow | 🏝️ Okinawa", body_style))
    story.append(PageBreak())
    
    # Budget breakdown - £2,000 target
    story.append(Paragraph("💰 Budget Breakdown - £2,000 Target", heading_style))
    
    budget_data = [
        ['Expense', 'Budget Option', 'Cost per Person', 'Total for 12', 'Booking Source'],
        ['International Flights', 'Economy, advance booking', '£450', '£5,400', 'Skyscanner/Expedia'],
        ['Domestic Flights', 'Budget airlines (Peach/Jetstar)', '£80', '£960', 'Skyscanner Japan'],
        ['JR Rail Pass', '14-day Ordinary', '£426', '£5,112', 'JR Pass.com'],
        ['Accommodation', 'Mix Airbnb/Budget Hotels', '£600', '£7,200', 'Airbnb/Booking.com'],
        ['Meals', 'Convenience stores + casual dining', '£280', '£3,360', 'Local restaurants'],
        ['Local Transport', 'IC cards + day passes', '£45', '£540', 'Station counters'],
        ['Activities', 'Free attractions + onsen', '£75', '£900', 'Local booking'],
        ['Ski Day', 'Equipment rental + lift', '£44', '£528', 'Resort booking'],
        ['TOTAL', '', '£2,000', '£24,000', '']
    ]
    
    budget_table = Table(budget_data, colWidths=[1.2*inch, 1.5*inch, 1*inch, 1*inch, 1.3*inch])
    budget_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, -1), (-1, -1), lightgrey),
        ('TEXTCOLOR', (0, -1), (-1, -1), darkred),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, -1), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -2), 9),
    ]))
    
    story.append(budget_table)
    story.append(PageBreak())
    
    # Budget accommodation options
    story.append(Paragraph("🏠 Budget Accommodation Options", heading_style))
    
    # Tokyo options
    story.append(Paragraph("🗼 Tokyo (3 nights) - Nov 10-13", subheading_style))
    tokyo_options = """
    <b>Option A - Airbnb Group House (Recommended)</b>
    • Large house in Shibuya/Shinjuku area for 12 people
    • Cost: £90/night total (£7.50 per person per night)
    • Book via: Airbnb.com - Search "Tokyo large group house 12 guests"
    • Benefits: Kitchen for group meals, social space, cultural experience
    
    <b>Option B - Budget Hotel Rooms</b>
    • 6 twin rooms at business hotel (2 people per room)
    • Cost: £25/night per person (£300 total per night)
    • Book via: Booking.com - "Tokyo Station Hotel" or "Capsule Hotel chains"
    • Benefits: Individual privacy, breakfast included, central location
    
    <b>Option C - Mixed Accommodation</b>
    • 4 people in Airbnb + 8 people in nearby budget hotel
    • Cost: £20/night per person average
    • Book via: Combination of Airbnb.com and Expedia
    • Benefits: Flexibility for different preferences
    """
    story.append(Paragraph(tokyo_options, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Mt. Fuji options
    story.append(Paragraph("🏔️ Mt. Fuji Area (2 nights) - Nov 13-15", subheading_style))
    fuji_options = """
    <b>Option A - Kawaguchiko Group Villa</b>
    • Traditional Japanese house with Mt. Fuji views
    • Cost: £120/night total (£10 per person per night)
    • Book via: Airbnb.com - Search "Kawaguchiko villa 12 guests mountain view"
    • Benefits: Authentic experience, group cooking, stunning views
    
    <b>Option B - Budget Ryokan</b>
    • Traditional inn with shared facilities
    • Cost: £35/night per person (including breakfast)
    • Book via: Booking.com - "Kawaguchiko budget ryokan"
    • Benefits: Traditional experience, onsen access, meals included
    
    <b>Option C - Hostel-style Accommodation</b>
    • Mixed dormitory and private rooms
    • Cost: £25/night per person
    • Book via: Expedia - "Fuji Five Lakes hostels"
    • Benefits: Meet other travelers, lowest cost option
    """
    story.append(Paragraph(fuji_options, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Kyoto/Nara options
    story.append(Paragraph("🏯 Kyoto/Nara (2 nights) - Nov 15-17", subheading_style))
    kyoto_options = """
    <b>Option A - Traditional Machiya House</b>
    • Restored traditional wooden house in Gion district
    • Cost: £140/night total (£11.67 per person per night)
    • Book via: Airbnb.com - Search "Kyoto traditional house 12 guests Gion"
    • Benefits: Cultural immersion, perfect location, group space
    
    <b>Option B - Budget Temple Lodging</b>
    • Stay at Buddhist temple with vegetarian meals
    • Cost: £30/night per person (including meals)
    • Book via: Booking.com - "Kyoto temple lodging shukubo"
    • Benefits: Unique cultural experience, meditation sessions
    
    <b>Option C - Kyoto Guest House</b>
    • Modern guest house with shared facilities
    • Cost: £28/night per person
    • Book via: Expedia - "Kyoto downtown guest houses"
    • Benefits: Social atmosphere, central location
    """
    story.append(Paragraph(kyoto_options, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Sendai options
    story.append(Paragraph("🦊 Sendai (2 nights) - Nov 17-19", subheading_style))
    sendai_options = """
    <b>Option A - Business Hotel Group Booking</b>
    • 6 twin rooms at business hotel near station
    • Cost: £22/night per person
    • Book via: Booking.com - "Sendai Station business hotels"
    • Benefits: Convenient for Fox Village day trip, reliable
    
    <b>Option B - Sendai Guest House</b>
    • Large guest house with group accommodation
    • Cost: £18/night per person
    • Book via: Airbnb.com - Search "Sendai group accommodation"
    • Benefits: Lowest cost, local area experience
    
    <b>Option C - Hot Spring Resort</b>
    • Budget onsen resort outside city
    • Cost: £35/night per person (including dinner)
    • Book via: Expedia - "Sendai onsen budget resorts"
    • Benefits: Relaxing hot springs, traditional meals
    """
    story.append(Paragraph(sendai_options, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Hokkaido options
    story.append(Paragraph("🎿 Hokkaido (2 nights) - Nov 19-21", subheading_style))
    hokkaido_options = """
    <b>Option A - Ski Lodge Dormitory</b>
    • Shared accommodation at ski resort
    • Cost: £40/night per person
    • Book via: Booking.com - "Niseko budget ski lodges"
    • Benefits: Ski-in/ski-out, meet other skiers, equipment storage
    
    <b>Option B - Sapporo Budget Hotel</b>
    • Stay in Sapporo city, day trips to ski areas
    • Cost: £25/night per person
    • Book via: Expedia - "Sapporo budget hotels"
    • Benefits: City nightlife, food scene, cheaper accommodation
    
    <b>Option C - Group Chalet</b>
    • Rent entire chalet for group
    • Cost: £50/night per person
    • Book via: Airbnb.com - "Niseko group chalet 12 people"
    • Benefits: Group bonding, cooking facilities, privacy
    """
    story.append(Paragraph(hokkaido_options, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Okinawa options
    story.append(Paragraph("🏝️ Okinawa (3 nights) - Nov 21-24", subheading_style))
    okinawa_options = """
    <b>Option A - Beach House Rental</b>
    • Entire house near beach for group
    • Cost: £100/night total (£8.33 per person per night)
    • Book via: Airbnb.com - Search "Okinawa beach house 12 guests"
    • Benefits: Beach access, group cooking, relaxing end to trip
    
    <b>Option B - Naha City Guest House</b>
    • Central location in Naha with shared facilities
    • Cost: £20/night per person
    • Book via: Booking.com - "Naha budget accommodations"
    • Benefits: Easy airport access, explore local culture
    
    <b>Option C - Resort Hotel Group Booking</b>
    • Budget resort with group discounts
    • Cost: £35/night per person
    • Book via: Expedia - "Okinawa budget resorts"
    • Benefits: Resort amenities, organized activities
    """
    story.append(Paragraph(okinawa_options, body_style))
    story.append(PageBreak())
    
    # Money-saving strategies
    story.append(Paragraph("💡 Money-Saving Strategies", heading_style))
    
    money_saving = """
    <b>🛫 Flights:</b>
    • Book 2-3 months in advance for best prices
    • Use flight comparison sites: Skyscanner, Momondo, Google Flights
    • Consider flying Tuesday/Wednesday for lower fares
    • Pack light to avoid baggage fees on domestic flights
    
    <b>🏠 Accommodation:</b>
    • Book Airbnb for longer stays (3+ nights) for better rates
    • Use Booking.com for last-minute hotel deals
    • Consider staying slightly outside city centers
    • Book directly with hotels for potential upgrades
    
    <b>🍜 Food:</b>
    • Convenience store meals: £2-4 per meal
    • Ramen shops: £4-6 per bowl
    • Conveyor belt sushi: £8-12 per meal
    • Cook group meals in Airbnb kitchens
    • Look for lunch sets (teishoku) for better value
    
    <b>🚌 Transport:</b>
    • Use IC cards (Suica/Pasmo) for small savings
    • Buy day passes for local transport
    • Walk when possible - great for sightseeing
    • Use overnight buses for longer distances (saves on accommodation)
    
    <b>🎫 Activities:</b>
    • Many temples and shrines are free
    • City parks and gardens often have no entrance fee
    • Free walking tours in major cities
    • Happy hour discounts at many attractions
    """
    story.append(Paragraph(money_saving, body_style))
    story.append(PageBreak())
    
    # Booking timeline and links
    story.append(Paragraph("📅 Booking Timeline & Links", heading_style))
    
    booking_timeline = """
    <b>Immediate (Now - 1 week):</b>
    • Book international flights: Expedia.com, Skyscanner.com
    • Purchase JR Rail Pass: JRPass.com
    • Set up group decision-making process
    
    <b>2-3 months before (August-September):</b>
    • Book accommodations based on group votes
    • Book domestic flights: Peach.com, Jetstar.com
    • Purchase travel insurance
    
    <b>1 month before (October):</b>
    • Confirm all bookings
    • Download essential apps
    • Start learning basic Japanese phrases
    
    <b>Key Booking Websites:</b>
    • Airbnb.com - Group houses and unique stays
    • Booking.com - Hotels with free cancellation
    • Expedia.com - Package deals and group bookings
    • Agoda.com - Asia-focused hotel booking
    • Skyscanner.com - Flight comparisons
    • JRPass.com - Rail pass purchase
    """
    story.append(Paragraph(booking_timeline, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Final budget summary
    story.append(Paragraph("💰 Final Budget Summary", subheading_style))
    final_budget = """
    <b>Target: £2,000 per person achieved by:</b>
    • Choosing budget accommodation options (averaging £20-30/night)
    • Mixing Airbnb group houses with budget hotels
    • Using convenience stores and casual dining
    • Booking flights well in advance
    • Maximizing JR Pass value
    • Focusing on free and low-cost activities
    
    <b>Contingency fund: £200 per person recommended</b>
    • For unexpected expenses, souvenirs, and treats
    • Emergency accommodation or transport changes
    • Special meals or experiences not in base budget
    """
    story.append(Paragraph(final_budget, body_style))
    
    # Generate PDF
    doc.build(story)
    
    print(f"Budget PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_budget_japan_trip_pdf()
