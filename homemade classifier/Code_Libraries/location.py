import requests
import re
from urllib.request import urlopen
from phonenumbers import geocoder
import phonenumbers
from opencage.geocoder import OpenCageGeocode


df = [('united states', 'us / usa', '1'), ('china', 'cn / chn', '86'), ('japan', 'jp / jpn', '81'),
      ('germany', 'de / deu', '49'), ('brazil', 'br / bra', '55'), ('france', 'fr / fra', '33'), 
      ('italy', 'it / ita', '39'), ('russia', 'ru / rus', '7'), ('united kingdom', 'gb / gbr', '44'), 
      ('australia', 'au / aus', '61'), ('canada', 'ca / can', '1'), ('india', 'in / ind', '91'), 
      ('mexico', 'mx / mex', '52'), ('south korea', 'kr / kor', '82'), ('spain', 'es / esp', '34'), 
      ('indonesia', 'id / idn', '62'), ('turkey', 'tr / tur', '90'), ('netherlands', 'nl / nld', '31'),
      ('saudi arabia', 'sa / sau', '966'), ('switzerland', 'ch / che', '41'), ('sweden', 'se / swe', '46'), 
      ('norway', 'no / nor', '47'), ('poland', 'pl / pol', '48'), ('belgium', 'be / bel', '32'), 
      ('nigeria', 'ng / nga', '234'), ('argentina', 'ar / arg', '54'), ('taiwan', 'tw / twn', '886'), 
      ('austria', 'at / aut', '43'), ('iran', 'ir / irn', '98'), ('thailand', 'th / tha', '66'), 
      ('united arab emirates', 'ae / are', '971'), ('colombia', 'co / col', '57'), ('venezuela', 've / ven', '58'), 
      ('south africa', 'za / zaf', '27'), ('denmark', 'dk / dnk', '45'), ('malaysia', 'my / mys', '60'), 
      ('singapore', 'sg / sgp', '65'), ('chile', 'cl / chl', '56'), ('hong kong', 'hk / hkg', '852'), 
      ('israel', 'il / isr', '972'), ('philippines', 'ph / phl', '63'), ('egypt', 'eg / egy', '20'), 
      ('finland', 'fi / fin', '358'), ('greece', 'gr / grc', '30'), ('pakistan', 'pk / pak', '92'), 
      ('kazakhstan', 'kz / kaz', '7'), ('iraq', 'iq / irq', '964'), ('ireland', 'ie / irl', '353'), 
      ('portugal', 'pt / prt', '351'), ('algeria', 'dz / dza', '213'), ('qatar', 'qa / qat', '974'), 
      ('peru', 'pe / per', '51'), ('czech republic', 'cz / cze', '420'), ('romania', 'ro / rou', '40'), 
      ('new zealand', 'nz / nzl', '64'), ('kuwait', 'kw / kwt', '965'), ('ukraine', 'ua / ukr', '380'), 
      ('vietnam', 'vn / vnm', '84'), ('bangladesh', 'bd / bgd', '880'), ('hungary', 'hu / hun', '36'), 
      ('angola', 'ao / ago', '244'), ('morocco', 'ma / mar', '212'), ('slovakia', 'sk / svk', '421'), 
      ('puerto rico', 'pr / pri', '(1-787, 1-939)'), ('ecuador', 'ec / ecu', '593'), ('oman', 'om / omn', '968'), 
      ('azerbaijan', 'az / aze', '994'), ('cuba', 'cu / cub', '53'), ('libya', 'ly / lby', '218'), 
      ('belarus', 'by / blr', '375'), ('sri lanka', 'lk / lka', '94'), ('syria', 'sy / syr', '963'), 
      ('luxembourg', 'lu / lux', '352'), ('croatia', 'hr / hrv', '385'), ('dominican republic', 'do / dom', '(1-809, 1-829, 1-849)'), 
      ('myanmar', 'mm / mmr', '95'), ('uruguay', 'uy / ury', '598'), ('uzbekistan', 'uz / uzb', '998'), 
      ('bulgaria', 'bg / bgr', '359'), ('guatemala', 'gt / gtm', '502'), ('sudan', 'sd / sdn', '249'), 
      ('macau', 'mo / mac', '853'), ('costa rica', 'cr / cri', '506'), ('tunisia', 'tn / tun', '216'), 
      ('ethiopia', 'et / eth', '251'), ('lithuania', 'lt / ltu', '370'), ('slovenia', 'si / svn', '386'), 
      ('ghana', 'gh / gha', '233'), ('kenya', 'ke / ken', '254'), ('lebanon', 'lb / lbn', '961'), 
      ('serbia', 'rs / srb', '381'), ('yemen', 'ye / yem', '967'), ('panama', 'pa / pan', '507'), 
      ('turkmenistan', 'tm / tkm', '993'), ('jordan', 'jo / jor', '962'), ('tanzania', 'tz / tza', '255'), 
      ('bolivia', 'bo / bol', '591'), ('latvia', 'lv / lva', '371'), ('paraguay', 'py / pry', '595'), 
      ('bahrain', 'bh / bhr', '973'), ('ivory coast', 'ci / civ', '225'), ('north korea', 'kp / prk', '850'), 
      ('cameroon', 'cm / cmr', '237'), ('trinidad and tobago', 'tt / tto', '1-868'), ('el salvador', 'sv / slv', '503'), 
      ('estonia', 'ee / est', '372'), ('uganda', 'ug / uga', '256'), ('zambia', 'zm / zmb', '260'), 
      ('cyprus', 'cy / cyp', '357'), ('afghanistan', 'af / afg', '93'), ('gabon', 'ga / gab', '241'), 
      ('nepal', 'np / npl', '977'), ('bosnia and herzegovina', 'ba / bih', '387'), ('democratic republic of the congo', 'cd / cod', '243'), 
      ('honduras', 'hn / hnd', '504'), ('equatorial guinea', 'gq / gnq', '240'), ('brunei', 'bn / brn', '673'), 
      ('papua new guinea', 'pg / png', '675'), ('botswana', 'bw / bwa', '267'), ('cambodia', 'kh / khm', '855'), 
      ('georgia', 'ge / geo', '995'), ('senegal', 'sn / sen', '221'), ('iceland', 'is / isl', '354'), 
      ('jamaica', 'jm / jam', '1-876'), ('mozambique', 'mz / moz', '258'), ('republic of the congo', 'cg / cog', '242'), 
      ('chad', 'td / tcd', '235'), ('albania', 'al / alb', '355'), ('burkina faso', 'bf / bfa', '226'), 
      ('namibia', 'na / nam', '264'), ('mali', 'ml / mli', '223'), ('mauritius', 'mu / mus', '230'), 
      ('mongolia', 'mn / mng', '976'), ('nicaragua', 'ni / nic', '505'), ('south sudan', 'ss / ssd', '211'), 
      ('armenia', 'am / arm', '374'), ('laos', 'la / lao', '856'), ('macedonia', 'mk / mkd', '389'), 
      ('madagascar', 'mg / mdg', '261'), ('zimbabwe', 'zw / zwe', '263'), ('malta', 'mt / mlt', '356'), 
      ('new caledonia', 'nc / ncl', '687'), ('bahamas', 'bs / bhs', '1-242'), ('benin', 'bj / ben', '229'), 
      ('haiti', 'ht / hti', '509'), ('tajikistan', 'tj / tjk', '992'), ('kosovo', 'xk / xkx', '383'), 
      ('kyrgyzstan', 'kg / kgz', '996'), ('moldova', 'md / mda', '373'), ('niger', 'ne / ner', '227'), 
      ('rwanda', 'rw / rwa', '250'), ('east timor', 'tl / tls', '670'), ('guinea', 'gn / gin', '224'), 
      ('palestine', 'ps / pse', '970'), ('bermuda', 'bm / bmu', '1-441'), ('curacao', 'cw / cuw', '599'), 
      ('french polynesia', 'pf / pyf', '689'), ('jersey', 'je / jey', '44-1534'), ('liechtenstein', 'li / lie', '423'), 
      ('monaco', 'mc / mco', '377'), ('suriname', 'sr / sur', '597'), ('andorra', 'ad / and', '376'), 
      ('barbados', 'bb / brb', '1-246'), ('fiji', 'fj / fji', '679'), ('guam', 'gu / gum', '1-671'), 
      ('isle of man', 'im / imn', '44-1624'), ('mauritania', 'mr / mrt', '222'), ('montenegro', 'me / mne', '382'), 
      ('sierra leone', 'sl / sle', '232'), ('togo', 'tg / tgo', '228'), ('eritrea', 'er / eri', '291'), 
      ('guyana', 'gy / guy', '592'), ('malawi', 'mw / mwi', '265'), ('swaziland', 'sz / swz', '268'), 
      ('aruba', 'aw / abw', '297'), ('bhutan', 'bt / btn', '975'), ('burundi', 'bi / bdi', '257'), 
      ('cayman islands', 'ky / cym', '1-345'), ('central african republic', 'cf / caf', '236'), 
      ('faroe islands', 'fo / fro', '298'), ('greenland', 'gl / grl', '299'), ('guernsey', 'gg / ggy', '44-1481'), 
      ('lesotho', 'ls / lso', '266'), ('maldives', 'mv / mdv', '960'), ('somalia', 'so / som', '252'), 
      ('antigua and barbuda', 'ag / atg', '1-268'), ('belize', 'bz / blz', '501'), ('british virgin islands', 'vg / vgb', '1-284'), 
      ('cape verde', 'cv / cpv', '238'), ('djibouti', 'dj / dji', '253'), ('gibraltar', 'gi / gib', '350'), 
      ('liberia', 'lr / lbr', '231'), ('saint lucia', 'lc / lca', '1-758'), ('san marino', 'sm / smr', '378'), 
      ('seychelles', 'sc / syc', '248'), ('solomon islands', 'sb / slb', '677'), ('gambia', 'gm / gmb', '220'), 
      ('guinea-bissau', 'gw / gnb', '245'), ('vanuatu', 'vu / vut', '678'), ('grenada', 'gd / grd', '1-473'), 
      ('sint maarten', 'sx / sxm', '1-721'), ('saint kitts and nevis', 'kn / kna', '1-869'), ('saint vincent and the grenadines', 'vc / vct', '1-784'), 
      ('northern mariana islands', 'mp / mnp', '1-670'), ('samoa', 'ws / wsm', '685'), ('comoros', 'km / com', '269'), 
      ('saint martin', 'mf / maf', '590'), ('dominica', 'dm / dma', '1-767'), ('tonga', 'to / ton', '676'), 
      ('american samoa', 'as / asm', '1-684'), ('micronesia', 'fm / fsm', '691'), ('sao tome and principe', 'st / stp', '239'), 
      ('palau', 'pw / plw', '680'), ('saint pierre and miquelon', 'pm / spm', '508'), ('marshall islands', 'mh / mhl', '692'), 
      ('cook islands', 'ck / cok', '682'), ('anguilla', 'ai / aia', '1-264'), ('kiribati', 'ki / kir', '686'), 
      ('falkland islands', 'fk / flk', '500'), ('tuvalu', 'tv / tuv', '688'), ('niue', 'nu / niu', '683'), 
      ('antarctica', 'aq / ata', '672'), ('british indian ocean territory', 'io / iot', '246'), ('christmas island', 'cx / cxr', '61'), 
      ('cocos islands', 'cc / cck', '61'), ('mayotte', 'yt / myt', '262'), ('montserrat', 'ms / msr', '1-664'), 
      ('nauru', 'nr / nru', '674'), ('netherlands antilles', 'an / ant', '599'), ('pitcairn', 'pn / pcn', '64'), 
      ('reunion', 're / reu', '262'), ('saint barthelemy', 'bl / blm', '590'), ('saint helena', 'sh / shn', '290'), 
      ('svalbard and jan mayen', 'sj / sjm', '47'), ('tokelau', 'tk / tkl', '690'), ('turks and caicos islands', 'tc / tca', '1-649'), 
      ('u.s. virgin islands', 'vi / vir', '1-340'), ('vatican', 'va / vat', '379'), ('wallis and futuna', 'wf / wlf', '681'), 
      ('western sahara', 'eh / esh', '212')]


