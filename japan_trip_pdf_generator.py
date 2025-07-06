"""
Japan Trip PDF Generator
Generates a comprehensive PDF document with complete itinerary, accommodation options, and cost estimates
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, blue, gray, lightgrey
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

def create_japan_trip_pdf():
    """Generate comprehensive Japan trip PDF document"""
    
    # Create PDF document
    filename = "Japan_Trip_Complete_Guide.pdf"
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
    
    # Story content
    story = []
    
    # Title page
    story.append(Paragraph("14-Day Japan Autumn Adventure", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Complete Trip Guide for Group of 12", heading_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("November 10-24, 2025", subheading_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Trip overview
    story.append(Paragraph("Trip Overview", heading_style))
    overview_text = """
    This comprehensive guide covers your 14-day autumn adventure through Japan, including:
    • Tokyo city culture and cuisine
    • Mt. Fuji and traditional onsen experiences
    • Kyoto temples and Nara's bowing deer
    • Sendai and the famous Fox Village
    • Hokkaido skiing and powder snow
    • Okinawa tropical finale
    • Complete accommodation options with booking links
    • Detailed cost estimates per person
    """
    story.append(Paragraph(overview_text, body_style))
    story.append(PageBreak())
    
    # Detailed itinerary
    story.append(Paragraph("Detailed 14-Day Itinerary", heading_style))
    
    # Days 1-3: Tokyo
    story.append(Paragraph("Days 1-3: Tokyo - City Culture & Cuisine", subheading_style))
    tokyo_text = """
    <b>Arrive Tokyo:</b> Land at Narita or Haneda. Check into group-friendly lodging in central Tokyo.
    
    <b>Day 1:</b> Recover from jetlag with an easy stroll. Explore Shinjuku Gyoen or Meiji Shrine, and view the neon cityscape from Shinjuku or Roppongi. Sample Japanese comfort food (ramen, yakitori).
    
    <b>Day 2:</b> Hit classic spots – Tsukiji/Toyosu Market for sushi breakfast, historic Asakusa (Senso-ji temple), then modern Odaiba or teamLab Borderless for tech-art. In the evening, wander the Shibuya Crossing and Hachiko statue, and try izakaya (pub) dining.
    
    <b>Day 3:</b> Morning in Ueno Park/museums or Imperial Palace gardens. Afternoon in Harajuku/Takeshita street (young fashion) and Omotesando. Optional: Tokyo Skytree or Tokyo Tower for panoramas.
    
    <b>Notes:</b> Tokyo has endless food and shopping. Public transit is excellent (JR+subway).
    """
    story.append(Paragraph(tokyo_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Days 4-5: Mt. Fuji
    story.append(Paragraph("Days 4-5: Hakone / Mt. Fuji (Fuji Five Lakes)", subheading_style))
    fuji_text = """
    <b>Transit:</b> Take the JR Fuji Excursion train from Shinjuku direct to Kawaguchiko (~2h), or take the Shinkansen to Mishima/Otsuki and transfer to the local Fujikyu line to Kawaguchiko.
    
    <b>Fuji Highlights:</b> Stay near Lake Kawaguchi or Hakone. Enjoy the autumn leaves festival (late Oct–Nov) around Lake Kawaguchi. On clear days the lake gives a perfect mirror image of Mt. Fuji. Ride the Mt. Tenjō ropeway for panoramic Fuji views. Relax in an onsen overlooking the mountain. Visit Arakura Sengen's Chūreitō Pagoda (classic pagoda + Fuji view).
    
    <b>Cuisine & Onsen:</b> Try local hōtō noodles or yaki-manjū sweet. Book a ryokan/onsen hotel. Autumn days are cool (15–20°C) but mornings/evenings can be ~5–10°C, so pack layers.
    """
    story.append(Paragraph(fuji_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Days 6-7: Kyoto/Nara
    story.append(Paragraph("Days 6-7: Kyoto – Temples & Tradition (with Nara Deer)", subheading_style))
    kyoto_text = """
    <b>Transit:</b> Shinkansen from Mishima/Kawaguchiko to Kyoto (~2h20). Check into Kyoto city hotel or house.
    
    <b>Day 6 (Kyoto):</b> Visit Kinkaku-ji (Golden Pavilion) and Ryoan-ji garden, then head west to Arashiyama: stroll the bamboo grove, see Tenryu-ji temple, and the Katsura River. In evening, wander Gion's lantern-lit lanes and Pontocho alley for dinner.
    
    <b>Day 7 (Kyoto/Nara):</b> Morning in Fushimi Inari Taisha (thousands of torii gates). Afternoon take the JR Nara Line (~30m) to Nara. In Nara Park hundreds of friendly bowing ("nodding") deer roam – they will gently bow for treats. Don't miss Tōdai-ji's giant Buddha.
    """
    story.append(Paragraph(kyoto_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Days 8-9: Fox Village
    story.append(Paragraph("Days 8-9: Tōhoku – Fox Village & Nature (Sendai/Shiroishi)", subheading_style))
    fox_text = """
    <b>Transit:</b> Bullet train from Kyoto to Sendai (~4–5h, with one transfer). Stay in Sendai or nearby.
    
    <b>Foxes at Zao:</b> Take the local train from Sendai to Shiroishi-Zao Station (45m) and then a short bus or taxi to Zao Fox Village. Zao Fox Village (Miyagi Prefecture) is a one-of-a-kind forest inhabited by foxes. Over a hundred Japanese red foxes live here in semi-wild conditions. Visitors can wander the enclosed forest, watch foxes lazing on rocks, and even feed or (on weekends/holidays) gently hold them in a special zone.
    
    <b>Return/Stay:</b> After Fox Village, return to Sendai. You might explore Sendai (Aoba Castle ruins, famous beef tongue ramen) or head onward to Hokkaido.
    """
    story.append(Paragraph(fox_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Days 10-11: Hokkaido
    story.append(Paragraph("Days 10-11: Hokkaido – Skiing & Snow (Sapporo/Niseko)", subheading_style))
    hokkaido_text = """
    <b>Transit:</b> Fly Sendai→Sapporo (New Chitose Airport) or Sendai→Tokyo→Sapporo.
    
    <b>Snow Adventures:</b> Spend 2 days skiing/snowboarding at Hokkaido's famous powder resorts (e.g. Niseko, Rusutsu, Sapporo Kokusai). Japan is famed for very dry, deep snow. By late November many northern resorts open and have "aspirin-like" powder. Even if a bit early, Hokkaido nights get cold, so expect good conditions on the slopes.
    
    <b>Sapporo City:</b> In the evening sample Sapporo's specialties: try miso-based ramen in the lively Susukino district (Ramen Alley). Visit the Sapporo Beer Museum or Odori Park. Stay in Sapporo or resort town.
    """
    story.append(Paragraph(hokkaido_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Days 12-14: Okinawa
    story.append(Paragraph("Days 12-14: Okinawa – Tropical Finale (Naha/Kokusai-dōri)", subheading_style))
    okinawa_text = """
    <b>Transit:</b> Fly Sapporo→Naha (direct flights ~3h15) or Sapporo→Tokyo→Naha (~5–6h total).
    
    <b>Okinawa Main Island:</b> Base in Naha or a resort area. Explore Shurijō Castle (Ryukyu Kingdom), stroll Kokusaidō shopping street, and sample tropical street food (taco rice, beni-imo sweets). For beaches, ferry to the Kerama or Tokashiki islands (30–60m boat).
    
    <b>Cuisine:</b> Okinawa cuisine is unique. Try goya champuru (stir-fried bitter melon with tofu and pork) and rafute (sweet-simmered Okinawan pork). Don't miss local sōki soba (ryukyuan noodles with pork ribs) and awamori liquor. Tropical fruits (pineapple, mango) are abundant.
    
    <b>Departure:</b> On Day 15 fly Naha→Tokyo (~2.5h) for your international flight home.
    """
    story.append(Paragraph(okinawa_text, body_style))
    story.append(PageBreak())
    
    # Accommodation options
    story.append(Paragraph("Accommodation Options with Booking Links", heading_style))
    
    # Create accommodation table
    accommodation_data = [
        ['Location', 'Option', 'Type', 'Sleeps', 'Price/Night', 'Booking Link'],
        ['Tokyo\n(Nov 10-13)', 'A', 'Airbnb House', '12', '¥18,000 (£110)', 'airbnb.com/rooms/tokyo-shibuya'],
        ['', 'B', 'Hotel Suites', '12', '¥12,000/person', 'booking.com/randor-residence-tokyo'],
        ['Mt. Fuji\n(Nov 13-15)', 'A', 'Villa Rental', '12', '¥20,000', 'vrbo.com/villa-yawaragi-kawaguchiko'],
        ['', 'B', 'Hotel Rooms', '4/room', '¥18,000/room', 'booking.com/fujikawaguchiko-resort'],
        ['Kyoto/Nara\n(Nov 15-17)', 'A', 'Ryokan', 'Multiple rooms', '¥20,000/room', 'booking.com/nara-hotel'],
        ['', 'B', 'Hotel Split', '4-6 rooms', '¥12,000/room', 'booking.com/kyoto-central'],
        ['Sendai\n(Nov 17-19)', 'A', 'Hotel Rooms', '4×triple/twin', '¥12,000/room', 'booking.com/metropolitan-sendai'],
        ['', 'B', 'Downtown Hotel', 'Multiple rooms', '¥13,000/room', 'expedia.com/sendai-downtown'],
        ['Hokkaido\n(Nov 19-21)', 'A', 'Luxury Chalet', '12', '¥200,000', 'niseko.com/yukisugi-chalet'],
        ['', 'B', 'Ski Hotel', '3×rooms', '¥60,000/room', 'booking.com/niseko-northern-resort'],
        ['Okinawa\n(Nov 21-24)', 'A', 'Beach Villa', '12', '¥20,000', 'vrbo.com/grandioso-villa-kin'],
        ['', 'B', 'City Hotel', 'Multiple rooms', '¥12,000/room', 'booking.com/hotel-collective-naha'],
        ['', 'C', 'Luxury Hotel', 'Multiple rooms', '¥15,000/room', 'expedia.com/rihga-royal-gran-okinawa']
    ]
    
    accommodation_table = Table(accommodation_data, colWidths=[1.2*inch, 0.4*inch, 1*inch, 0.8*inch, 1*inch, 2*inch])
    accommodation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), gray),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(accommodation_table)
    story.append(PageBreak())
    
    # Cost estimates
    story.append(Paragraph("Cost Estimates Per Person", heading_style))
    
    cost_breakdown = """
    <b>International Flights (UK–Tokyo round-trip):</b>
    • Budget: £480–£550 (book early, mid-week flights)
    • Comfortable: £800–£1,000 (peak pricing or flexible tickets)
    
    <b>Domestic Flights (within Japan):</b>
    • Budget: £100 total (2 flights with low-cost carriers)
    • Comfortable: £240 total (premium airlines or last-minute booking)
    
    <b>JR Rail Pass (14-day):</b>
    • Ordinary Pass: £426 (covers almost all Shinkansen and JR trains)
    • Green Pass (first-class): £586 (larger seats and lounges)
    
    <b>Accommodation (14 nights):</b>
    • Budget: £700 total (£50/night, sharing rooms/Airbnbs)
    • Comfortable: £1,190 total (£85/night, mid-range hotels)
    
    <b>Meals (3 per day):</b>
    • Budget: £250–£350 (convenience stores, casual restaurants)
    • Comfortable: £420–£500 (mid-range restaurants, some fine dining)
    
    <b>Local Transport:</b>
    • Budget: £50 (metro/bus passes, occasional taxis)
    • Comfortable: £100–£125 (more taxis, premium transport)
    
    <b>Activities & Sightseeing:</b>
    • Budget: £30 (mostly free attractions)
    • Comfortable: £90–£120 (paid activities, onsen visits, ski day)
    """
    story.append(Paragraph(cost_breakdown, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Total cost summary
    story.append(Paragraph("Total Cost Summary", subheading_style))
    
    cost_summary_data = [
        ['Budget Level', 'Low-end Budget', 'High-end Comfortable'],
        ['International Flights', '£500', '£800'],
        ['Domestic Flights', '£100', '£240'],
        ['JR Rail Pass', '£426', '£586'],
        ['Accommodation', '£700', '£1,190'],
        ['Meals', '£300', '£450'],
        ['Local Transport', '£50', '£100'],
        ['Activities', '£30', '£90'],
        ['TOTAL PER PERSON', '£2,106', '£3,456']
    ]
    
    cost_table = Table(cost_summary_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    cost_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), lightgrey),
        ('BACKGROUND', (0, -1), (-1, -1), lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(cost_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Money-saving tips
    story.append(Paragraph("Money-Saving Tips", subheading_style))
    tips_text = """
    <b>Flights:</b> Book well in advance and fly mid-week to save £100s. Consider budget airlines with carry-on-only fares.
    
    <b>Lodging:</b> Sharing Airbnbs or family-style ryokans cuts costs. Group bookings often get discounts.
    
    <b>Meals:</b> Convenience stores (¥100–¥500 snacks), conveyor-belt sushi or ramen shops (¥800–¥1,200) help budgets. Splurge on a few special meals and keep most meals moderate.
    
    <b>Transport:</b> Use IC cards (Suica/Pasmo) for small savings. Daily metro passes can be cheaper than individual tickets. Activate JR Pass on day 1 to maximize use.
    
    <b>Activities:</b> Many shrines, parks and museums have little or no fee. Plan free days between splurges.
    """
    story.append(Paragraph(tips_text, body_style))
    story.append(PageBreak())
    
    # Transport logistics
    story.append(Paragraph("Transport & Logistics", heading_style))
    
    transport_text = """
    <b>JR Rail Pass:</b> Covers nearly all train travel between major cities. Must be purchased before arriving in Japan. Activate on your first travel day.
    
    <b>Domestic Flights:</b> Book with budget airlines like Peach, Jetstar, or major carriers ANA/JAL for longer routes (especially to Okinawa).
    
    <b>Local Transport:</b> Get IC cards (Suica/Pasmo) for Tokyo metro and buses. Most cities have excellent public transport.
    
    <b>Group Travel Tips:</b>
    • Book accommodations early for groups of 12
    • Split into smaller groups for restaurant reservations
    • Designate a group leader for transport coordination
    • Download Google Translate app for communication
    • Keep emergency contact information for all group members
    """
    story.append(Paragraph(transport_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Packing essentials
    story.append(Paragraph("Packing Essentials for November", subheading_style))
    packing_text = """
    <b>Clothing:</b> Layers are key! Pack for 15-20°C days and 5-10°C evenings. Bring warm clothes for Hokkaido skiing.
    
    <b>Electronics:</b> Universal adapter, portable charger, camera, phone with offline maps
    
    <b>Documents:</b> Passport, JR Pass voucher, travel insurance, accommodation confirmations
    
    <b>Special Items:</b> Ski gear (or rent in Hokkaido), comfortable walking shoes, light rain jacket
    """
    story.append(Paragraph(packing_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Final recommendations
    story.append(Paragraph("Final Recommendations", subheading_style))
    final_text = """
    <b>Best Time to Visit:</b> Mid-November offers the perfect balance of autumn foliage and early snow for skiing.
    
    <b>Group Coordination:</b> Create a shared group chat and document for real-time updates and decisions.
    
    <b>Cultural Etiquette:</b> Learn basic Japanese phrases, bow when greeting, remove shoes when entering homes/temples.
    
    <b>Emergency Contacts:</b> Keep British Embassy Tokyo contact (+81-3-5211-1100) and travel insurance details handy.
    
    <b>Money:</b> Japan is still largely cash-based. Withdraw yen from 7-Eleven ATMs which accept international cards.
    """
    story.append(Paragraph(final_text, body_style))
    
    # Generate PDF
    doc.build(story)
    
    print(f"PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_japan_trip_pdf()
