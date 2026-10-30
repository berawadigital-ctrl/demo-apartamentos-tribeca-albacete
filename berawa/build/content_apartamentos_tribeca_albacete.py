# Contenido de la demo Apartamentos Tribeca (Albacete) (es/en/fr/de). Hechos de apartamentostribeca.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Apartments.'}
H={'es':['TriBeCa Centro I','TriBeCa Centro II y III'],'en':['TriBeCa Centro I','TriBeCa Centro II and III'],'fr':['TriBeCa Centro I','TriBeCa Centro II et III'],'de':['TriBeCa Centro I','TriBeCa Centro II und III']}
RD={
'es':['60 m², 2 habitaciones y 1 baño privado, cocina completa y balcón. Pensado para familias y grupos de amigos pequeños.','II: 100 m², 3 habitaciones, 2 baños (uno en suite), terraza y lavadora. III: 95 m², 3 habitaciones y 2 baños, de concepto abierto.'],
'en':['60 m², 2 bedrooms and 1 private bathroom, full kitchen and balcony. Designed for families and small groups of friends.','II: 100 m², 3 bedrooms, 2 bathrooms (one en suite), terrace and washing machine. III: 95 m², 3 bedrooms and 2 bathrooms, open-plan.'],
'fr':['60 m², 2 chambres et 1 salle de bain privée, cuisine complète et balcon. Pensé pour les familles et les petits groupes d’amis.','II : 100 m², 3 chambres, 2 salles de bain (dont une en suite), terrasse et lave-linge. III : 95 m², 3 chambres et 2 salles de bain, espace ouvert.'],
'de':['60 m², 2 Schlafzimmer und 1 eigenes Bad, voll ausgestattete Küche und Balkon. Für Familien und kleine Freundesgruppen.','II: 100 m², 3 Schlafzimmer, 2 Bäder (eines en suite), Terrasse und Waschmaschine. III: 95 m², 3 Schlafzimmer und 2 Bäder, offen gestaltet.']}
ART={
'hero':('skyline',9901,['#1b2433','#c98f5a','#ecc590','#3a4a63','#2c3a50','#161e2b']),
'intro':('columns',9902,['#efede8','#f8f6f1','#3a4a63','#2c3a50','#161e2b']),
'r1':('arches',9911,['#ece6dc','#d49a63','#3a4a63','#1b2433','#0f141d']),
'r2':('columns',9912,['#e9ebee','#f7f7f5','#7a4b30','#5a3522','#331e13']),
'g1':('skyline',9921,['#232c3d','#d79a60','#f0cf9e','#5d3f52','#4a3243','#2b1d27']),
'g2':('hills',9922,['#eceee6','#efe4cc','#d9a067','#a7ae8c','#7c8664','#535c42']),
'g3':('arches',9923,['#e9e1d3','#cf955d','#3a4a63','#1b2433','#0f141d']),
'g4':('waves',9924,['#1b2433','#e0a86f','#f3d6aa','#34445c','#283649','#151c27'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Apartamentos Tribeca · Apartamentos turísticos en el centro de Albacete',see_rooms='Ver los apartamentos',hero_k='Albacete · Centro',hero_t='Apartamentos turísticos para familias y grupos de amigos',hero_s='Tres apartamentos de diseño minimalista y moderno en el corazón de Albacete.',
 intro_t='Tranquilidad en el corazón de Albacete',intro_p1='Un emplazamiento tranquilo rodeado por las arterias de la ciudad, con restaurantes, tiendas y puntos de interés a pie de calle.',
 intro_p2='Decoración minimalista y moderna con acabados de alta calidad. Recepción 24 h, Wi-fi, aire acondicionado y cocina completa en todos.',
 stats=['3 apartamentos','Recepción 24 h','Cocina completa','Wi-fi'],nav_rooms='Apartamentos',rooms_t='Nuestros apartamentos',rooms_s='De 60 a 100 m², con dos o tres habitaciones.',
 svcs=['Wi-fi','Aire acondicionado','Smart TV 55″','Cocina completa','Cuna gratuita bajo petición','Factura para empresas'],
 around_s='En pleno centro de Albacete; parkings públicos a menos de 6 minutos andando.',
 loc_p='C/ Nueva 8 · 02002 Albacete, en el centro. Entrada de 16:00 a 00:00 y salida hasta las 12:00.',
 chips=['¿Qué apartamentos tenéis?','¿A qué hora es el check-in?','¿Hay parking?','¿Cómo reservo?']),
'en':dict(title='Apartamentos Tribeca · Tourist apartments in central Albacete',see_rooms='See the apartments',hero_k='Albacete · City centre',hero_t='Tourist apartments for families and groups of friends',hero_s='Three apartments with minimalist, modern design in the heart of Albacete.',
 intro_t='Peace and quiet in the heart of Albacete',intro_p1='A quiet spot surrounded by the city’s main streets, with restaurants, shops and sights right on the doorstep.',
 intro_p2='Minimalist, modern decor with high-quality finishes. 24-hour reception, Wi-fi, air conditioning and a full kitchen in every apartment.',
 stats=['3 apartments','24-hour reception','Full kitchen','Wi-fi'],nav_rooms='Apartments',rooms_t='Our apartments',rooms_s='From 60 to 100 m², with two or three bedrooms.',
 svcs=['Wi-fi','Air conditioning','55″ Smart TV','Full kitchen','Free cot on request','Invoices for companies'],
 around_s='Right in the centre of Albacete; public car parks less than 6 minutes on foot.',
 loc_p='C/ Nueva 8 · 02002 Albacete, city centre. Check-in from 16:00 to 00:00 and check-out until 12:00.',
 chips=['Which apartments do you have?','What time is check-in?','Is there parking?','How do I book?']),
'fr':dict(title='Apartamentos Tribeca · Appartements touristiques au centre d’Albacete',see_rooms='Voir les appartements',hero_k='Albacete · Centre-ville',hero_t='Appartements touristiques pour familles et groupes d’amis',hero_s='Trois appartements au design minimaliste et moderne au cœur d’Albacete.',
 intro_t='Le calme au cœur d’Albacete',intro_p1='Un emplacement tranquille entouré des grandes artères de la ville, avec restaurants, boutiques et sites d’intérêt à deux pas.',
 intro_p2='Décoration minimaliste et moderne avec des finitions de grande qualité. Réception 24 h, Wi-fi, climatisation et cuisine complète partout.',
 stats=['3 appartements','Réception 24 h','Cuisine complète','Wi-fi'],nav_rooms='Appartements',rooms_t='Nos appartements',rooms_s='De 60 à 100 m², avec deux ou trois chambres.',
 svcs=['Wi-fi','Climatisation','Smart TV 55″','Cuisine complète','Lit bébé gratuit sur demande','Facture pour entreprises'],
 around_s='En plein centre d’Albacete ; parkings publics à moins de 6 minutes à pied.',
 loc_p='C/ Nueva 8 · 02002 Albacete, centre-ville. Arrivée de 16:00 à 00:00 et départ jusqu’à 12:00.',
 chips=['Quels appartements avez-vous ?','À quelle heure est le check-in ?','Y a-t-il un parking ?','Comment réserver ?']),
'de':dict(title='Apartamentos Tribeca · Ferienapartments im Zentrum von Albacete',see_rooms='Apartments ansehen',hero_k='Albacete · Zentrum',hero_t='Ferienapartments für Familien und Freundesgruppen',hero_s='Drei Apartments im minimalistischen, modernen Design im Herzen von Albacete.',
 intro_t='Ruhe im Herzen von Albacete',intro_p1='Eine ruhige Lage, umgeben von den Hauptstraßen der Stadt, mit Restaurants, Geschäften und Sehenswürdigkeiten direkt vor der Tür.',
 intro_p2='Minimalistische, moderne Einrichtung mit hochwertigen Materialien. Rezeption rund um die Uhr, WLAN, Klimaanlage und voll ausgestattete Küche.',
 stats=['3 Apartments','Rezeption 24 h','Voll ausgestattete Küche','WLAN'],nav_rooms='Apartments',rooms_t='Unsere Apartments',rooms_s='60 bis 100 m², mit zwei oder drei Schlafzimmern.',
 svcs=['WLAN','Klimaanlage','Smart-TV 55″','Voll ausgestattete Küche','Kostenloses Kinderbett auf Anfrage','Rechnung für Firmen'],
 around_s='Mitten im Zentrum von Albacete; öffentliche Parkhäuser in weniger als 6 Gehminuten.',
 loc_p='C/ Nueva 8 · 02002 Albacete, im Zentrum. Check-in von 16:00 bis 00:00 Uhr, Check-out bis 12:00 Uhr.',
 chips=['Welche Apartments gibt es?','Wann ist der Check-in?','Gibt es einen Parkplatz?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://www.apartamentostribeca.com/reservas/'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Apartamentos Tribeca',ac='#1b2433',ac2='#7a4b30',ac2_a11y='#5a3522',book=BOOK,around=['Catedral de San Juan Bautista','Pasaje de Gabriel Lodares'],foot=FOOT,
 address='C/ Nueva 8 · 02002 Albacete',phones=['+34 623 97 11 17'],emails=['info@apartamentostribeca.com'],maps='Apartamentos TriBeCa, C/ Nueva 8, 02002 Albacete',t=T)
META=dict(repo='demo-apartamentos-tribeca-albacete',name='Apartamentos Tribeca',legal_name='Odontologia Bleda SLU (titular del sitio web según su aviso legal)',registry_ids=['B02558997'],
 url='https://www.apartamentostribeca.com/',domain='apartamentostribeca.com',municipality='Albacete',province='Albacete',sector='tres apartamentos turísticos en el centro de Albacete',
 read_at='2026-10-30T08:51:00+01:00',created_at='2026-10-30T08:50:00+01:00',built_at='2026-10-30T09:05:00+01:00',audit_date='2026-10-30T08:45:02+01:00',
 rating=dict(value=5.0,coincide=['telefono','web'],date='2026-10-29T16:40:10+01:00',url='https://www.google.com/maps/place/Apartamentos+TriBeCa/@38.9920398,-1.8543695,17z/data=!3m1!4b1!4m6!3m5!1s0xd665f89523b0717:0x63bba6c0adf1fa13!8m2!3d38.9920398!4d-1.8543695!16s%2Fg%2F11vt5fxwb1'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (página /reservas/ con el buscador de fechas MotoPress Hotel Booking), HTTP 200 comprobado el 30/10/2026; su web solo está en español, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Qué equipamiento tiene la cocina?','K02'),('¿A qué hora es el check-in?','K03'),('¿Hay parking?','K04'),('¿Admitís mascotas?','K05'),('¿Tenéis cuna para el bebé?','K06'),('¿Hay ascensor?','K07'),('¿Dónde están los apartamentos?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Se puede fumar?','K10'),('¿Me podéis hacer factura?','K11'),('¿Cuál es la política de cancelación?','K12'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which apartments do you have?','K01'),('What equipment does the kitchen have?','K02'),('What time is check-in?','K03'),('Is there parking?','K04'),('Do you accept pets?','K05'),('Do you have a cot for the baby?','K06'),('Is there a lift?','K07'),('Where are the apartments?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Can I smoke?','K10'),('Can you give me an invoice?','K11'),('What is the cancellation policy?','K12'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Quel équipement a la cuisine ?','K02'),('À quelle heure est le check-in ?','K03'),('Y a-t-il un parking ?','K04'),('Acceptez-vous les animaux ?','K05'),('Avez-vous un lit bébé ?','K06'),('Y a-t-il un ascenseur ?','K07'),('Où se trouvent les appartements ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Peut-on fumer ?','K10'),('Pouvez-vous me faire une facture ?','K11'),("Quelle est la politique d'annulation ?",'K12'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Welche Ausstattung hat die Küche?','K02'),('Wann ist der Check-in?','K03'),('Gibt es einen Parkplatz?','K04'),('Sind Haustiere erlaubt?','K05'),('Haben Sie ein Kinderbett?','K06'),('Gibt es einen Aufzug?','K07'),('Wo befinden sich die Apartments?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Darf man rauchen?','K10'),('Bekomme ich eine Rechnung?','K11'),('Wie sind die Stornobedingungen?','K12'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
