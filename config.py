# Configuration for multiple businesses. Change BUSINESS_KEY env var to serve a different business.
DEFAULT_BUSINESS_KEY = '4U_Gym'

BUSINESSES = {
    '4U_Gym': {
        'name': '4U Gym (Al Hail North)',
        'menu': [
            'Membership Plans',
            'Facilities & Equipment',
            'Class Schedule',
            'Location & Hours',
            'Pricing',
            'Talk to a Human'
        ],
        'keywords': {
            'Membership Plans': ['membership', 'plan', 'plans'],
            'Facilities & Equipment': ['facility', 'facilities', 'equipment'],
            'Class Schedule': ['class', 'schedule', 'classes', 'timetable'],
            'Location & Hours': ['location', 'where', 'hours', 'time', 'open'],
            'Pricing': ['price', 'pricing', 'cost', 'fees'],
            'Talk to a Human': ['human', 'staff', 'contact', 'talk'],
        },
        'responses': {
            'Membership Plans':
                "🏋️ *Membership Plans*\n\n"
                "• Monthly – 20 OMR (renewable monthly)\n"
                "• Quarterly – 55 OMR\n"
                "• Yearly – 200 OMR\n\n"
                "Sign up at the gym reception or call us for help.",

            'Facilities & Equipment':
                "💪 *Facilities & Equipment*\n\n"
                "• Cardio machines (treadmills, ellipticals)\n"
                "• Free weights & strength training zone\n"
                "• Swimming pool & sauna\n"
                "• Yoga / group class studio\n"
                "• Personal training available\n\n"
                "We keep equipment sanitized and staff nearby to help.",

            'Class Schedule':
                "🗓️ *Class Schedule*\n\n"
                "• Yoga — Mon / Wed / Fri @ 7:00 AM\n"
                "• Zumba — Tue / Thu @ 6:00 PM\n"
                "• Spinning — Sat @ 8:00 AM\n\n"
                "Contact reception to join a class or try a free trial.",

            'Location & Hours':
                "📍 *Location & Hours*\n\n"
                "4U Gym — Al Hail North, Muscat, Oman\n"
                "Google Maps: https://maps.app.goo.gl/aA9hHWAof9H2tist5\n\n"
                "Hours:\n"
                "• Saturday–Thursday: 05:00 AM – 03:00 AM\n"
                "• Friday: 04:00 PM – 10:00 PM\n\n"
                "(Please confirm these hours with the gym directly.)",

            'Pricing':
                "💰 *Pricing (OMR)*\n\n"
                "• Monthly — 20 OMR\n"
                "• Quarterly — 55 OMR\n"
                "• Yearly — 200 OMR\n\n"
                "Cash & card accepted at reception.",

            'Talk to a Human':
                "👩‍💼 *Talk to a Human*\n\n"
                "You can call reception at: +968 78730737 or +968 78766220\n"
                "Alternate: +968 79504353\n\n"
                "Email: contact@4ugym.com\n\n"
                "Would you like us to send these details again? Reply 'menu' to see the options."
        },
        'fallback': "I didn't get that. Reply 'menu' to see options.",
    },
    'Karate_Center': {
        'name': 'International Karate Center - Al Maabelah',
        'menu': [
            'Programs Offered',
            'Class Schedule',
            'Location & Hours',
            'Fees & Membership',
            'Instructors',
            'Talk to a Human'
        ],
        'keywords': {
            'Programs Offered': ['program', 'programs', 'offer', 'offers'],
            'Class Schedule': ['class', 'schedule', 'timetable', 'time'],
            'Location & Hours': ['location', 'where', 'hours', 'open'],
            'Fees & Membership': ['fee', 'fees', 'price', 'pricing', 'membership'],
            'Instructors': ['coach', 'instructor', 'sensei', 'shihan'],
            'Talk to a Human': ['human', 'contact', 'call', 'phone']
        },
        'responses': {
            'Programs Offered':
                "🥋 *Programs Offered*\n\n"
                "• Kids Karate (Ages 5–12)\n"
                "• Teen & Adult Karate\n"
                "• Advanced / Black Belt Training\n"
                "• Self-Defense Workshops\n\n"
                "Great for beginners and experienced students.",

            'Class Schedule':
                "🗓️ *Class Schedule*\n\n"
                "• Kids — Mon / Wed / Fri @ 5:00 PM\n"
                "• Teens — Tue / Thu @ 6:00 PM\n"
                "• Adults — Sat @ 7:00 AM\n\n"
                "Check with the dojo for special workshops and belt exams.",

            'Location & Hours':
                "📍 *Location & Hours*\n\n"
                "International Karate Center — Al Maabelah, Muscat\n"
                "(Search 'International Karate Center Al Maabelah' on Google Maps)\n\n"
                "Hours: Typically evenings & weekends for classes — contact for exact times.",

            'Fees & Membership':
                "💰 *Fees (OMR)*\n\n"
                "• Kids — 15 OMR / month\n"
                "• Teens — 20 OMR / month\n"
                "• Adults — 25 OMR / month\n\n"
                "Contact the dojo for trial classes and group discounts.",

            'Instructors':
                "👨‍🏫 *Our Instructors*\n\n"
                "Head Instructor: Shihan Bava Ahammed\n"
                "Assistant Coaches: Local certified instructors\n\n"
                "For instructor backgrounds, ask us or visit our social media pages.",

            'Talk to a Human':
                "☎️ *Talk to a Human*\n\n"
                "Contact the dojo through their social pages or visit the branch.\n"
                "If you prefer phone contact, please ask and we can provide the best number to call."    
        },
        'fallback': "I didn't get that. Reply 'menu' to see options."
    }
}
