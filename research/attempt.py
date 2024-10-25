import json
import csv

# Sample input JSON structure
data = {'items': [
{
     'title': 'Atomic Clock for Satellite Timing and Frequency Control',
     'link': 'https://www.satnow.com/products/atomic-clocks/microchip-technology/148-1082-090-02984-007',
     'organization': 'Microchip Technology',
     'sku': '090-02984-007',
     'details':
     {
        'Space Standard:': 'MIL-STD-810G, MIL-STD-202-213A',
        'Mass:': '35 g',
        'Frequency Accuracy:': '±5 x 10-11, ±5 x 10-10',
        'Frequency Stability:': '3 x 10-10, 1 x 10-10, 3 x 10-11, 1 x 10-11',
        'Phase Noise:': '-140 to -50 dBc/Hz',
        'Supply Voltage:': '3.3 V',
        'Power Consumption:': '120 mW',
        'Radiation:': '20 kRad',
        'Interface:': 'RS-232',
        'Operating Temperature:': '-10 to 70 Degree C',
        'Application:': 'Satellite timing and frequency control, Satellite clock reference, Assured Position, Navigation and Timing (PNT), Atomic clock accuracy, Satellite cro...',
        'Dimension:': '1.6 x 1.39 x 0.45 mm'
     }
}, {'title': 'Rubidium Atomic Frequency Standard', 'link': 'https://www.satnow.com/products/atomic-clocks/airbus/148-1213-rafs', 'organization': 'Airbus', 'sku': 'RAFS', 'details': {'Mass:': '3.3 Kg', 'Frequency Drift:': '5·10-14', 'Frequency Stability:': '5·10-12, 1.5·10-12, 5·10-13, 1.5·10-13, 5·10-14', 'Supply Voltage:': '26 to 48.5 V (adaptable), 50 V (regulated)', 'Operating Temperature:': '-5 to 10 Degree C', 'Storage Temperature:': '-25 to 70 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Giove A & Giove B, Galileo, ISRO (Indian regional navigation satellite system), Navigation payloads (global or regional), High-performance communicati...', 'Dimension:': '210 x 106 x 107 mm'}}, {'title': 'Atomic Clock for Satellite Positioning Applications', 'link': 'https://www.satnow.com/products/atomic-clocks/leonardo/148-1190-phm', 'organization': 'Leonardo', 'sku': 'PHM', 'details': {'Mass:': '18.2 Kg', 'Output Frequency:': '10.00285741 MHz', 'Frequency Drift:': '1x10-14, 1x10-15', 'Supply Voltage:': '50 V', 'Power Consumption:': '60 to 70 W', 'Operating Temperature:': '-15 to 20 Degree C', 'Dimension:': '210 x 500 x 250 mm'}}, {'title': 'Space-Qualified Rubidium Frequency Standard', 'link': 'https://www.satnow.com/products/atomic-clocks/safran-group/148-1236-rafs', 'organization': 'Safran Group', 'sku': 'RAFS', 'details': {'Mass:': '3.4 Kg', 'Output Frequency:': '10 MHz', 'Frequency Accuracy:': '2 x 10-10, 1 x 10-10', 'Frequency Drift:': '3 x 10-14', 'Frequency Stability:': '3 x 10-12, 5 x 10-12, 1 x 10-12, 1.3 x 10-12, 3 x 10-13, 5 x 10-13, 6 x 10-1, 1.8 x ...', 'Phase Noise:': '-145 to -90 dBc/Hz', 'Supply Voltage:': '28 to 50 V', 'Power Consumption:': '35 to 60 W', 'Harmonics:': '-40 dBc', 'Return Loss:': '20 dB', 'Spurious:': '-80 to -60 dBc', 'Operating Temperature:': '-5 to 10 Degree C', 'Storage Temperature:': '-15 to 70 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Navigation satellites, Space scientific missions, Military communication satellites, Tracking and guidance control and  Advanced low orbit digital com...', 'Dimension:': '217 x 124 x 117 mm (L x W x H)'}}, {'title': 'Space Qualified Rubidium Atomic Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/quartzlock/148-1399-e10-spc', 'organization': 'Quartzlock', 'sku': 'E10-SPC', 'details': {'Mass:': '5 Kg', 'Output Frequency:': '10 MHz', 'Frequency Drift:': '1 x 10-13', 'Frequency Stability:': '3 x 10-12, 1 x 10-12, 3 x 10-13, 3 x 10-14, 2 x 10-14', 'Phase Noise:': '-150 to -90 dBc/Hz', 'Power Consumption:': '35 W', 'Radiation:': '100 krad', 'Operating Temperature:': '-15 to 10 Degree C', 'Application:': 'Satellite Navigation System, Intelligence Reconnaissance Satellite, Military Communication Satellite, Deep-Space Survey, Space Station', 'Dimension:': '200 x 100 x 100 mm'}}, {'title': 'Ultra Stable Oscillator for Deep Space Exploration', 'link': 'https://www.satnow.com/products/atomic-clocks/accubeat/148-1454-ultra-stable-oscillator-uso-', 'organization': 'AccuBeat', 'sku': 'Ultra Stable Oscillator (USO)', 'details': {'Mass:': '2 Kg', 'Output Frequency:': '57.51852 Hz', 'Frequency Stability:': '5 x 10-13, 6 x 10-13', 'Phase Noise:': '-119 to -80 dBc/Hz', 'Supply Voltage:': '26.5 to 29 V', 'Harmonics:': '-30 dBc', 'Radiation:': '50 krad', 'Spurious:': '-80 dBc', 'Operating Temperature:': '-20 to 50 Degree C', 'Storage Temperature:': '-30 to 60 Degree C', 'Dimension:': '132.6 x 120 x 105 mm(W x D x H)'}}, {'title': 'Space-Qualified Rubidium Atomic Frequency Standard Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/excelitas-technologies/148-1455-rubidium-atomic-frequency-standard-rafs-', 'organization': 'Excelitas Technologies', 'sku': 'Rubidium Atomic Frequency Standard (RAFS)', 'details': {'Space Standard:': 'MIL-STD-461E', 'Mass:': '14 lbs', 'Output Frequency:': '13.40134393 MHz', 'Frequency Accuracy:': '± 1 x 10-9', 'Frequency Drift:': '1x10-13/day, 5x10-14/day', 'Frequency Stability:': '2 x 10-12, 2x10-14', 'Phase Noise:': '-95 dBc', 'Supply Voltage:': '28 V', 'Power Consumption:': '14 W', 'Harmonics:': '50 dBc', 'Spurious:': '-85 to -50 dBc', 'Operating Temperature:': '-20 to 45 Degree C', 'Storage Temperature:': '-34 to 71 Degree C', 'Application:': 'Global Navigation Satellite Systems (GNSS)', 'Dimension:': '5 x 8.5 x 6 Inches'}}, {'title': '10.23 MHz Master Clock Generation Unit for Satellites', 'link': 'https://www.satnow.com/products/atomic-clocks/airbus/148-1213-cmcu', 'organization': 'Airbus', 'sku': 'CMCU', 'details': {'Space Standard:': 'MIL-STD-1553B', 'Mass:': '5.2 Kg', 'Input Frequency:': '9.99 to 10.01 MHz', 'Output Frequency:': '10.23 MHz', 'Frequency Stability:': '6.4 x10-14, 2.0 x10-14, 6.4 x10-15, 2.0 x10-15', 'Phase Noise:': '-154 to -100 dBc/Hz', 'Supply Voltage:': '26 to 48.5 V', 'Power Consumption:': '21 W', 'Harmonics:': '-60 dBc', 'Radiation:': 'up to 100 kRad', 'Spurious:': '-80 dBc', 'Operating Temperature:': '-15 to 45 Degree C', 'Storage Temperature:': '-40 to 60 Degree C', 'Application:': 'Giove A & Giove B, Galileo, ISRO (Indian regional navigation satellite system), Navigation payloads (global or regional), High-performance communicati...', 'Dimension:': '270 x 216 x 137 mm'}}, {'title': 'Atomic Clock for Satellite Positioning Applications', 'link': 'https://www.satnow.com/products/atomic-clocks/leonardo/148-1190-mini-phm', 'organization': 'Leonardo', 'sku': 'Mini PHM', 'details': {'Mass:': '12 Kg', 'Output Frequency:': '10.00285741 MHz', 'Frequency Drift:': '1x10-14, 1x10-15', 'Supply Voltage:': '50 V', 'Power Consumption:': '47 to 54 W', 'Operating Temperature:': '-15 to 20 Degree C', 'Dimension:': '210 x 485 x 218 mm'}}, {'title': 'Space-Qualified Rubidium Frequency Atomic Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/safran-group/148-1236-minirafs', 'organization': 'Safran Group', 'sku': 'MiniRAFS', 'details': {'Mass:': '0.45 Kg', 'Output Frequency:': '10 MHz', 'Frequency Accuracy:': '2 x 10-10, 1 x 10-10', 'Frequency Drift:': '1 x 10-13, 2 x 10-13', 'Frequency Stability:': '1 x 10-11, 3 x 10-12, 1 x 10-12, 3 x 10-13', 'Phase Noise:': '-135 to -64 dBc/Hz', 'Supply Voltage:': '15.5 to 16.5 V (analog power voltage)', 'Harmonics:': '-30 dBc', 'Return Loss:': '20 dB', 'Spurious:': '-80 to -60 dBc', 'Operating Temperature:': '-15 to 55 Degree C', 'Storage Temperature:': '-55 to 85 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Space scientific missions, Secure satellite communications, Tracking and guidance control, Advanced low satellite orbit digital communications', 'Dimension:': '53 x 67.5 x 107.5 mm (L x W x H)'}}, {'title': 'Atomic Clock for Satellite Timing and Frequency Control', 'link': 'https://www.satnow.com/products/atomic-clocks/microchip-technology/148-1082-090-02984-007', 'organization': 'Microchip Technology', 'sku': '090-02984-007', 'details': {'Space Standard:': 'MIL-STD-810G, MIL-STD-202-213A', 'Mass:': '35 g', 'Frequency Accuracy:': '±5 x 10-11, ±5 x 10-10', 'Frequency Stability:': '3 x 10-10, 1 x 10-10, 3 x 10-11, 1 x 10-11', 'Phase Noise:': '-140 to -50 dBc/Hz', 'Supply Voltage:': '3.3 V', 'Power Consumption:': '120 mW', 'Radiation:': '20 kRad', 'Interface:': 'RS-232', 'Operating Temperature:': '-10 to 70 Degree C', 'Application:': 'Satellite timing and frequency control, Satellite clock reference, Assured Position, Navigation and Timing (PNT), Atomic clock accuracy, Satellite cro...', 'Dimension:': '1.6 x 1.39 x 0.45 mm'}}, {'title': 'Rubidium Atomic Frequency Standard', 'link': 'https://www.satnow.com/products/atomic-clocks/airbus/148-1213-rafs', 'organization': 'Airbus', 'sku': 'RAFS', 'details': {'Mass:': '3.3 Kg', 'Frequency Drift:': '5·10-14', 'Frequency Stability:': '5·10-12, 1.5·10-12, 5·10-13, 1.5·10-13, 5·10-14', 'Supply Voltage:': '26 to 48.5 V (adaptable), 50 V (regulated)', 'Operating Temperature:': '-5 to 10 Degree C', 'Storage Temperature:': '-25 to 70 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Giove A & Giove B, Galileo, ISRO (Indian regional navigation satellite system), Navigation payloads (global or regional), High-performance communicati...', 'Dimension:': '210 x 106 x 107 mm'}}, {'title': 'Atomic Clock for Satellite Positioning Applications', 'link': 'https://www.satnow.com/products/atomic-clocks/leonardo/148-1190-phm', 'organization': 'Leonardo', 'sku': 'PHM', 'details': {'Mass:': '18.2 Kg', 'Output Frequency:': '10.00285741 MHz', 'Frequency Drift:': '1x10-14, 1x10-15', 'Supply Voltage:': '50 V', 'Power Consumption:': '60 to 70 W', 'Operating Temperature:': '-15 to 20 Degree C', 'Dimension:': '210 x 500 x 250 mm'}}, {'title': 'Space-Qualified Rubidium Frequency Standard', 'link': 'https://www.satnow.com/products/atomic-clocks/safran-group/148-1236-rafs', 'organization': 'Safran Group', 'sku': 'RAFS', 'details': {'Mass:': '3.4 Kg', 'Output Frequency:': '10 MHz', 'Frequency Accuracy:': '2 x 10-10, 1 x 10-10', 'Frequency Drift:': '3 x 10-14', 'Frequency Stability:': '3 x 10-12, 5 x 10-12, 1 x 10-12, 1.3 x 10-12, 3 x 10-13, 5 x 10-13, 6 x 10-1, 1.8 x ...', 'Phase Noise:': '-145 to -90 dBc/Hz', 'Supply Voltage:': '28 to 50 V', 'Power Consumption:': '35 to 60 W', 'Harmonics:': '-40 dBc', 'Return Loss:': '20 dB', 'Spurious:': '-80 to -60 dBc', 'Operating Temperature:': '-5 to 10 Degree C', 'Storage Temperature:': '-15 to 70 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Navigation satellites, Space scientific missions, Military communication satellites, Tracking and guidance control and  Advanced low orbit digital com...', 'Dimension:': '217 x 124 x 117 mm (L x W x H)'}}, {'title': 'Space Qualified Rubidium Atomic Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/quartzlock/148-1399-e10-spc', 'organization': 'Quartzlock', 'sku': 'E10-SPC', 'details': {'Mass:': '5 Kg', 'Output Frequency:': '10 MHz', 'Frequency Drift:': '1 x 10-13', 'Frequency Stability:': '3 x 10-12, 1 x 10-12, 3 x 10-13, 3 x 10-14, 2 x 10-14', 'Phase Noise:': '-150 to -90 dBc/Hz', 'Power Consumption:': '35 W', 'Radiation:': '100 krad', 'Operating Temperature:': '-15 to 10 Degree C', 'Application:': 'Satellite Navigation System, Intelligence Reconnaissance Satellite, Military Communication Satellite, Deep-Space Survey, Space Station', 'Dimension:': '200 x 100 x 100 mm'}}, {'title': 'Ultra Stable Oscillator for Deep Space Exploration', 'link': 'https://www.satnow.com/products/atomic-clocks/accubeat/148-1454-ultra-stable-oscillator-uso-', 'organization': 'AccuBeat', 'sku': 'Ultra Stable Oscillator (USO)', 'details': {'Mass:': '2 Kg', 'Output Frequency:': '57.51852 Hz', 'Frequency Stability:': '5 x 10-13, 6 x 10-13', 'Phase Noise:': '-119 to -80 dBc/Hz', 'Supply Voltage:': '26.5 to 29 V', 'Harmonics:': '-30 dBc', 'Radiation:': '50 krad', 'Spurious:': '-80 dBc', 'Operating Temperature:': '-20 to 50 Degree C', 'Storage Temperature:': '-30 to 60 Degree C', 'Dimension:': '132.6 x 120 x 105 mm(W x D x H)'}}, {'title': 'Space-Qualified Rubidium Atomic Frequency Standard Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/excelitas-technologies/148-1455-rubidium-atomic-frequency-standard-rafs-', 'organization': 'Excelitas Technologies', 'sku': 'Rubidium Atomic Frequency Standard (RAFS)', 'details': {'Space Standard:': 'MIL-STD-461E', 'Mass:': '14 lbs', 'Output Frequency:': '13.40134393 MHz', 'Frequency Accuracy:': '± 1 x 10-9', 'Frequency Drift:': '1x10-13/day, 5x10-14/day', 'Frequency Stability:': '2 x 10-12, 2x10-14', 'Phase Noise:': '-95 dBc', 'Supply Voltage:': '28 V', 'Power Consumption:': '14 W', 'Harmonics:': '50 dBc', 'Spurious:': '-85 to -50 dBc', 'Operating Temperature:': '-20 to 45 Degree C', 'Storage Temperature:': '-34 to 71 Degree C', 'Application:': 'Global Navigation Satellite Systems (GNSS)', 'Dimension:': '5 x 8.5 x 6 Inches'}}, {'title': '10.23 MHz Master Clock Generation Unit for Satellites', 'link': 'https://www.satnow.com/products/atomic-clocks/airbus/148-1213-cmcu', 'organization': 'Airbus', 'sku': 'CMCU', 'details': {'Space Standard:': 'MIL-STD-1553B', 'Mass:': '5.2 Kg', 'Input Frequency:': '9.99 to 10.01 MHz', 'Output Frequency:': '10.23 MHz', 'Frequency Stability:': '6.4 x10-14, 2.0 x10-14, 6.4 x10-15, 2.0 x10-15', 'Phase Noise:': '-154 to -100 dBc/Hz', 'Supply Voltage:': '26 to 48.5 V', 'Power Consumption:': '21 W', 'Harmonics:': '-60 dBc', 'Radiation:': 'up to 100 kRad', 'Spurious:': '-80 dBc', 'Operating Temperature:': '-15 to 45 Degree C', 'Storage Temperature:': '-40 to 60 Degree C', 'Application:': 'Giove A & Giove B, Galileo, ISRO (Indian regional navigation satellite system), Navigation payloads (global or regional), High-performance communicati...', 'Dimension:': '270 x 216 x 137 mm'}}, {'title': 'Atomic Clock for Satellite Positioning Applications', 'link': 'https://www.satnow.com/products/atomic-clocks/leonardo/148-1190-mini-phm', 'organization': 'Leonardo', 'sku': 'Mini PHM', 'details': {'Mass:': '12 Kg', 'Output Frequency:': '10.00285741 MHz', 'Frequency Drift:': '1x10-14, 1x10-15', 'Supply Voltage:': '50 V', 'Power Consumption:': '47 to 54 W', 'Operating Temperature:': '-15 to 20 Degree C', 'Dimension:': '210 x 485 x 218 mm'}}, {'title': 'Space-Qualified Rubidium Frequency Atomic Clock', 'link': 'https://www.satnow.com/products/atomic-clocks/safran-group/148-1236-minirafs', 'organization': 'Safran Group', 'sku': 'MiniRAFS', 'details': {'Mass:': '0.45 Kg', 'Output Frequency:': '10 MHz', 'Frequency Accuracy:': '2 x 10-10, 1 x 10-10', 'Frequency Drift:': '1 x 10-13, 2 x 10-13', 'Frequency Stability:': '1 x 10-11, 3 x 10-12, 1 x 10-12, 3 x 10-13', 'Phase Noise:': '-135 to -64 dBc/Hz', 'Supply Voltage:': '15.5 to 16.5 V (analog power voltage)', 'Harmonics:': '-30 dBc', 'Return Loss:': '20 dB', 'Spurious:': '-80 to -60 dBc', 'Operating Temperature:': '-15 to 55 Degree C', 'Storage Temperature:': '-55 to 85 Degree C', 'Connector:': 'SMA, DSUB', 'Application:': 'Space scientific missions, Secure satellite communications, Tracking and guidance control, Advanced low satellite orbit digital communications', 'Dimension:': '53 x 67.5 x 107.5 mm (L x W x H)'}}]}