def CountryCodeIdentify(country:str) -> str:
    country = country.lower()
    for count in df:
        if (country == count[0]) or (country in count[1]):
            return count[2]



key = "a782a361a698440cb77a33344b5cc414"

def phone_number_location(number) -> dict:

    ch_number = phonenumbers.parse(number)
        
    info = geocoder.description_for_number(ch_number, "en")

    geocoder1 = OpenCageGeocode(key)
    query = str(info)
    results = geocoder1.geocode(query)

    return results

class Location:
    def __init__(self, *args) -> None:
        
        response = requests.get("http://ip-api.com/json/%s" % self.get_ip()).json()

        location = {"country": response["country"],
                    "countryCode": response["countryCode"],
                    "region": response["regionName"],
                    "city": response["city"],
                    "zip": response["zip"],
                    "lat": response["lat"],
                    "lon": response["lon"],
                    "IP Address": response["query"]}
        
        lat = location["lat"]
        lng = location["lon"]

        ip_cords = lat, lng

        self.IP_cords = ip_cords
        self.location_info = location

        if "numbers" in args:    
            CCIdentity=CountryCodeIdentify(location["countryCode"])
            if len(CCIdentity) > 3:
                for iteration in CCIdentity:
                    results = phone_number_location("+" + iteration + args["numbers"])
            
            results = phone_number_location("+" + CountryCodeIdentify(location["countryCode"]) + args["numbers"])

            lat2 = results[0]['geometry']['lat']
            lng2 = results[0]["geometry"]["lng"]
            
            lat3 = (lat+lat2)/2
            lng3 = (lng+lng2)/2
            put_together = lat3, lng3

            self.phone_location = lat2, lng2
            self.averaged_location = put_together
        
    @classmethod
    def get_ip(self) -> str:
        source = urlopen("http://checkip.dyndns.com")
        data = str(source.read())
        ip_string = re.search(r"\d+\.+\d+\.\d+\.\d+", data).group()

        return ip_string

        
if __name__=="__main__":
    pass
    

    

    

