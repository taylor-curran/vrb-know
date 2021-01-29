# from vrb_know.ETL_tools.airdna_calls import market_summary_call
from ETL_tools.airdna_calls import market_search_call, market_summary_call 


initial_100 = [
    ['gatlinburg', 'TN'],
    ['seattle', 'WA'],
    ['bend', 'OR'],
    ['tahoe city', 'CA'],
    ['sonoma', 'CA'],
    ['paso robles', 'CA'],
    ['big bear', 'CA'],
    ['palm springs', 'CA'],
    ['temecula', 'CA'],
    ['san diego', 'CA'],
    ['encinitas', 'CA'],
    ['newport beach', 'CA'],
    ['malibu', 'CA'],
    ['sedona', 'AZ'],
    ['phoenix', 'AZ'],
    ['scottsdale', 'AZ'],
    ['santa fe', 'NM'],
    ['salt lake city', 'UT'],
    ['park city', 'UT'],
    ['jackson hole', 'WY'],
    ['steamboat springs', 'CO'],
    ['vail', 'CO'],
    ['breckenridge', 'CO'],
    ['denver', 'CO'],
    ['telluride', 'CO'],
    ['austin', 'TX'],
    ['corpus christi', 'TX'],
    ['nashville', 'TN'],
    ['pigeon forge', 'TN'],
    ['destin', 'FL'],
    ['fort meyers', 'FL'],
    ['miami', 'FL'],
    ['savannah', 'GA'],
    ['jacksonville beach', 'FL'],
    ['hilton head', 'SC'],
    ['charleston', 'SC'],
    ['oak island', 'NC'],
    ['kissimmee', 'FL'],
    ['gardiner', 'MT'], # Yellowstone
    ['washington', 'DC'],
    ['mission beach', 'CA'],
    ['coronado', 'CA'],
    ['el portal', 'CA'], # Yosemite
    ['yosemite west', 'CA'], # Yosemite
    ['Anaheim', 'CA'],
    ['myrtle beach', 'SC'],
    ['sanibel', 'FL'],
    ['ocean city', 'MD'],
    ['gettysburg', 'PA'],
    ['williamsburg', 'VA'],
    ['terlingua', 'TX'],
    ['mount desert', 'ME'], # Acadia
    ['moab', 'UT'], # Arches
    ['hill city', 'SD'], # Badlands
    ['cimarron', 'CO'], # Black Canyon of the Gunnison
    ['cannonville', 'UT'], # Bryce Canyon
    ['carlsbad', 'NM'], # Carlsbad Caverns
    ['chiloquin', 'OR'], # Crater Lake
    ['pahrump', 'NV'], # Death Valley -> Near Las Vegas
    ['key west', 'FL'],
    ['west glacier', 'MT'], # Glacier National Park
    ['east glacier', 'MT'], # Glacier National Park
    ['wilson', 'WY'], # Grand Teton
    ['teton village', 'WY'], # Grand Teton
    ['haines', 'AK'], # Glacier Bay
    ['grand canyon', 'AZ'], # Grand Canyon
    ['williams', 'AZ'], # Grand Canyon
    ['crestone', 'CO'], # Great Sand Dunes
    ['westcliffe', 'CO'], # Great Sand Dunes
    ['hot springs national', 'AR'], # Hot Springs
    ['hot springs village', 'AR'], # Hot Springs
    ['chesterton', 'IN'], # Indiana Dunes
    ['grand marais', 'MI'], # Isle Royale
    ['hovland', 'MN'], # Isle Royale
    ['joshua tree', 'CA'], # Joshua Tree
    ['yuccaa valley', 'CA'], # Josua Tree
    ['landers', 'CA'], # Josua Tree
    ['westwood', 'CA'], # Lassen Volcanic
    ['bee spring', 'KY'], # Mammoth Cave 
    ['cub run', 'KY'], # Mammoth Cave
    ['ollie', 'KY'], # Mammoth Cave 
    ['cortez', 'CO'], # Mesa Verde,
    ['eatonville', 'WA'], # Mount Rainier
    ['rockport', 'WA'], # North Cascades
    ['hoodsport', 'WA'], # Olympic
    ['belfair', 'WA'], # Olympic
    ['trinidad', 'CA'], # Redwood
    ['grand lake', 'CO'], # Rocky Mountain #
    ['three rivers', 'CA'], # Sequoia
    ['shenandoah', 'VI'], # Shenandoah, 
    ['luray', 'VI'], # Shenandoah,
    ['elkton', 'VI'], # Shenandoah,
    ['gallatin gateway', 'MT'], # Yellowstone
    ['west yellowstone', 'MT'], # Yellowstone
    ['emigrant', 'MT'], # Yellowstone
    ['Nye', 'MT'], # Yellowstone
    ['Big Sky', 'MT'], # Yellowstone
    ['springdale', 'UT'] # Zion
    ]

print(len(initial_100))
print('--------')

first_100_market_ids = []

# for market in initial_100:
#     first_100_market_ids.append(market_search_call(city=market[0], state=market[1]))

print(len(first_100_market_ids))

row = market_summary_call(58697)
market_summary_call(58697)




