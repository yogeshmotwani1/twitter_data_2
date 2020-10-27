import os
import subprocess
import random, time, queue
import multiprocessing
multiprocessing.set_start_method('spawn')

from multiprocessing.managers import BaseManager
# command=['twint -s "@exidecare"  -o exidecare.csv --csv --limit 100','twint -s "@venkysindia"  -o venkys.csv --csv --limit 100']

company = ['GEMINI EDIBLES AND FATS INDIA PRIVATE LIMITED','JSW CEMENT LIMITED','RENEW SOLAR POWER PRIVATE LIMITED','M@S.ADANI WILMAR LTD','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','EMAAR MGF LAND LIMITED','KEC INTERNATIONAL LIMITED','SOBHA LIMITED','INDIAN POTASH LIMITED','DISH INFRA SERVICES PRIVATE LIMITED','M@S.ADANI ENTERPRISES LIMITED','M@S.ADANI ENTERPRISES LIMITED','M@S.ADANI ENTERPRISES LIMITED','FUTURE CORPORATE RESOURCES PRIVATE LIMITED','POLYCAB INDIA LIMITED','SIEMENS GAMESA RENEWABLE POWER PRIVATE LIMITED','HT MEDIA LTD.','M@S.CEAT LTD','EXIDE INDUSTRIES LIMITED','VENKATESHWARA HATCHERIES PRIVATE LIMITED','GAWAR CONSTRUCTION LIMITED','TITAN COMPANY LIMITED','TITAN COMPANY LIMITED','TITAN COMPANY LIMITED','TITAN COMPANY LIMITED','TITAN COMPANY LIMITED','LITE BITE FOODS PVT LTD','COFFEE DAY GLOBAL LIMITED','AMRI HOSPITALS LIMITED','AMRI HOSPITALS LIMITED','EVEREADY INDUSTRIES INDIA LTD','TATA POWER SOLAR SYSTEMS LIMITED','HATHWAY CABLE AND DATACOM LIMITED','BAJAJ ELECTRICALS LIMITED','BAJAJ ELECTRICALS LIMITED','MAHINDRA SUSTEN PRIVATE LIMITED','THRIVENI SAINIK MINING PRIVATE LIMITED','G R INFRAPROJECTS LIMITED','MORE RETAIL LIMITED','MAHARASHTRA SEAMLESS LIMITED','THINK GAS INVESTMENTS PTE LTD','STERLITE TECHNOLOGIES LIMITED','AAK KAMANI PRIVATE LIMITED','JINDAL ITF LIMITED','VEDANTA LIMITED','ESSEL MINING & INDUSTRIES LIMITED','DILIP BUILDCON LIMITED','MANIPAL ACADAMIC SERVICES INTERNATIONAL','SINTEX BAPL LTD','Parasa Kente Collieries Ltd','Universal Cables Ltd','Fourth Partner Energy Private Ltd','Tata Sky Limited','Deloitte Touche Tohmatsu India, LLP','H & R Johnson (India)','Jubiliant life sciences ltd','K raheja private limited','K raheja private limited','K raheja private limited']
handle = ['@freedomoil_in','@jswcement','@renew_power','fortune rice','emaar delhi','emaar gurgaon','emaar jaipur','emaar chennai','emaar mohali','emaar lucknow','emaar hyderabad','@kec_intl','@sobhaltd','@indian_potash','@dishtv_india','@adanionline','@adani_elec_mumbai','@adani_gas','@bigbazaar','@polycabindia','@siemensgamesa','ht media ltd','@ceattyres','@exidecare','@venkysindia','gawar construction','@titancompanyltd','@titanestore','@fastrack','@sonatawatches','@leecooperin','@bitefoods','@cafecoffeeday','@amrihospitals','@amribbsr','@evereadyindia','tatapowersolar','hathwaybrdband','@bajajelectrical','@bajajelecbiz','@mahindrasusten','@thriveni_group','@grinfraprojects','@moreretailltd','@seamlesstubes','@thinkgasindia','@stl_tech','@aakkamani','@jindal_saw','@vedantalimited','@esselmining','@dilipbuildcon','@manipaluniv','@sintexplastics_','Parsa kente','@cablesuniversal','@4PEL','@tatasky','@deloitteindia','@HRJohnsonIndia','@jubiliantlifesci','@corpraheja','@inorbitmall','@shoppersstop']
print(len(company))
print(len(handle))
for i in range(0,len(company)):
    print(company[i]+" ---> "+handle[i])

for i in range(0,len(company)):
    cmd = subprocess.Popen('twint -s '+'"'+handle[i]+'" '+'-o '+'"'+company[i]+"#"+handle[i]+".csv "+'" '+'--csv '+'--limit 150000'+' -ho')
    cmd.communicate() 