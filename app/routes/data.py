from .helpers import getHitsPerDay

# days, hits = getHitsPerDay()

days= ['2020/11/10', '2020/11/11', '2020/11/12', '2020/11/13', '2020/11/14', '2020/11/15', '2020/11/16'] 
hits =  [0, 0, 0, 0, 0, 9, 5]


refs={'Direct': 3, 'https://athul.github.io/notes/graph.html': 3, 'https://athul.github.io/notes/posts/nih.html': 2, 'https://athul.github.io/notes/all.html': 2, 'https://athul.github.io/notes/tags/other.html': 1, 'https://athul.github.io/notes/posts/golang.html': 1, 'https://athul.github.io/notes/posts/goroutines.html': 1, 'https://athul.github.io/notes/posts/air-zettel.html': 1} 
hiturls={'https://athul.github.io/notes/posts/adbot.html': 4, 'https://athul.github.io/notes/all.html': 4, 'https://athul.github.io/notes/posts/air-zettel.html': 1, 'https://athul.github.io/notes/posts/cz.html': 1, 'https://athul.github.io/notes/posts/nih.html': 1, 'https://athul.github.io/notes/tags/go.html': 1, 'https://athul.github.io/notes/graph.html': 1, 'https://athul.github.io/notes/posts/goroutines.html': 1}
hours= ['20', '00', '22'] 
hhits= [5, 5, 4] 
ipSorted=[{'2020-11-16 00:23:10.142567+05:30':{'asn': 'AS3209', 'city': 'Berlin', 'continent_code': 'EU', 'country': 'DE', 'country_area': 357021, 'country_calling_code': '+49', 'country_capital': 'Berlin', 'country_code': 'DE', 'country_code_iso3': 'DEU', 'country_name': 'Germany', 'country_population': 82927922, 'country_tld': '.de', 'currency': 'EUR', 'currency_name': 'Euro', 'in_eu': True, 'ip': '95.90.242.33', 'languages': 'de', 'latitude': 52.5061, 'longitude': 13.3684, 'model': 'Other', 'org': 'Vodafone GmbH', 'postal': '10785', 'region': 'Land Berlin', 'region_code': 'BE', 'timezone': 'Europe/Berlin', 'utc_offset': '+0100', 'version': 'IPv4'}},{'2020-11-16 00:22:59.375922+05:30':{'asn': 'AS3209', 'city': 'Berlin', 'continent_code': 'EU', 'country': 'DE', 'country_area': 357021, 'country_calling_code': '+49', 'country_capital': 'Berlin', 'country_code': 'DE', 'country_code_iso3': 'DEU', 'country_name': 'Germany', 'country_population': 82927922, 'country_tld': '.de', 'currency': 'EUR', 'currency_name': 'Euro', 'in_eu': True, 'ip': '95.90.242.33', 'languages': 'de', 'latitude': 52.5061, 'longitude': 13.3684, 'model': 'Other', 'org': 'Vodafone GmbH', 'postal': '10785', 'region': 'Land Berlin', 'region_code': 'BE', 'timezone': 'Europe/Berlin', 'utc_offset': '+0100', 'version': 'IPv4'}},{'2020-11-16 00:21:11.243832+05:30':{'asn': 'AS3209', 'city': 'Berlin', 'continent_code': 'EU', 'country': 'DE', 'country_area': 357021, 'country_calling_code': '+49', 'country_capital': 'Berlin', 'country_code': 'DE', 'country_code_iso3': 'DEU', 'country_name': 'Germany', 'country_population': 82927922, 'country_tld': '.de', 'currency': 'EUR', 'currency_name': 'Euro', 'in_eu': True, 'ip': '95.90.242.33', 'languages': 'de', 'latitude': 52.5061, 'longitude': 13.3684, 'model': 'Other', 'org': 'Vodafone GmbH', 'postal': '10785', 'region': 'Land Berlin', 'region_code': 'BE', 'timezone': 'Europe/Berlin', 'utc_offset': '+0100', 'version': 'IPv4'}},{'2020-11-16 00:21:07.592049+05:30':{'asn': 'AS3209', 'city': 'Berlin', 'continent_code': 'EU', 'country': 'DE', 'country_area': 357021, 'country_calling_code': '+49', 'country_capital': 'Berlin', 'country_code': 'DE', 'country_code_iso3': 'DEU', 'country_name': 'Germany', 'country_population': 82927922, 'country_tld': '.de', 'currency': 'EUR', 'currency_name': 'Euro', 'in_eu': True, 'ip': '95.90.242.33', 'languages': 'de', 'latitude': 52.5061, 'longitude': 13.3684, 'model': 'Other', 'org': 'Vodafone GmbH', 'postal': '10785', 'region': 'Land Berlin', 'region_code': 'BE', 'timezone': 'Europe/Berlin', 'utc_offset': '+0100', 'version': 'IPv4'}},{'2020-11-16 00:19:15.166111+05:30':{'asn': 'AS3209', 'city': 'Berlin', 'continent_code': 'EU', 'country': 'DE', 'country_area': 357021, 'country_calling_code': '+49', 'country_capital': 'Berlin', 'country_code': 'DE', 'country_code_iso3': 'DEU', 'country_name': 'Germany', 'country_population': 82927922, 'country_tld': '.de', 'currency': 'EUR', 'currency_name': 'Euro', 'in_eu': True, 'ip': '95.90.242.33', 'languages': 'de', 'latitude': 52.5061, 'longitude': 13.3684, 'model': 'Other', 'org': 'Vodafone GmbH', 'postal': '10785', 'region': 'Land Berlin', 'region_code': 'BE', 'timezone': 'Europe/Berlin', 'utc_offset': '+0100', 'version': 'IPv4'}},{'2020-11-15 22:38:54.679407+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}},{'2020-11-15 22:09:58.625159+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'AC2001', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}},{'2020-11-15 22:09:53.499640+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'AC2001', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}},{'2020-11-15 22:09:48.296847+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'AC2001', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}},{'2020-11-15 20:48:56.371573+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}, {'2020-11-15 20:47:40.502408+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}, {'2020-11-15 20:47:28.122849+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}, {'2020-11-15 20:38:26.015282+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}, {'2020-11-15 20:34:40.693390+05:30':{'asn': 'AS55836', 'city': 'Panampilly Nagar', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '157.44.138.229', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 9.9587, 'longitude': 76.2982, 'model': 'Mac', 'org': 'Reliance Jio Infocomm Limited', 'postal': '682036', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}] 
totHits=14
os= {'Mac OS X': 6, 'Fedora': 5, 'Android': 3} 
browsers= {'Firefox': 5, 'Chrome': 4, 'Chrome Mobile': 3, 'Safari': 2} 
dev= {'Desktop 🖥': 11, 'Phone 📱': 3} 
lt=1945.7857142857142
ctDict={'IN|India': 9, 'DE|Germany': 5}