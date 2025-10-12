from app import app, db
from models import Vehicle, AdminUser
import sys

def clear_and_seed_database():
    """Clear all data and add exactly 10 records for each category"""
    
    with app.app_context():
        print("Clearing all existing data...")
        
        # Delete all vehicles
        Vehicle.query.delete()
        
        # Delete all admin users
        AdminUser.query.delete()
        
        db.session.commit()
        print("All data cleared successfully!")
        
        # Create admin user
        print("\nCreating admin user...")
        admin = AdminUser()
        admin.username = 'abc'
        admin.set_password('123')
        db.session.add(admin)
        
        # Create exactly 10 Cars
        print("\nAdding 10 Cars...")
        cars = [
            Vehicle(
                title="2020 Honda Civic LX",
                category="Cars",
                make="Honda",
                model="Civic",
                year=2020,
                price=1550000,
                mileage=45000,
                description="Excellent condition, one owner, clean carfax. Great fuel economy and reliability.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["bmw_330i_front.jpg", "bmw_330i_interior.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic"
            ),
            Vehicle(
                title="2021 Toyota Camry LE",
                category="Cars",
                make="Toyota",
                model="Camry",
                year=2021,
                price=2080000,
                mileage=28000,
                description="Low mileage, excellent condition. Advanced safety features included.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["audi_a4_front.jpg", "audi_a4_interior.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic"
            ),
            Vehicle(
                title="2022 BMW 330i xDrive Sport Package",
                category="Cars",
                make="BMW",
                model="330i",
                year=2022,
                price=3450000,
                mileage=18500,
                description="Luxury sports sedan with premium interior, advanced technology, and all-wheel drive.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["bmw_330i_front.jpg", "bmw_330i_interior.jpg", "bmw_330i_side.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="2.0L Turbo",
                horsepower=255,
                drivetrain="AWD"
            ),
            Vehicle(
                title="2023 Mercedes-Benz C300 4MATIC",
                category="Cars",
                make="Mercedes-Benz",
                model="C300",
                year=2023,
                price=4250000,
                mileage=8200,
                description="Nearly new luxury sedan with cutting-edge technology and refined performance.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["mercedes_c300_front.jpg", "mercedes_c300_interior.jpg", "mercedes_c300_rear.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="2.0L Turbo",
                horsepower=255,
                drivetrain="AWD"
            ),
            Vehicle(
                title="2021 Audi A4 Prestige Quattro",
                category="Cars",
                make="Audi",
                model="A4",
                year=2021,
                price=3780000,
                mileage=22100,
                description="Premium compact sedan with sophisticated design and advanced driver assistance features.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["audi_a4_front.jpg", "audi_a4_interior.jpg", "audi_a4_profile.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="2.0L TFSI",
                horsepower=261,
                drivetrain="AWD"
            ),
            Vehicle(
                title="2020 Hyundai Creta SX Turbo",
                category="Cars",
                make="Hyundai",
                model="Creta",
                year=2020,
                price=1680000,
                mileage=35000,
                description="Premium compact SUV with turbo engine, feature-loaded interior.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["hyundai_creta_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="1.4L Turbo",
                horsepower=140,
                drivetrain="FWD"
            ),
            Vehicle(
                title="2022 Maruti Suzuki Swift ZXi+",
                category="Cars",
                make="Maruti Suzuki",
                model="Swift",
                year=2022,
                price=850000,
                mileage=18000,
                description="Popular hatchback with peppy performance and excellent fuel economy.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["swift_front.jpg"],
                fuel_type="Gasoline",
                transmission="Manual",
                engine_size="1.2L",
                horsepower=90,
                drivetrain="FWD"
            ),
            Vehicle(
                title="2023 Toyota Fortuner Legender",
                category="Cars",
                make="Toyota",
                model="Fortuner",
                year=2023,
                price=4850000,
                mileage=15000,
                description="Premium SUV with commanding road presence and advanced features.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["fortuner_front.jpg"],
                fuel_type="Diesel",
                transmission="Automatic",
                engine_size="2.8L",
                horsepower=204,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2021 Honda City VX",
                category="Cars",
                make="Honda",
                model="City",
                year=2021,
                price=1450000,
                mileage=32000,
                description="Stylish sedan with spacious interiors and premium features.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["city_front.jpg"],
                fuel_type="Gasoline",
                transmission="CVT",
                engine_size="1.5L",
                horsepower=121,
                drivetrain="FWD"
            ),
            Vehicle(
                title="2020 Volkswagen Polo GT TSI",
                category="Cars",
                make="Volkswagen",
                model="Polo",
                year=2020,
                price=1180000,
                mileage=28000,
                description="Sporty hatchback with turbocharged engine and solid build quality.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["polo_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="1.0L TSI",
                horsepower=110,
                drivetrain="FWD"
            )
        ]
        
        for car in cars:
            db.session.add(car)
        
        # Create exactly 10 Trucks
        print("Adding 10 Trucks...")
        trucks = [
            Vehicle(
                title="2019 Ford F-150 XLT",
                category="Trucks",
                make="Ford",
                model="F-150",
                year=2019,
                price=2750000,
                mileage=68000,
                description="4WD, crew cab, powerful V6 engine. Perfect for work and family use.",
                contact_name="Friendscars", 
                contact_phone="(555) 123-4567",
                images=["mercedes_c300_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                drivetrain="4WD"
            ),
            Vehicle(
                title="2021 Mahindra Bolero Pickup Extra Strong",
                category="Trucks",
                make="Mahindra",
                model="Bolero Pickup",
                year=2021,
                price=980000,
                mileage=42000,
                description="Rugged pickup truck built for tough conditions. Excellent for commercial use.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["bolero_pickup_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="2.5L",
                horsepower=76,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2020 Isuzu D-Max V-Cross Z",
                category="Trucks",
                make="Isuzu",
                model="D-Max",
                year=2020,
                price=1890000,
                mileage=38000,
                description="Premium lifestyle pickup with excellent off-road capability.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["isuzu_dmax_front.jpg"],
                fuel_type="Diesel",
                transmission="Automatic",
                engine_size="1.9L",
                horsepower=150,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2019 Tata 407 Gold SFC",
                category="Trucks",
                make="Tata",
                model="407 Gold",
                year=2019,
                price=1250000,
                mileage=85000,
                description="Reliable light commercial vehicle for goods transportation.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["tata_407_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="2.2L",
                horsepower=85,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2022 Chevrolet Silverado 1500",
                category="Trucks",
                make="Chevrolet",
                model="Silverado",
                year=2022,
                price=3200000,
                mileage=25000,
                description="Full-size pickup with impressive towing capacity and modern tech.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["silverado_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="5.3L V8",
                horsepower=355,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2021 RAM 1500 Big Horn",
                category="Trucks",
                make="RAM",
                model="1500",
                year=2021,
                price=3100000,
                mileage=32000,
                description="Comfortable pickup with smooth ride and luxurious interior.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["ram_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="5.7L V8",
                horsepower=395,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2020 Toyota Hilux Revo",
                category="Trucks",
                make="Toyota",
                model="Hilux",
                year=2020,
                price=2450000,
                mileage=48000,
                description="Legendary reliability and off-road capability in a mid-size pickup.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["hilux_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="2.8L",
                horsepower=177,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2023 Nissan Frontier Pro-4X",
                category="Trucks",
                make="Nissan",
                model="Frontier",
                year=2023,
                price=2850000,
                mileage=12000,
                description="Rugged mid-size truck with off-road package and modern features.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["frontier_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="3.8L V6",
                horsepower=310,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2021 GMC Sierra 1500",
                category="Trucks",
                make="GMC",
                model="Sierra",
                year=2021,
                price=3350000,
                mileage=29000,
                description="Premium full-size truck with refined interior and strong performance.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["sierra_front.jpg"],
                fuel_type="Gasoline",
                transmission="Automatic",
                engine_size="6.2L V8",
                horsepower=420,
                drivetrain="4WD"
            ),
            Vehicle(
                title="2022 Ford Ranger Wildtrak",
                category="Trucks",
                make="Ford",
                model="Ranger",
                year=2022,
                price=2650000,
                mileage=22000,
                description="Adventure-ready mid-size pickup with excellent capability.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["ranger_front.jpg"],
                fuel_type="Diesel",
                transmission="Automatic",
                engine_size="2.0L",
                horsepower=213,
                drivetrain="4WD"
            )
        ]
        
        for truck in trucks:
            db.session.add(truck)
        
        # Create exactly 10 Commercial Vehicles
        print("Adding 10 Commercial Vehicles...")
        commercial_vehicles = [
            Vehicle(
                title="2020 Ashok Leyland Dost Express",
                category="Commercial Vehicles",
                make="Ashok Leyland",
                model="Dost",
                year=2020,
                price=890000,
                mileage=55000,
                description="Efficient mini truck for last-mile delivery and small business needs.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["dost_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="1.5L",
                horsepower=80,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2021 Mahindra Supro Profit Truck",
                category="Commercial Vehicles",
                make="Mahindra",
                model="Supro",
                year=2021,
                price=750000,
                mileage=48000,
                description="Compact commercial vehicle perfect for urban deliveries.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["supro_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="1.2L",
                horsepower=75,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2022 Tata Ace Gold Petrol",
                category="Commercial Vehicles",
                make="Tata",
                model="Ace Gold",
                year=2022,
                price=680000,
                mileage=25000,
                description="India's favorite mini truck with petrol engine option.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["ace_gold_front.jpg"],
                fuel_type="Gasoline",
                transmission="Manual",
                engine_size="1.05L",
                horsepower=70,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2020 Eicher Pro 2049",
                category="Commercial Vehicles",
                make="Eicher",
                model="Pro 2049",
                year=2020,
                price=1850000,
                mileage=72000,
                description="Medium-duty truck with excellent payload capacity and fuel efficiency.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["eicher_pro_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="3.8L",
                horsepower=140,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2021 Tata Intra V30",
                category="Commercial Vehicles",
                make="Tata",
                model="Intra V30",
                year=2021,
                price=920000,
                mileage=38000,
                description="Smart city delivery truck with modern design and features.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["intra_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="1.5L",
                horsepower=70,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2022 Mahindra Jeeto Plus",
                category="Commercial Vehicles",
                make="Mahindra",
                model="Jeeto Plus",
                year=2022,
                price=580000,
                mileage=20000,
                description="Micro truck ideal for small businesses and local deliveries.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["jeeto_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="0.9L",
                horsepower=16,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2020 Ashok Leyland Partner",
                category="Commercial Vehicles",
                make="Ashok Leyland",
                model="Partner",
                year=2020,
                price=820000,
                mileage=62000,
                description="Reliable light commercial vehicle with good load capacity.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["partner_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="1.5L",
                horsepower=78,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2021 Tata Ultra T.7",
                category="Commercial Vehicles",
                make="Tata",
                model="Ultra T.7",
                year=2021,
                price=1950000,
                mileage=55000,
                description="Medium commercial vehicle with superior technology and comfort.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["ultra_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="3.8L",
                horsepower=150,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2023 BharatBenz 1215R",
                category="Commercial Vehicles",
                make="BharatBenz",
                model="1215R",
                year=2023,
                price=2150000,
                mileage=18000,
                description="Advanced light truck with superior fuel economy and payload.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["bharatbenz_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="3.9L",
                horsepower=150,
                drivetrain="RWD"
            ),
            Vehicle(
                title="2022 Eicher Pro 3015",
                category="Commercial Vehicles",
                make="Eicher",
                model="Pro 3015",
                year=2022,
                price=2850000,
                mileage=42000,
                description="Heavy-duty commercial vehicle with exceptional performance.",
                contact_name="Friendscars",
                contact_phone="(555) 123-4567",
                images=["eicher_3015_front.jpg"],
                fuel_type="Diesel",
                transmission="Manual",
                engine_size="4.6L",
                horsepower=150,
                drivetrain="RWD"
            )
        ]
        
        for cv in commercial_vehicles:
            db.session.add(cv)
        
        # Commit all changes
        db.session.commit()
        
        # Print summary
        print("\n" + "="*50)
        print("DATABASE RESET COMPLETE!")
        print("="*50)
        print(f"\nAdmin Users: {AdminUser.query.count()}")
        print(f"Cars: {Vehicle.query.filter_by(category='Cars').count()}")
        print(f"Trucks: {Vehicle.query.filter_by(category='Trucks').count()}")
        print(f"Commercial Vehicles: {Vehicle.query.filter_by(category='Commercial Vehicles').count()}")
        print(f"\nTotal Vehicles: {Vehicle.query.count()}")
        print("\nAdmin Login: username='abc', password='123'")
        print("="*50)

if __name__ == '__main__':
    clear_and_seed_database()
