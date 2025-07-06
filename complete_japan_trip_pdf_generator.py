"""
Enhanced Japan Trip PDF Generator with Complete Chat Content
Generates a comprehensive PDF document with all chat content, complete itinerary, 
accommodation options, and detailed booking information
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, blue, gray, lightgrey, darkgrey
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

def create_complete_japan_trip_pdf():
    """Generate comprehensive Japan trip PDF with complete chat content"""
    
    # Create PDF document
    filename = "Japan_Trip_Complete_Chat_Guide.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=black
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=black
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=15,
        textColor=black
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_JUSTIFY
    )
    
    chat_style = ParagraphStyle(
        'ChatStyle',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=8,
        alignment=TA_LEFT,
        leftIndent=20
    )
    
    # Story content
    story = []
    
    # Title page
    story.append(Paragraph("Japan Adventure Planning Guide", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Complete Chat Summary & 14-Day Itinerary", heading_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Group of 12 Travelers | November 10-24, 2025", subheading_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Generated: July 6, 2025", body_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Table of contents
    story.append(Paragraph("Table of Contents", heading_style))
    toc_text = """
    1. Original Planning Discussion
    2. Complete 14-Day Itinerary
    3. Accommodation Options with Booking Links
    4. Cost Breakdown & Budget Analysis
    5. Transport & Logistics
    6. Money-Saving Tips & Recommendations
    7. Packing & Cultural Guidelines
    8. Group Voting & Decision Framework
    """
    story.append(Paragraph(toc_text, body_style))
    story.append(PageBreak())
    
    # Original planning discussion
    story.append(Paragraph("1. Original Planning Discussion", heading_style))
    
    story.append(Paragraph("Initial Request:", subheading_style))
    initial_request = """
    "Can you give me an itinerary for going to Japan in autumn so can experience Tokyo, Okinawa, Mount Fuji, 
    the snow up north for two weeks? Mix of Hotels and www.airbnb.com would be useful with suggestions and 
    other options to experience like the nodding dears, the foxes etc. Check various hotel websites as well 
    like booking.com and Expedia."
    """
    story.append(Paragraph(initial_request, chat_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Group Details Clarified:", subheading_style))
    group_details = """
    • Group size: 12 travelers from the UK
    • Budget: £2,000-£3,000 per person
    • Preferences: Food, culture, sightseeing, snowboarding
    • Transport: Open to domestic flights and bullet trains
    • Accommodation: Mix of hotels and Airbnbs
    • Special experiences: Nodding deer in Nara, fox village, skiing with good snow
    """
    story.append(Paragraph(group_details, body_style))
    story.append(PageBreak())
    
    # Complete itinerary
    story.append(Paragraph("2. Complete 14-Day Itinerary", heading_style))
    
    story.append(Paragraph("Optimal Travel Dates", subheading_style))
    dates_text = """
    <b>November 10-24, 2025</b> - This timing offers:
    • Peak autumn foliage in Tokyo, Kyoto, and Mt. Fuji region
    • Early ski season opening in Hokkaido with fresh powder
    • Comfortable temperatures for sightseeing
    • Fewer crowds compared to peak cherry blossom season
    """
    story.append(Paragraph(dates_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Detailed daily itinerary
    story.append(Paragraph("Day-by-Day Breakdown", subheading_style))
    
    itinerary_sections = [
        ("Days 1-3: Tokyo - Urban Culture & Cuisine", """
<b>Arrival & Setup (Day 1):</b>
• Land at Narita or Haneda Airport
• Take Airport Express to central Tokyo
• Check into group accommodation in Shinjuku area
• Evening: Gentle exploration of Shinjuku district, sample ramen and yakitori
• Get JR Pass and IC cards for local transport

<b>Classic Tokyo (Day 2):</b>
• Morning: Tsukiji Outer Market for fresh sushi breakfast
• Visit Senso-ji Temple in historic Asakusa district
• Afternoon: Modern Tokyo - Odaiba or teamLab Borderless digital art museum
• Evening: Shibuya Crossing experience, visit Hachiko statue
• Dinner: Izakaya (Japanese pub) experience in Shibuya or Shinjuku

<b>Culture & Views (Day 3):</b>
• Morning: Ueno Park and National Museum, or Imperial Palace East Gardens
• Afternoon: Harajuku fashion district and Takeshita Street
• Visit Meiji Shrine
• Optional: Tokyo Skytree or Tokyo Tower for city panoramas
• Evening: Explore Omotesando for upscale shopping and dining
        """),
        
        ("Days 4-5: Mt. Fuji Region - Autumn Foliage & Onsen", """
