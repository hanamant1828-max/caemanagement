"""Script to add 50 sample vehicles with images"""
import os
import random
from app import app, db
from models import Vehicle

# Sample vehicle data for Indian market
vehicles_data = [
    # Cars - Sedans
    {"title": "2022 Honda City ZX CVT", "category": "Cars", "make": "Honda", "model": "City", "year": 2022, "price": 1450000, "mileage": 18000, "description": "Premium sedan with CVT transmission, sunroof, and Honda Sensing safety suite. Well maintained single owner car."},
    {"title": "2021 Maruti Suzuki Dzire VXi", "category": "Cars", "make": "Maruti Suzuki", "model": "Dzire", "year": 2021, "price": 720000, "mileage": 28000, "description": "India's best-selling compact sedan. Excellent fuel efficiency and low maintenance cost."},
    {"title": "2020 Hyundai Verna SX(O)", "category": "Cars", "make": "Hyundai", "model": "Verna", "year": 2020, "price": 1180000, "mileage": 32000, "description": "Feature-rich sedan with turbo petrol engine. Includes ventilated seats and Bose audio system."},
    {"title": "2023 Tata Tigor EV XZ+", "category": "Cars", "make": "Tata", "model": "Tigor EV", "year": 2023, "price": 1280000, "mileage": 8000, "description": "Electric sedan with 306km range. Fast charging capable, connected car features."},
    {"title": "2019 Toyota Yaris VX", "category": "Cars", "make": "Toyota", "model": "Yaris", "year": 2019, "price": 890000, "mileage": 45000, "description": "Reliable Japanese sedan with 7 airbags. Toyota quality and service network."},
    
    # Cars - Hatchbacks
    {"title": "2022 Tata Altroz XZ+", "category": "Cars", "make": "Tata", "model": "Altroz", "year": 2022, "price": 920000, "mileage": 15000, "description": "5-star safety rated premium hatchback. Diesel engine with great mileage."},
    {"title": "2021 Hyundai i20 Asta", "category": "Cars", "make": "Hyundai", "model": "i20", "year": 2021, "price": 1050000, "mileage": 22000, "description": "Premium hatchback with sunroof, connected car features, and BlueLink technology."},
    {"title": "2020 Maruti Suzuki Baleno Alpha", "category": "Cars", "make": "Maruti Suzuki", "model": "Baleno", "year": 2020, "price": 780000, "mileage": 35000, "description": "Popular premium hatchback with great boot space and Nexa service experience."},
    {"title": "2022 Tata Punch Creative", "category": "Cars", "make": "Tata", "model": "Punch", "year": 2022, "price": 880000, "mileage": 12000, "description": "Micro SUV with 5-star safety. Perfect city car with SUV looks and ground clearance."},
    {"title": "2021 Volkswagen Polo GT TSI", "category": "Cars", "make": "Volkswagen", "model": "Polo", "year": 2021, "price": 1150000, "mileage": 25000, "description": "Sporty German hatchback with turbo petrol engine. Fun to drive with solid build."},
    
    # Cars - SUVs
    {"title": "2022 Mahindra XUV700 AX7L", "category": "Cars", "make": "Mahindra", "model": "XUV700", "year": 2022, "price": 2350000, "mileage": 20000, "description": "Flagship SUV with ADAS Level 2. 7-seater luxury with panoramic sunroof."},
    {"title": "2021 Tata Harrier XZ+", "category": "Cars", "make": "Tata", "model": "Harrier", "year": 2021, "price": 1950000, "mileage": 28000, "description": "Premium SUV on OMEGA platform. Stunning design with powerful diesel engine."},
    {"title": "2023 Hyundai Creta SX(O)", "category": "Cars", "make": "Hyundai", "model": "Creta", "year": 2023, "price": 1780000, "mileage": 8000, "description": "India's most popular compact SUV. Panoramic sunroof, ADAS, and premium features."},
    {"title": "2020 Kia Seltos HTX+", "category": "Cars", "make": "Kia", "model": "Seltos", "year": 2020, "price": 1520000, "mileage": 38000, "description": "Feature-loaded compact SUV with UVO connected tech. Great value for money."},
    {"title": "2022 MG Hector Sharp", "category": "Cars", "make": "MG", "model": "Hector", "year": 2022, "price": 1850000, "mileage": 18000, "description": "Internet inside car with 14-inch touchscreen. Spacious cabin and strong presence."},
    {"title": "2021 Toyota Fortuner Legender", "category": "Cars", "make": "Toyota", "model": "Fortuner", "year": 2021, "price": 4250000, "mileage": 32000, "description": "Premium full-size SUV with 4x4. Toyota reliability with commanding road presence."},
    {"title": "2020 Jeep Compass Limited", "category": "Cars", "make": "Jeep", "model": "Compass", "year": 2020, "price": 2180000, "mileage": 40000, "description": "American SUV with Jeep DNA. 4x4 capability with premium interiors."},
    {"title": "2022 Skoda Kushaq Style", "category": "Cars", "make": "Skoda", "model": "Kushaq", "year": 2022, "price": 1680000, "mileage": 15000, "description": "European engineering with Indian value. TSI engine and solid German build."},
    
    # Cars - Luxury
    {"title": "2021 BMW 3 Series 320d", "category": "Cars", "make": "BMW", "model": "3 Series", "year": 2021, "price": 4850000, "mileage": 22000, "description": "Ultimate driving machine. Sporty diesel sedan with M Sport package."},
    {"title": "2022 Mercedes C-Class C200", "category": "Cars", "make": "Mercedes-Benz", "model": "C-Class", "year": 2022, "price": 5650000, "mileage": 12000, "description": "Luxury sedan with latest MBUX system. Baby S-Class looks and features."},
    {"title": "2020 Audi A4 40 TFSI", "category": "Cars", "make": "Audi", "model": "A4", "year": 2020, "price": 4250000, "mileage": 35000, "description": "Quattro all-wheel drive sedan. Virtual cockpit and premium quattro grip."},
    {"title": "2021 Volvo S60 T4 Inscription", "category": "Cars", "make": "Volvo", "model": "S60", "year": 2021, "price": 4950000, "mileage": 18000, "description": "Safest sedan on Indian roads. Scandinavian luxury with excellent safety."},
    
    # Trucks - Pickup
    {"title": "2022 Isuzu D-Max V-Cross", "category": "Trucks", "make": "Isuzu", "model": "D-Max", "year": 2022, "price": 2450000, "mileage": 25000, "description": "Premium lifestyle pickup truck. 4x4 with adventure-ready capabilities."},
    {"title": "2021 Toyota Hilux 4x4", "category": "Trucks", "make": "Toyota", "model": "Hilux", "year": 2021, "price": 3150000, "mileage": 28000, "description": "Legendary tough pickup. Built for extreme conditions with Toyota reliability."},
    {"title": "2020 Mahindra Bolero Pik-Up", "category": "Trucks", "make": "Mahindra", "model": "Bolero Pik-Up", "year": 2020, "price": 850000, "mileage": 55000, "description": "Rugged Indian pickup truck. Perfect for commercial and agricultural use."},
    {"title": "2022 Tata Yodha 2.0", "category": "Trucks", "make": "Tata", "model": "Yodha", "year": 2022, "price": 1150000, "mileage": 18000, "description": "Modern pickup with comfort features. Ideal for both cargo and passenger use."},
    {"title": "2021 Force Gurkha Pickup", "category": "Trucks", "make": "Force", "model": "Gurkha", "year": 2021, "price": 1850000, "mileage": 30000, "description": "Off-road specialist pickup. Extreme capability for tough terrains."},
    
    # Trucks - Light Commercial
    {"title": "2022 Tata Intra V30", "category": "Trucks", "make": "Tata", "model": "Intra V30", "year": 2022, "price": 780000, "mileage": 20000, "description": "Best-in-class pickup truck for small businesses. Great payload and mileage."},
    {"title": "2021 Mahindra Jeeto Plus", "category": "Trucks", "make": "Mahindra", "model": "Jeeto Plus", "year": 2021, "price": 520000, "mileage": 35000, "description": "Compact mini truck for city deliveries. Tight turning radius for narrow streets."},
    {"title": "2020 Ashok Leyland Dost+", "category": "Trucks", "make": "Ashok Leyland", "model": "Dost+", "year": 2020, "price": 680000, "mileage": 48000, "description": "Reliable workhorse for last-mile delivery. Low running cost and strong build."},
    {"title": "2022 Eicher Pro 2049", "category": "Trucks", "make": "Eicher", "model": "Pro 2049", "year": 2022, "price": 1250000, "mileage": 22000, "description": "Light truck for versatile cargo needs. Great for distribution business."},
    {"title": "2021 Maruti Suzuki Super Carry", "category": "Trucks", "make": "Maruti Suzuki", "model": "Super Carry", "year": 2021, "price": 480000, "mileage": 28000, "description": "Mini truck from Maruti. CNG option available with excellent mileage."},
    
    # Trucks - Medium
    {"title": "2020 Tata 407 Gold", "category": "Trucks", "make": "Tata", "model": "407 Gold", "year": 2020, "price": 1450000, "mileage": 65000, "description": "India's most trusted light truck. Proven platform with excellent resale value."},
    {"title": "2021 Eicher Pro 3015", "category": "Trucks", "make": "Eicher", "model": "Pro 3015", "year": 2021, "price": 1850000, "mileage": 45000, "description": "Medium-duty truck for regional transport. Comfortable cabin for long hauls."},
    {"title": "2022 BharatBenz 1015R", "category": "Trucks", "make": "BharatBenz", "model": "1015R", "year": 2022, "price": 1950000, "mileage": 25000, "description": "German engineering for Indian roads. Premium cabin with safety features."},
    
    # Commercial Vehicles
    {"title": "2022 Tata Ace Gold Diesel", "category": "Commercial", "make": "Tata", "model": "Ace Gold", "year": 2022, "price": 520000, "mileage": 22000, "description": "India's favorite mini truck. Perfect for urban logistics and small businesses."},
    {"title": "2021 Mahindra Supro Maxi", "category": "Commercial", "make": "Mahindra", "model": "Supro Maxi", "year": 2021, "price": 680000, "mileage": 35000, "description": "Versatile mini van for cargo and passengers. Dual-purpose vehicle."},
    {"title": "2020 Piaggio Ape Xtra LD", "category": "Commercial", "make": "Piaggio", "model": "Ape Xtra", "year": 2020, "price": 280000, "mileage": 45000, "description": "Three-wheeler cargo vehicle. Low investment, high returns for small traders."},
    {"title": "2022 Bajaj RE Maxima Cargo", "category": "Commercial", "make": "Bajaj", "model": "RE Maxima", "year": 2022, "price": 320000, "mileage": 18000, "description": "Efficient three-wheeler for deliveries. CNG variant with excellent economy."},
    {"title": "2021 Mahindra Bolero MaXX", "category": "Commercial", "make": "Mahindra", "model": "Bolero MaXX", "year": 2021, "price": 950000, "mileage": 42000, "description": "Crew carrier for people transport. Robust and comfortable for rural roads."},
    {"title": "2022 Force Traveller 3350", "category": "Commercial", "make": "Force", "model": "Traveller", "year": 2022, "price": 1850000, "mileage": 30000, "description": "Staff carrier and school bus. 26-seater with AC option available."},
    {"title": "2020 Tata Winger 15 Seater", "category": "Commercial", "make": "Tata", "model": "Winger", "year": 2020, "price": 1450000, "mileage": 55000, "description": "Premium passenger van for travel business. Comfortable seating and AC."},
    {"title": "2021 Ashok Leyland Partner", "category": "Commercial", "make": "Ashok Leyland", "model": "Partner", "year": 2021, "price": 1650000, "mileage": 38000, "description": "Light commercial vehicle for distribution. Good payload capacity."},
    {"title": "2022 Eicher Pro 1059", "category": "Commercial", "make": "Eicher", "model": "Pro 1059", "year": 2022, "price": 1780000, "mileage": 20000, "description": "Container truck for logistics. High fuel efficiency for long routes."},
    {"title": "2020 Tata Ultra 912", "category": "Commercial", "make": "Tata", "model": "Ultra 912", "year": 2020, "price": 1550000, "mileage": 62000, "description": "Light medium-duty truck. Versatile platform for various applications."},
    {"title": "2021 Mahindra Blazo X 28", "category": "Commercial", "make": "Mahindra", "model": "Blazo X", "year": 2021, "price": 2850000, "mileage": 45000, "description": "Heavy-duty tipper truck. FuelSmart technology for maximum efficiency."},
    {"title": "2022 BharatBenz 1217C", "category": "Commercial", "make": "BharatBenz", "model": "1217C", "year": 2022, "price": 2250000, "mileage": 28000, "description": "Medium-duty truck for city distribution. Euro-6 ready engine."},
    {"title": "2020 Ashok Leyland Ecomet 1215", "category": "Commercial", "make": "Ashok Leyland", "model": "Ecomet", "year": 2020, "price": 1850000, "mileage": 52000, "description": "Efficient truck for regional transport. Low total cost of ownership."},
    {"title": "2021 Tata Prima 4928.S", "category": "Commercial", "make": "Tata", "model": "Prima", "year": 2021, "price": 3850000, "mileage": 75000, "description": "Heavy-duty tractor for long haul. World-class cabin comfort."},
    {"title": "2022 Volvo FM 420", "category": "Commercial", "make": "Volvo", "model": "FM 420", "year": 2022, "price": 6850000, "mileage": 35000, "description": "Premium heavy truck for highways. I-Shift and excellent safety features."},
]

