Dessa övningar utgår ifrån datasettet weatherAUS som ligger under matplotlib i LearnPoint.


1. Beräkna genomsnittlig 'MaxTemp' för varje plats.

2. Hitta total 'Rainfall' för varje datum över alla platser.

3. Ta reda på om vindhastigheten skiljer sig beroende på vilket håll det blåser. 

4. Hitta genomsnittlig 'MaxTemp', 'MinTemp' och 'Rainfall' för varje månad.

5. Hitta den högst uppmätta vindhastigheten per plats och väderstreck.'Location' och 'WindGustDir' och beräkna maximal 'WindGustSpeed' för varje kombination.

6. Skapa en ny kolumn som beräknar skillnaden mellan 'Pressure9am' och 'Pressure3pm'. Hitta sedan genomsnittlig tryckskillnad för varje 'Location'.

7. Beräkna ett 7-dagars rullande genomsnitt av 'MaxTemp' och 'MinTemp' för en given plats. Kolla upp .rolling().

8. **Korrelationsanalys per Plats**: För varje 'Location', beräkna korrelationskoefficienten mellan 'MaxTemp' och 'Rainfall'. Googla gärna om konceptet och hur man gör i Pandas.