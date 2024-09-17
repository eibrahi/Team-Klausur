import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# Seitenmenü in der Sidebar
st.sidebar.title("Team-Klausur PG D/SX")

menu = st.sidebar.radio("Wähle eine Folien:", 
                        ("Cloud-Computing-Grundlagen", 
                         "Cloud-Deployement-Modelle",
                         "Cloud-Service-Modelle", 
                         "Summary", 
                         "Mercedes Platformen",
                         "Architektur CAD",
                         "Delta-Lake-House",))

# Einführung in die Cloud
import streamlit as st

# Menüpunkt: Was ist die Cloud?
if menu == "Cloud-Computing-Grundlagen":
    
    st.title("Was ist Cloud-Computing")

    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        
        st.write("""
        - Netzwerk von Servern/Ressourcen, die über das Internet zugänglich sind. 
                 
        - Bei diesen Ressourcen kann es sich um Speicherplatz, Rechenleistung, Software (Web-Anwendungen) oder komplette IT-Infrastrukturen handeln.        
      
        - Daten und Anwendungen werden nicht lokal gespeichert, sie werden in der Cloud gespeichert und können von überall aus abgerufen werden.
        
        - Dienste werden von Drittanbietern, die die physische Infrastukrur verwalten, bereitgestellt. 
        
        - Anwender konzentriert sich nur auf die Nutzung der Dienste.
                 """)
    
    with col2:
        st.image("data/Cloud.PNG", caption="Cloud", use_column_width=True)
        st.image("data/Cloud-Computing.PNG", caption="Cloud Computing", use_column_width=True)

    st.video("https://www.youtube.com/watch?v=NoABtadYfxo", )

        # Fügt einen Abstand vor dem zweiten Textblock hinzu
    # st.write("")  # Leere Zeile als Abstand

# Typen des Cloud Computing
elif menu == "Cloud-Deployement-Modelle":
    st.title("Deployement Modelle")
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:    
        st.subheader("Public Cloud")
        st.write("Dienste werden über das öffentliche Internet angeboten und sind für jedermann zugänglich (z. B. AWS, Microsoft Azure).")
    with col2:
        st.image("data/Mercedes-Bus.png", caption="Accessable to everyone", use_column_width=True)
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Private Cloud")
        st.write("""Wird exklusiv von einem Unternehmen genutzt und ist nicht für die Öffentlichkeit zugänglich.
             """)
    with col2:
        st.image("data/Mercedes-Auto.png", caption="Owned by a single person", use_column_width=True)

    # Fügt einen Abstand vor dem zweiten Textblock hinzu
    st.write("")  # Leere Zeile als Abstand
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Hybrid Cloud")
        st.write("Kombination aus Private und Public Cloud, um die Vorteile beider zu nutzen.")
    with col2:
        st.image("data/Mercedes-Taxi.png", caption="Rent a private taxi", use_column_width=True)

    
    st.video("https://youtu.be/M988_fsOSWo?t=127", start_time=142, end_time=195)
    
# Typen des Cloud Computing
elif menu == "Cloud-Service-Modelle":
    st.title("Service Modelle")

     # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Infrastructure as a Service (IaaS)")
        st.write("""
        - Bietet virtuelle Maschinen, Netzwerke und Speicherplatz.
        - Nutzer mieten die Infrastruktur und zahlen nach Nutzung.
        - Beispiel: Microsoft Azure, Amazon Web Services (AWS).
        """)
    
        st.subheader("Platform as a Service (PaaS)")
        st.write("""
        - Bietet Entwicklungsplattformen, um Anwendungen zu entwickeln.
        - Entwickler müssen sich nicht um die zugrunde liegende Infrastruktur kümmern.
        - Beispiel: Databricks, PowerBI Publish Server, Google App Engine.
        """)

        st.subheader("Software as a Service (SaaS)")
        st.write("""
        - Bietet Software über das Internet an.
        - Nutzer verwenden die Software direkt über den Webbrowser, ohne Installation.
        - Beispiel: Microsoft Office 365, Google Workspace.
        """)
    
    with col2:
        st.write("")  # Leere Zeile als Abstand
        st.image("data/Pizza-as-a-Service-Infrastructure.png", caption="Infrastructure as a Pizza-Service", use_column_width=True)
        st.write("")  # Leere Zeile als Abstand
        st.image("data/Pizza-as-a-Service-Platform.png", caption="Platform as a Pizza-Service", use_column_width=True)
        st.write("")  # Leere Zeile als Abstand
        st.image("data/Pizza-as-a-Service-Software.png", caption="Software as a Pizza-Service", use_column_width=True)


    st.video("https://youtu.be/M988_fsOSWo?t=127", start_time=196, end_time=304)