<b>Transit to Fuji (Day 4):</b>
• Morning: JR Fuji Excursion train from Shinjuku to Kawaguchiko (2 hours)
• Check into ryokan or hotel with Mt. Fuji views
• Afternoon: Lake Kawaguchi autumn leaves festival
• Evening: First onsen (hot spring) experience with mountain views

<b>Fuji Exploration (Day 5):</b>
• Morning: Mt. Tenjo Ropeway for panoramic Fuji views
• Visit Arakura Sengen Shrine and Chureito Pagoda (classic Fuji photo spot)
• Afternoon: Explore Kawaguchi or Hakone area
• Try local specialties: hōtō noodles, yaki-manjū sweets
• Evening: Onsen relaxation, kaiseki dinner at ryokan
        """),
        
        ("Days 6-7: Kyoto & Nara - Temples & Bowing Deer", """
<b>Kyoto Temples (Day 6):</b>
• Morning: Shinkansen from Mishima to Kyoto (2h 20m)
• Check into Kyoto accommodation
• Visit Kinkaku-ji (Golden Pavilion) and Ryoan-ji rock garden
• Afternoon: Arashiyama bamboo grove and Tenryu-ji temple
• Evening: Gion district for traditional architecture and dining
• Walk through Pontocho Alley for atmospheric dinner

<b>Nara Day Trip (Day 7):</b>
• Morning: Fushimi Inari Shrine - thousands of vermillion torii gates
• Afternoon: Train to Nara (30 minutes)
• Nara Park: Meet the famous bowing deer (over 1,000 deer roam freely)
• Visit Todai-ji Temple with giant bronze Buddha statue
• Deer feeding experience (they bow politely for treats!)
• Return to Kyoto for evening
        """),
        
        ("Days 8-9: Sendai & Zao Fox Village", """
<b>Travel to Sendai (Day 8):</b>
• Morning: Shinkansen from Kyoto to Sendai (4-5 hours with transfers)
• Check into Sendai accommodation
• Explore Sendai: Aoba Castle ruins, historic downtown
• Evening: Try famous Sendai beef tongue ramen

<b>Fox Village Experience (Day 9):</b>
• Morning: Local train to Shiroishi-Zao Station (45 minutes)
• Bus or taxi to Zao Fox Village
• Experience: Over 100 Japanese red foxes in semi-wild forest setting
• Unique opportunity to observe fox behavior up close
• Special feeding areas where gentle interaction is possible
• Return to Sendai for evening
        """),
        
        ("Days 10-11: Hokkaido - Powder Snow & Skiing", """
<b>Hokkaido Arrival (Day 10):</b>
• Morning: Fly Sendai to Sapporo (or via Tokyo)
• Travel to Niseko ski resort area
• Check into ski lodge or hotel
• Afternoon: Equipment rental, ski area orientation
• Evening: Sapporo specialties - miso ramen in Susukino district

<b>Ski Day (Day 11):</b>
• Full day skiing/snowboarding at Niseko or nearby resorts
• Experience Japan's famous powder snow
• Non-skiers: Onsen day at nearby hot springs (Noboribetsu)
• Evening: Sapporo Beer Museum or Odori Park
• Group dinner featuring Hokkaido specialties
        """),
        
        ("Days 12-14: Okinawa - Tropical Finale", """
<b>Okinawa Arrival (Day 12):</b>
• Morning: Fly Sapporo to Naha, Okinawa (3h 15m direct)
• Check into Naha accommodation or beach resort
• Afternoon: Shuri Castle (former Ryukyu Kingdom palace)
• Evening: Kokusai-dori street for shopping and unique Okinawan street food

<b>Island Culture (Day 13):</b>
• Morning: Ferry to Kerama Islands for pristine beaches (optional)
• Afternoon: Okinawan cultural experiences
• Try unique cuisine: goya champuru, rafute pork, soki soba
• Sample awamori (local spirit) and tropical fruits
• Beach time and relaxation