# Recursive function to flatten JSON keys
def flatten_json_keys(nested_dict, parent_key=''):
    keys = []
    for key, value in nested_dict.items():
        if key[len(key) - 1] == ":":
            full_key = key[:len(key) - 1]
        else:
            full_key = key

        if full_key[0].islower():
            full_key = full_key.capitalize()

        if isinstance(value, dict):
            keys.extend(flatten_json_keys(value, full_key))
        else:
            keys.append(full_key)
    return keys

# Function to gather all unique keys for CSV header
def gather_all_keys(json_data):
    all_keys = set()  # Use a set to avoid duplicate keys
    for item in json_data['items']:
        item_keys = flatten_json_keys(item)
        all_keys.update(item_keys)
    return sorted(all_keys)

def gather_all_data(data, csv_header):
    output = []
    for item in data['items']:
        mapping = {header.strip(): "" for header in csv_header}
        print(mapping)
        # create a lambda function to make all the data linear
        flatten_json = lambda d: {**{k: v for k, v in d.items() if k != 'details'}, **{k: v for k, v in d['details'].items()}}
        item = flatten_json(item)
        print("in yo face space", item)
        for key, value in item.items():
            if key[len(key) - 1] == ":":
                full_key = key[:len(key) - 1]
            else:
                full_key = key

            if full_key[0].islower():
                full_key = full_key.capitalize()

            if full_key in mapping:
                mapping[full_key] = value
            elif full_key in item.get('details', {}):
                mapping[full_key] = item['details'][source_key]
            else:
                mapping[full_key] = ""
            print(full_key)
        output.append(mapping)
    return output

# Gather all the unique keys
csv_headers = gather_all_keys(data)
data = gather_all_data(data, csv_headers)
print(data)

# Save headers to a CSV file
csv_filename = 'output_headers.csv'
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)
    for item in data:
        writer.writerow(item.values())

print(f"CSV headers saved to {csv_filename}")