# Vorteile von Cloud Computing
elif menu == "Summary":
    st.title("Vorteile von Cloud Computing")
    st.write("""
    - **Kosteneffizienz:** Reduziert die Kosten für den Kauf und die Wartung von Hardware.
    
    - **Skalierbarkeit:** Ressourcen können je nach Bedarf flexibel hinzugefügt oder reduziert werden.
    
    - **Zugänglichkeit:** Nutzer können von überall und zu jeder Zeit auf Daten und Dienste zugreifen.
    
    - **Sicherheit:** Cloud-Anbieter bieten integrierte Sicherheitslösungen und automatische Backups.
    
    - **Umweltfreundlichkeit:** Durch gemeinsame Nutzung von Ressourcen wird die Energieeffizienz erhöht.
    """)

    st.title("Zusammenfassung und Diskussion")
    st.write("""Cloud Computing ermöglicht es, Rechenressourcen und Dienste über das Internet flexibel zu nutzen, ohne eigene Infrastruktur betreiben zu müssen. 
            """)
    st.write("""Mit Modellen wie IaaS, PaaS und SaaS sowie verschiedenen Cloud-Arten (Private, Public, Hybrid) bietet die Cloud eine große Bandbreite an Lösungen für unterschiedliche Bedürfnisse.
            """)

# eXtollo & neXtollo
elif menu == "Mercedes Platformen":

    st.title("Mercedes Platformen")

    st.subheader("eXtollo")
    st.write("""eXtollo ist unsere eigene, spezielle Version der Microsoft Azure Cloud. Bei Mercedes können wir alle Funktionen von Microsoft Azure nutzen. 
            """)
    st.write("""Um sicherzustellen, dass unsere Daten geschützt bleiben, haben wir den Zugang zur Microsoft Azure Cloud für Unbefugte gesperrt. Deshalb haben wir eine zusätzliche Sicherheitsebene eingeführt und die Microsoft Azure Cloud in „eXtollo“ umbenannt.
            """)
    st.image("data/eXtollo.PNG", caption="eXtollo", use_column_width=True)
    st.write("")  # Leere Zeile als Abstand
    st.subheader("neXtollo")
    st.write("""neXtollo ist die Plattform der nächsten Generation von eXtollo. Mit neXtollo können unsere Kunden ihre eXtollo-Ressourcen über das eXtollo-Portal verwalten. Sie können OLA- und ToU-Dokumente digital unterschreiben, ohne den Aufwand mit E-Mails und Excel-Tabellen.  
            """)
    st.write("""neXtollo bietet viele Self-Service-Funktionen und Automatisierungen, was zu einer schnelleren Bereitstellung führt.
            """)
    st.image("data/neXtollo.PNG", caption="neXtollo", use_column_width=True)
        
             
# Architektur CAD
elif menu == "Architektur CAD":

    st.title("Architektur")
    st.write("""
            """)
    st.image("data/Architektur.PNG", caption="Lakehouse Architektur CAD", use_column_width=True)
      

# Data Lakehouse
elif menu == "Delta-Lake-House":
    
    st.title("Vom Data-Warehouse über Data-Lake zum Delta-Lake-House")
    st.write("""Unternehmen verwenden sowohl Data Lakes als auch Data Warehouses für große Datenmengen aus verschiedenen Quellen.
            """)
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Data-Warehouse")
        st.write("""
                Data Warehouses sind speziell für die Analyse von Daten vorgesehen. Die analytische Verarbeitung innerhalb eines Data Warehouse wird nur für strukturierte Daten durchgeführt mit dem Zweck analysebasierte Daten zu generieren. 
                """)
    with col2:
        st.write("")  # Leere Zeile als Abstand
        st.video("https://www.youtube.com/watch?v=XUa2RHENO-E")
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Data-Lake")
        st.write("""
                Data Lakes speichern eine Fülle an unterschiedlichen, ungefilterten Daten, die später für einen bestimmten Zweck verwendet werden sollen. In einem Data Lake werden Daten aus Unternehmensanwendungen, mobilen Apps, Social Media, IoT-Geräten usw. als Rohdaten erfasst. Die Struktur, Integrität, Auswahl und das Format der verschiedenen Datasets werden zum Zeitpunkt der Analyse von der Person, die die Analyse durchführt, abgeleitet.
                """)
    with col2:
        st.write("")  # Leere Zeile als Abstand
        st.write("")  # Leere Zeile als Abstand
        st.video("https://youtu.be/kJpI1WzFqho")
    
    # Erster Textblock und Bild nebeneinander
    col1, col2 = st.columns([2, 1])  # Linke Spalte breiter (für Text), rechte schmaler (für Bild)
    
    with col1:
        st.subheader("Delta-Lake-House")
        st.write("""
                Delta Lake-Houses sind optimiert für die Speicherung und Analyse von Big Data. Diese skalierbare Lösung entlastet Datenteams von der Pipeline-Wartungsarbeit, vereinfacht Data-Science-Projekte und bietet Datenbenutzern direkten Zugriff auf größere, vielfältigere und aktuellere Datensätze.
                """)
    with col2:
        st.write("")  # Leere Zeile als Abstand
        st.write("")  # Leere Zeile als Abstand
        st.video("https://youtu.be/CfubH7XpRVw")