<b>Departure (Day 14):</b>
• Morning: Final souvenir shopping
• Afternoon: Fly Naha to Tokyo for international connections
• Evening: Depart for UK
        """)
    ]
    
    for section_title, content in itinerary_sections:
        story.append(Paragraph(section_title, subheading_style))
        story.append(Paragraph(content, body_style))
        story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # Accommodation options with detailed booking information
    story.append(Paragraph("3. Accommodation Options with Booking Links", heading_style))
    
    story.append(Paragraph("Booking Strategy for Groups", subheading_style))
    booking_strategy = """
    For a group of 12, we recommend a mix of:
    • Large Airbnb houses/apartments for social gathering and group meals
    • Multiple hotel rooms for privacy and amenities
    • Traditional ryokan experiences for cultural immersion
    • Book early as autumn is peak season in Japan
    """
    story.append(Paragraph(booking_strategy, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Detailed accommodation table
    story.append(Paragraph("Accommodation Options by Location", subheading_style))
    
    accommodation_data = [
        ['Location', 'Option', 'Type', 'Capacity', 'Price/Night', 'Booking Platform', 'Notes'],
        ['Tokyo\n(Nov 10-13)', 'A', 'Airbnb House', '12 guests', '¥18,000\n(£110)', 'airbnb.com', 'Shibuya line access'],
        ['', 'B', 'Hotel Suites', '4×3-bed suites', '¥12,000/person', 'booking.com', 'Ueno area, breakfast included'],
        ['Mt. Fuji\n(Nov 13-15)', 'A', 'Villa Rental', '12 guests', '¥20,000', 'vrbo.com', 'Lake Kawaguchi views'],
        ['', 'B', 'Ryokan', '4×3-person rooms', '¥18,000/room', 'booking.com', 'Traditional onsen experience'],
        ['Kyoto/Nara\n(Nov 15-17)', 'A', 'Traditional Ryokan', 'Multiple rooms', '¥20,000/room', 'booking.com', 'Nara Park area'],
        ['', 'B', 'Hotel Rooms', '4-6 standard rooms', '¥12,000/room', 'expedia.com', 'Central Kyoto location'],
        ['Sendai\n(Nov 17-19)', 'A', 'Hotel Rooms', '4×triple rooms', '¥12,000/room', 'booking.com', 'Near station'],
        ['', 'B', 'Business Hotel', '6×twin rooms', '¥13,000/room', 'japanican.com', 'Downtown location'],
        ['Hokkaido\n(Nov 19-21)', 'A', 'Ski Chalet', '12 guests', '¥200,000', 'niseko.com', 'Ski-in/ski-out'],
        ['', 'B', 'Resort Hotel', '3×4-person rooms', '¥60,000/room', 'booking.com', 'Annupuri resort'],
        ['Okinawa\n(Nov 21-24)', 'A', 'Beach Villa', '12 guests', '¥20,000', 'vrbo.com', 'Private beach access'],
        ['', 'B', 'City Hotel', '6×twin rooms', '¥12,000/room', 'agoda.com', 'Naha monorail access'],
        ['', 'C', 'Resort Hotel', '4×triple rooms', '¥15,000/room', 'expedia.com', 'Beachfront location']
    ]
    
    accommodation_table = Table(accommodation_data, colWidths=[1*inch, 0.3*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.2*inch])
    accommodation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), gray),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
    ]))
    
    story.append(accommodation_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Specific booking links section
    story.append(Paragraph("Recommended Booking Links (for Nov 10-24, 2025)", subheading_style))
    booking_links = """
    <b>Tokyo Options:</b>
    • Airbnb: Search "Tokyo Shibuya large group" - filter for 12+ guests
    • Booking.com: "Randor Residence Tokyo Suites" - family accommodations
    • Expedia: "Tokyo Bay area hotels" - multiple room bookings
    
    <b>Mt. Fuji Options:</b>
    • VRBO: "Villa Yawaragi Kawaguchiko" - mountain view villa
    • Booking.com: "Fujikawaguchiko Resort Hotel" - traditional ryokan
    • Japanican.com: "Hakone onsen hotels" - authentic experience
    
    <b>Kyoto/Nara Options:</b>
    • Booking.com: "Nara Hotel" - historic luxury near deer park
    • Agoda: "Kyoto central hotels" - temple district access
    • Airbnb: "Kyoto traditional house" - cultural immersion
    
    <b>Sendai Options:</b>
    • Booking.com: "Hotel Metropolitan Sendai East" - station access
    • Expedia: "Sendai business hotels" - group bookings
    
    <b>Hokkaido Options:</b>
    • Niseko.com: "Yukisugi Chalet" - luxury ski accommodation
    • Booking.com: "Niseko Northern Resort" - ski-in/ski-out
    • Powderlife.com: "Hokkaido ski lodges" - group packages
    
    <b>Okinawa Options:</b>
    • VRBO: "Grandioso Villa Kin" - beachfront villa
    • Booking.com: "Hotel Collective Naha" - city center
    • Expedia: "Rihga Royal Gran Okinawa" - monorail connected
    """
    story.append(Paragraph(booking_links, body_style))
    story.append(PageBreak())
    
    # Cost breakdown section
    story.append(Paragraph("4. Detailed Cost Breakdown & Budget Analysis", heading_style))
    
    story.append(Paragraph("Cost Per Person Summary", subheading_style))
    
    cost_summary_data = [
        ['Expense Category', 'Budget Option', 'Comfortable Option', 'Luxury Option'],
        ['International Flights (UK-Tokyo)', '£480-£550', '£800-£1,000', '£1,200-£1,500'],
        ['Domestic Flights (2 flights)', '£100', '£240', '£400'],
        ['JR Rail Pass (14-day)', '£426', '£586 (Green)', '£586 (Green)'],
        ['Accommodation (14 nights)', '£700', '£1,190', '£1,800'],
        ['Meals (3 per day)', '£250-£350', '£420-£500', '£600-£800'],
        ['Local Transport', '£50', '£100-£125', '£200'],
        ['Activities & Sightseeing', '£30', '£90-£120', '£200-£300'],
        ['Skiing (2 days)', '£150', '£180', '£250'],
        ['Souvenirs & Extras', '£100', '£200', '£400'],
        ['TOTAL PER PERSON', '£2,106-£2,356', '£3,006-£3,411', '£4,436-£5,236']
    ]
    
    cost_table = Table(cost_summary_data, colWidths=[1.5*inch, 1.2*inch, 1.2*inch, 1.2*inch])
    cost_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), lightgrey),
        ('BACKGROUND', (0, -1), (-1, -1), lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, -1), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -2), 9),
    ]))
    
    story.append(cost_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Budget recommendations
    story.append(Paragraph("Budget Recommendations", subheading_style))
    budget_recs = """
    <b>For £2,000-£3,000 per person budget:</b>
    • Target the "Comfortable Option" column above
    • Book flights 2-3 months in advance for better prices
    • Mix Airbnb (for group bonding) with mid-range hotels
    • Use JR Pass efficiently for all train travel
    • Balance street food with nice restaurant experiences
    • Book ski equipment rentals in advance for better rates
    
    <b>Money-saving strategies:</b>
    • Fly mid-week and avoid peak travel days
    • Share large Airbnb accommodations when possible
    • Use convenience stores for breakfast and snacks
    • Take advantage of free attractions (temples, parks, shrines)
    • Buy alcohol at supermarkets rather than restaurants
    • Use day passes for local transport in each city
    """
    story.append(Paragraph(budget_recs, body_style))
    story.append(PageBreak())
    
    # Transport and logistics
    story.append(Paragraph("5. Transport & Logistics", heading_style))
    
    transport_sections = [
        ("JR Rail Pass Strategy", """
