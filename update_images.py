from app import app, db
from models import Vehicle
import os

def update_vehicle_images():
    """Update all vehicle records with actual image filenames"""
    
    with app.app_context():
        # Image mappings for each vehicle
        image_mappings = {
            # Cars
            "2020 Honda Civic LX": ["honda_civic_2020_sed_38503d46.jpg", "honda_civic_2020_sed_bd41c88c.jpg"],
            "2021 Toyota Camry LE": ["toyota_camry_sedan_c_d89492c3.jpg", "toyota_camry_sedan_c_31726831.jpg"],
            "2022 BMW 330i xDrive Sport Package": ["bmw_330i_luxury_spor_c585c9cb.jpg", "bmw_330i_luxury_spor_2f463738.jpg", "bmw_330i_luxury_spor_c2124752.jpg"],
            "2023 Mercedes-Benz C300 4MATIC": ["mercedes-benz_c300_l_b6f18101.jpg", "mercedes-benz_c300_l_c0e078dd.jpg", "mercedes-benz_c300_l_0fc657cf.jpg"],
            "2021 Audi A4 Prestige Quattro": ["audi_a4_sedan_car_dccebe22.jpg", "audi_a4_sedan_car_c919168c.jpg", "audi_a4_sedan_car_af09891e.jpg"],
            "2020 Hyundai Creta SX Turbo": ["hyundai_creta_suv_ca_82a930f7.jpg", "hyundai_creta_suv_ca_a1be3691.jpg"],
            "2022 Maruti Suzuki Swift ZXi+": ["maruti_suzuki_swift__8d88d365.jpg", "maruti_suzuki_swift__e296a41a.jpg"],
            "2023 Toyota Fortuner Legender": ["toyota_fortuner_suv_e3b8e254.jpg", "toyota_fortuner_suv_1929af92.jpg"],
            "2021 Honda City VX": ["honda_city_sedan_car_52bc45ee.jpg", "honda_city_sedan_car_1df3d58b.jpg"],
            "2020 Volkswagen Polo GT TSI": ["volkswagen_polo_hatc_848e1425.jpg", "volkswagen_polo_hatc_0b8461d1.jpg"],
            
            # Trucks
            "2019 Ford F-150 XLT": ["ford_f-150_pickup_tr_12aa2716.jpg", "ford_f-150_pickup_tr_a09d46ce.jpg"],
            "2021 Mahindra Bolero Pickup Extra Strong": ["mahindra_bolero_pick_eb4d501c.jpg", "mahindra_bolero_pick_5cd93049.jpg"],
            "2020 Isuzu D-Max V-Cross Z": ["isuzu_d-max_pickup_t_45c7d17f.jpg", "isuzu_d-max_pickup_t_7245649d.jpg"],
            "2019 Tata 407 Gold SFC": ["tata_407_commercial__38ac7b0d.jpg", "tata_407_commercial__d423ce46.jpg"],
            "2022 Chevrolet Silverado 1500": ["chevrolet_silverado__d765d8bd.jpg", "chevrolet_silverado__5a4295b1.jpg"],
            "2021 RAM 1500 Big Horn": ["ram_1500_pickup_truc_cf8bc460.jpg", "ram_1500_pickup_truc_c4d2d112.jpg"],
            "2020 Toyota Hilux Revo": ["toyota_hilux_pickup__bdf07349.jpg", "toyota_hilux_pickup__7574221a.jpg"],
            "2023 Nissan Frontier Pro-4X": ["nissan_frontier_pick_0bc0e8ef.jpg", "nissan_frontier_pick_ab96dffd.jpg"],
            "2021 GMC Sierra 1500": ["gmc_sierra_pickup_tr_1ba7227c.jpg", "gmc_sierra_pickup_tr_eadff035.jpg"],
            "2022 Ford Ranger Wildtrak": ["ford_ranger_pickup_t_3c04d834.jpg", "ford_ranger_pickup_t_a8928835.jpg"],
            
            # Commercial Vehicles
            "2020 Ashok Leyland Dost Express": ["ashok_leyland_dost_m_2d761c75.jpg", "ashok_leyland_dost_m_d79c197f.jpg"],
            "2021 Mahindra Supro Profit Truck": ["mahindra_supro_comme_dd83b736.jpg", "mahindra_supro_comme_359ddcd8.jpg"],
            "2022 Tata Ace Gold Petrol": ["tata_ace_mini_truck_63e7381e.jpg", "tata_ace_mini_truck_2012c860.jpg"],
            "2020 Eicher Pro 2049": ["eicher_pro_commercia_fa91bf78.jpg", "eicher_pro_commercia_e183bf62.jpg"],
            "2021 Tata Intra V30": ["tata_intra_delivery__6485078c.jpg", "tata_intra_delivery__fd17b6a6.jpg"],
            "2022 Mahindra Jeeto Plus": ["mahindra_jeeto_mini__9033f331.jpg", "mahindra_jeeto_mini__742ea1aa.jpg"],
            "2020 Ashok Leyland Partner": ["ashok_leyland_partne_489d333a.jpg", "ashok_leyland_partne_6cf538d1.jpg"],
            "2021 Tata Ultra T.7": ["tata_ultra_commercia_6ae96106.jpg", "tata_ultra_commercia_cfdafd9c.jpg"],
            "2023 BharatBenz 1215R": ["bharatbenz_commercia_fd9483af.jpg", "bharatbenz_commercia_bf29adab.jpg"],
            "2022 Eicher Pro 3015": ["eicher_pro_3015_heav_25ded483.jpg", "eicher_pro_3015_heav_73c1114f.jpg"]
        }
        
        # Update each vehicle
        updated_count = 0
        for title, images in image_mappings.items():
            vehicle = Vehicle.query.filter_by(title=title).first()
            if vehicle:
                vehicle.images = ','.join(images)
                updated_count += 1
                print(f"Updated images for: {title}")
            else:
                print(f"Vehicle not found: {title}")
        
        db.session.commit()
        
        print(f"\n{'='*50}")
        print(f"Successfully updated {updated_count} vehicles with images")
        print(f"{'='*50}")
        
        # Verify all vehicles have images
        print("\nVerifying all vehicles have images:")
        all_vehicles = Vehicle.query.all()
        for vehicle in all_vehicles:
            images_count = len(vehicle.images_list) if vehicle.images_list else 0
            print(f"{vehicle.category}: {vehicle.title} - {images_count} images")

if __name__ == '__main__':
    update_vehicle_images()
