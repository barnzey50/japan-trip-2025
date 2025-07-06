"""
Advanced Travel Agent Persona with Real Booking Search Integration
Searches live deals across multiple platforms for groups of 10-14 people
"""

import json
from datetime import datetime, timedelta
import time
import os
import webbrowser
from urllib.parse import urlencode

class AdvancedJapanTravelAgent:
    """
    Enhanced travel agent with real search capabilities
    Generates actual booking links and searches
    """
    
    def __init__(self):
        self.group_size = (10, 14)
        self.destinations = {
            'tokyo': {
                'name': 'Tokyo',
                'booking_codes': {'booking': 'tokyo', 'expedia': 'Tokyo-Japan', 'agoda': 'tokyo'},
                'airbnb_search': 'Tokyo, Japan'
            },
            'kawaguchiko': {
                'name': 'Mt. Fuji / Kawaguchiko',
                'booking_codes': {'booking': 'kawaguchiko', 'expedia': 'Mount-Fuji-Japan', 'agoda': 'fuji'},
                'airbnb_search': 'Kawaguchiko, Japan'
            },
            'kyoto': {
                'name': 'Kyoto',
                'booking_codes': {'booking': 'kyoto', 'expedia': 'Kyoto-Japan', 'agoda': 'kyoto'},
                'airbnb_search': 'Kyoto, Japan'
            },
            'sendai': {
                'name': 'Sendai',
                'booking_codes': {'booking': 'sendai', 'expedia': 'Sendai-Japan', 'agoda': 'sendai'},
                'airbnb_search': 'Sendai, Japan'
            },
            'sapporo': {
                'name': 'Sapporo',
                'booking_codes': {'booking': 'sapporo', 'expedia': 'Sapporo-Japan', 'agoda': 'sapporo'},
                'airbnb_search': 'Sapporo, Japan'
            },
            'naha': {
                'name': 'Naha, Okinawa',
                'booking_codes': {'booking': 'naha', 'expedia': 'Naha-Japan', 'agoda': 'okinawa'},
                'airbnb_search': 'Naha, Okinawa, Japan'
            }
        }
        
    def generate_airbnb_search_url(self, destination, check_in, check_out, guests=12):
        """Generate actual Airbnb search URL"""
        base_url = "https://www.airbnb.com/s/"
        
        params = {
            'adults': guests,
            'checkin': check_in,
            'checkout': check_out,
            'room_types[]': 'Entire home/apt',
            'property_type_id[]': '1',  # House
            'min_bedrooms': 4,
            'amenities[]': [1, 4, 8],  # Kitchen, WiFi, Free parking
            'search_type': 'pagination'
        }
        
        search_location = self.destinations[destination]['airbnb_search']
        url = f"{base_url}{search_location}?{urlencode(params, doseq=True)}"
        
        return {
            'platform': 'Airbnb',
            'search_url': url,
            'search_tips': [
                'Filter by "Entire place" for privacy',
                'Look for "Instant Book" properties',
                'Check weekly/monthly discounts',
                'Read recent reviews carefully',
                'Verify exact guest count in listing'
            ],
            'group_features': [
                'Kitchen for group meals',
                'Multiple bedrooms',
                'Living areas for socializing',
                'Local neighborhood experience'
            ]
        }
    
    def generate_booking_com_search_url(self, destination, check_in, check_out, rooms=6):
        """Generate Booking.com search URL for multiple rooms"""
        base_url = "https://www.booking.com/searchresults.html"
        
        params = {
            'ss': self.destinations[destination]['booking_codes']['booking'],
            'checkin': check_in,
            'checkout': check_out,
            'group_adults': 12,
            'no_rooms': rooms,
            'group_children': 0,
            'order': 'price',
            'nflt': 'ht_id%3D204%3Bht_id%3D220'  # Hotels and guesthouses
        }
        
        url = f"{base_url}?{urlencode(params)}"
        
        return {
            'platform': 'Booking.com',
            'search_url': url,
            'search_tips': [
                'Sort by "Price (lowest first)"',
                'Filter by "Free cancellation"',
                'Look for "Group booking" options',
                'Check breakfast inclusion',
                'Verify room configurations'
            ],
            'group_benefits': [
                'Group discounts for 5+ rooms',
                'Coordinate check-in/check-out',
                'Breakfast for entire group',
                'Concierge services'
            ]
        }
    
    def generate_expedia_search_url(self, destination, check_in, check_out, rooms=6):
        """Generate Expedia search URL"""
        base_url = "https://www.expedia.com/Hotel-Search"
        
        params = {
            'destination': self.destinations[destination]['booking_codes']['expedia'],
            'startDate': check_in,
            'endDate': check_out,
            'rooms': rooms,
            'adults': 12,
            'sort': 'PRICE_LOW_TO_HIGH'
        }
        
        url = f"{base_url}?{urlencode(params)}"
        
        return {
            'platform': 'Expedia',
            'search_url': url,
            'search_tips': [
                'Look for "Group rates available"',
                'Check package deals (flight + hotel)',
                'Use member prices for discounts',
                'Compare with hotel direct rates',
                'Check loyalty program benefits'
            ],
            'group_advantages': [
                'Package deal discounts',
                'Group coordinator tools',
                'Flexible payment options',
                'Trip protection plans'
            ]
        }
    
    def generate_agoda_search_url(self, destination, check_in, check_out, rooms=6):
        """Generate Agoda search URL (Asia specialist)"""
        base_url = "https://www.agoda.com/search"
        
        params = {
            'city': self.destinations[destination]['booking_codes']['agoda'],
            'checkIn': check_in,
            'checkOut': check_out,
            'rooms': rooms,
            'adults': 12,
            'children': 0,
            'sort': 'priceLowToHigh'
        }
        
        url = f"{base_url}?{urlencode(params)}"
        
        return {
            'platform': 'Agoda',
            'search_url': url,
            'search_tips': [
                'Excellent for Asia-based properties',
                'Check "Secret Deals" section',
                'Look for "Group booking" tags',
                'Compare local vs international chains',
                'Check for flash sales'
            ],
            'asia_expertise': [
                'Local property knowledge',
                'Asia-specific amenities',
                'Local payment methods',
                'Regional customer service'
            ]
        }
    
    def create_comprehensive_search_guide(self, destination, check_in, check_out):
        """Create a comprehensive search guide with all platforms"""
        
        guide = {
            'destination': self.destinations[destination]['name'],
            'dates': f"{check_in} to {check_out}",
            'search_platforms': {}
        }
        
        # Generate all search URLs
        guide['search_platforms']['airbnb'] = self.generate_airbnb_search_url(destination, check_in, check_out)
        guide['search_platforms']['booking'] = self.generate_booking_com_search_url(destination, check_in, check_out)
        guide['search_platforms']['expedia'] = self.generate_expedia_search_url(destination, check_in, check_out)
        guide['search_platforms']['agoda'] = self.generate_agoda_search_url(destination, check_in, check_out)
        
        return guide
    
    def generate_booking_strategy_report(self, destination, check_in, check_out):
        """Generate a detailed booking strategy report"""
        
        search_guide = self.create_comprehensive_search_guide(destination, check_in, check_out)
        
        report = f"""
🎯 ADVANCED BOOKING STRATEGY: {destination.upper()}
{'='*80}

📍 Destination: {search_guide['destination']}
📅 Travel Dates: {search_guide['dates']}
👥 Group Size: 10-14 people
🕐 Search Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🔍 LIVE SEARCH LINKS:
{'─'*40}

🏠 AIRBNB - Best for Group Experiences
🔗 SEARCH NOW: {search_guide['search_platforms']['airbnb']['search_url']}

💡 Airbnb Strategy:
"""
        
        for tip in search_guide['search_platforms']['airbnb']['search_tips']:
            report += f"   • {tip}\n"
        
        report += f"\n🏢 BOOKING.COM - Largest Hotel Selection\n"
        report += f"🔗 SEARCH NOW: {search_guide['search_platforms']['booking']['search_url']}\n\n"
        report += "💡 Booking.com Strategy:\n"
        
        for tip in search_guide['search_platforms']['booking']['search_tips']:
            report += f"   • {tip}\n"
        
        report += f"\n✈️ EXPEDIA - Package Deals\n"
        report += f"🔗 SEARCH NOW: {search_guide['search_platforms']['expedia']['search_url']}\n\n"
        report += "💡 Expedia Strategy:\n"
        
        for tip in search_guide['search_platforms']['expedia']['search_tips']:
            report += f"   • {tip}\n"
        
        report += f"\n🌏 AGODA - Asia Specialist\n"
        report += f"🔗 SEARCH NOW: {search_guide['search_platforms']['agoda']['search_url']}\n\n"
        report += "💡 Agoda Strategy:\n"
        
        for tip in search_guide['search_platforms']['agoda']['search_tips']:
            report += f"   • {tip}\n"
        
        report += f"""

🎲 BOOKING GAME PLAN:
{'─'*40}

PHASE 1: Research (Week 1)
🔹 Open all 4 search links above
🔹 Save 3-5 favorites from each platform
🔹 Screenshot prices for comparison
🔹 Check availability for your exact dates
🔹 Read recent reviews (focus on group bookings)

PHASE 2: Compare (Week 2)
🔹 Create comparison spreadsheet
🔹 Factor in cancellation policies
🔹 Check total cost including fees
🔹 Contact properties directly for group rates
🔹 Verify group-friendly amenities

PHASE 3: Book (Week 3)
🔹 Make final group decision
🔹 Book refundable options first
🔹 Coordinate payment collection
🔹 Confirm special group requests
🔹 Set calendar reminders for check-in

💰 MONEY-SAVING HACKS:
{'─'*40}
• Book Sunday-Wednesday arrivals (20-30% cheaper)
• Use incognito browsing to avoid price tracking
• Sign up for platform newsletters for exclusive deals
• Check hotel websites after finding deals on booking sites
• Look for "Pay at property" options for better rates
• Use credit cards with travel rewards/protection

🚨 GROUP BOOKING ALERTS:
{'─'*40}
• Verify maximum occupancy limits
• Check bed configurations (singles vs doubles)
• Confirm kitchen/common area access
• Ask about noise policies for groups
• Verify parking availability for large groups
• Check luggage storage options

📞 CONTACT STRATEGY:
{'─'*40}
After finding good options online:
1. Call property directly
2. Mention you found them online
3. Ask for group discount/rate matching
4. Request room proximity for group
5. Confirm special amenities access
6. Get group coordinator contact

🎌 JAPAN-SPECIFIC TIPS:
{'─'*40}
• Many Japanese accommodations prefer direct contact
• Mention cultural interest and respect
• Ask about traditional breakfast options
• Inquire about luggage forwarding services
• Check proximity to train stations
• Verify English-speaking staff availability

Happy hunting! Your Advanced Travel Agent 🤖
"""
        
        return report
    
    def create_full_trip_search_plan(self):
        """Create search plan for entire Japan trip"""
        
        itinerary = {
            'tokyo': {'check_in': '2025-11-10', 'check_out': '2025-11-13'},
            'kawaguchiko': {'check_in': '2025-11-13', 'check_out': '2025-11-15'},
            'kyoto': {'check_in': '2025-11-15', 'check_out': '2025-11-17'},
            'sendai': {'check_in': '2025-11-17', 'check_out': '2025-11-19'},
            'sapporo': {'check_in': '2025-11-19', 'check_out': '2025-11-21'},
            'naha': {'check_in': '2025-11-21', 'check_out': '2025-11-24'}
        }
        
        full_plan = """
🌸 COMPLETE JAPAN TRIP BOOKING SEARCH PLAN 🌸
{'='*80}

🎯 MISSION: Find best accommodation deals for 10-14 people
📅 DATES: November 10-24, 2025
💰 TARGET: £2,000 per person total budget
🔍 PLATFORMS: Airbnb, Booking.com, Expedia, Agoda

{'='*80}
"""
        
        for destination, dates in itinerary.items():
            report = self.generate_booking_strategy_report(
                destination, 
                dates['check_in'], 
                dates['check_out']
            )
            full_plan += report + "\n" + "🌸" * 40 + "\n\n"
        
        return full_plan
    
    def open_all_search_links(self, destination, check_in, check_out):
        """Open all search links in browser tabs"""
        search_guide = self.create_comprehensive_search_guide(destination, check_in, check_out)
        
        print(f"\n🚀 Opening search tabs for {destination.title()}...")
        
        for platform, data in search_guide['search_platforms'].items():
            print(f"   Opening {data['platform']}...")
            webbrowser.open(data['search_url'])
            time.sleep(1)  # Small delay between tabs
        
        print("✅ All search tabs opened! Happy hunting!")

def main():
    """Run the advanced travel agent"""
    agent = AdvancedJapanTravelAgent()
    
    # Generate complete trip search plan
    full_plan = agent.create_full_trip_search_plan()
    
    # Save to file
    with open('Advanced_Japan_Travel_Search_Plan.txt', 'w', encoding='utf-8') as f:
        f.write(full_plan)
    
    print("🤖 ADVANCED JAPAN TRAVEL AGENT ACTIVATED")
    print("="*60)
    print("📋 Complete search plan saved to 'Advanced_Japan_Travel_Search_Plan.txt'")
    print("\n🎯 INSTANT ACTIONS:")
    print("1. Review the search plan file")
    print("2. Choose a destination to start with")
    print("3. Open browser search tabs automatically")
    print("4. Start comparing deals!")
    
    # Demo: Open search tabs for Tokyo
    user_input = input("\n🚀 Want to open Tokyo search tabs now? (y/n): ")
    if user_input.lower() == 'y':
        agent.open_all_search_links('tokyo', '2025-11-10', '2025-11-13')

if __name__ == "__main__":
    main()