# Get available images from uploads folder
def get_random_image():
    uploads_dir = 'static/uploads'
    if os.path.exists(uploads_dir):
        images = [f for f in os.listdir(uploads_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.PNG', '.JPEG', '.JPG'))]
        if images:
            return random.choice(images)
    return None

def add_vehicles():
    with app.app_context():
        # Check existing vehicle count
        existing_count = Vehicle.query.count()
        print(f"Existing vehicles: {existing_count}")
        
        added_count = 0
        for vehicle_data in vehicles_data[:50]:  # Ensure max 50
            # Check if vehicle already exists by title
            existing = Vehicle.query.filter_by(title=vehicle_data['title']).first()
            if existing:
                print(f"Skipping existing: {vehicle_data['title']}")
                continue
            
            # Get a random image
            image = get_random_image()
            images_list = [image] if image else []
            
            vehicle = Vehicle(
                title=vehicle_data['title'],
                category=vehicle_data['category'],
                make=vehicle_data['make'],
                model=vehicle_data['model'],
                year=vehicle_data['year'],
                price=vehicle_data['price'],
                mileage=vehicle_data['mileage'],
                description=vehicle_data['description'],
                contact_name="Friendscars",
                contact_phone="+91 9876543210",
                images=images_list
            )
            
            db.session.add(vehicle)
            added_count += 1
            print(f"Added: {vehicle_data['title']} with image: {image}")
        
        db.session.commit()
        print(f"\nSuccessfully added {added_count} vehicles!")
        print(f"Total vehicles now: {Vehicle.query.count()}")

if __name__ == '__main__':
    add_vehicles()