A 14-day JR Pass (£426 ordinary, £586 Green) covers nearly all train travel between cities.
Must be purchased before arriving in Japan. Activate on your first travel day.

<b>Covered routes:</b>
• Tokyo to Mt. Fuji area (JR lines)
• Mt. Fuji to Kyoto (Shinkansen)
• Kyoto to Sendai (Shinkansen)
• All local JR lines in cities

<b>Not covered:</b>
• Fujikyu Railway to Kawaguchiko (pay separately ~¥1,140)
• Private railways in some areas
• Domestic flights
        """),
        
        ("Domestic Flight Strategy", """
<b>Required flights for this itinerary:</b>
• Sendai to Sapporo (or Tokyo to Sapporo)
• Sapporo to Okinawa
• Okinawa to Tokyo (for departure)

<b>Booking tips:</b>
• Use budget airlines: Peach, Jetstar, Skymark
• Book early for group discounts
• Consider baggage allowances for ski equipment
• Major airlines (ANA, JAL) offer more flexibility
        """),
        
        ("Local Transport in Each City", """
<b>Tokyo:</b> IC card (Suica/Pasmo) for subway and JR lines
<b>Mt. Fuji:</b> Local buses around lakes, some walking
<b>Kyoto:</b> City bus day passes, some walking in temple areas
<b>Sendai:</b> Local trains to Fox Village, city buses
<b>Hokkaido:</b> Resort shuttles, rental car option for flexibility
<b>Okinawa:</b> Monorail in Naha, buses to beaches, car rental recommended
        """)
    ]
    
    for section_title, content in transport_sections:
        story.append(Paragraph(section_title, subheading_style))
        story.append(Paragraph(content, body_style))
        story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # Group coordination and voting
    story.append(Paragraph("6. Group Voting & Decision Framework", heading_style))
    
    voting_text = """
    <b>Accommodation Voting Process:</b>
    1. Review accommodation options for each location
    2. Each person votes for their preferred option (A, B, or C)
    3. Consider factors: price, location, amenities, group vs. individual space
    4. Majority rule, with consideration for budget constraints
    5. Book immediately after decision to secure availability
    
    <b>Activity Preferences:</b>
    • Skiing: Confirm who wants to ski vs. other activities
    • Onsen: Comfortable level with traditional bathing
    • Cultural sites: Must-see vs. optional experiences
    • Food: Dietary restrictions and adventure level
    
    <b>Budget Coordination:</b>
    • Set group budget ceiling per person
    • Decide on shared expenses (group dinners, transport)
    • Individual vs. group booking for accommodations
    • Emergency fund for unexpected expenses
    """
    story.append(Paragraph(voting_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Voting table template
    story.append(Paragraph("Accommodation Voting Template", subheading_style))
    
    voting_data = [
        ['Location', 'Option A', 'Option B', 'Option C', 'Your Vote', 'Comments'],
        ['Tokyo', 'Airbnb House', 'Hotel Suites', '-', '☐', ''],
        ['Mt. Fuji', 'Villa Rental', 'Ryokan', '-', '☐', ''],
        ['Kyoto/Nara', 'Traditional Ryokan', 'Hotel Split', '-', '☐', ''],
        ['Sendai', 'Hotel Rooms', 'Business Hotel', '-', '☐', ''],
        ['Hokkaido', 'Ski Chalet', 'Resort Hotel', '-', '☐', ''],
        ['Okinawa', 'Beach Villa', 'City Hotel', 'Resort Hotel', '☐', '']
    ]
    
    voting_table = Table(voting_data, colWidths=[1*inch, 1*inch, 1*inch, 1*inch, 0.6*inch, 1.4*inch])
    voting_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(voting_table)
    story.append(PageBreak())
    
    # Final recommendations and next steps
    story.append(Paragraph("7. Final Recommendations & Next Steps", heading_style))
    
    final_recs = """
    <b>Immediate Actions (within 1 week):</b>
    1. Confirm travel dates with all group members
    2. Book international flights (prices increase closer to travel)
    3. Purchase JR Rail Passes (must be done before arrival)
    4. Set up group chat for coordination
    5. Start accommodation voting process
    
    <b>Medium-term Actions (1-2 months before):</b>
    1. Book all accommodations based on group votes
    2. Purchase travel insurance for all group members
    3. Book domestic flights within Japan
    4. Research and book special activities (ski lessons, cultural tours)
    5. Plan group meals and restaurant reservations
    
    <b>Pre-departure Actions (2 weeks before):</b>
    1. Confirm all bookings and print confirmations
    2. Check passport validity (6+ months remaining)
    3. Download offline maps and translation apps
    4. Pack according to weather forecasts
    5. Exchange currency or arrange international cards
    
    <b>Cultural Preparation:</b>
    • Learn basic Japanese phrases (arigatou, sumimasen, konnichiwa)
    • Understand bowing etiquette and shoe removal customs
    • Research onsen etiquette if planning to use hot springs
    • Download Google Translate app with camera feature
    • Understand tipping culture (generally not expected in Japan)
    """
    story.append(Paragraph(final_recs, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Emergency contacts and resources
    story.append(Paragraph("Emergency Contacts & Resources", subheading_style))
    
    emergency_info = """
    <b>Important Contacts:</b>
    • UK Embassy Tokyo: +81-3-5211-1100
    • Japan Emergency Services: 110 (police), 119 (fire/ambulance)
    • Tourist Hotline: 050-3816-2787 (24/7, English support)
    
    <b>Useful Apps:</b>
    • Google Translate (with camera feature)
    • Hyperdia (train schedules)
    • Suica/Pasmo (IC card management)
    • Tabelog (restaurant reviews)
    • Weather news (local forecasts)
    
    <b>Money & Cards:</b>
    • Japan is still largely cash-based
    • 7-Eleven ATMs accept international cards
    • Notify banks of travel dates
    • Consider travel money cards for better exchange rates
    """
    story.append(Paragraph(emergency_info, body_style))
    
    # Generate PDF
    doc.build(story)
    
    print(f"Complete PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_complete_japan_trip_pdf()
