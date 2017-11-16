SELECT b.hid, a.Hotel_Address, a.Hotel_Name, a.Reviewer_Nationality, a.Negative_Review, a.Review_Total_Negative_Word_Counts, a.Total_Number_of_Reviews,a.Positive_Review,a.Review_Total_Positive_Word_Counts,a.Total_Number_of_Reviews_Reviewer_Has_Given,a.Reviewer_Score,a.Tags,a.days_since_review,a.lat,a.lng FROM hotel_data AS a, Hotel_Entity AS b WHERE a.Hotel_Name = b.Hotel_Name AND a.Hotel_Address = b.Hotel_Address AND a.lat = b.lat AND a.lng = b.lng

CREATE TABLE Temp_Data0 AS SELECT DISTINCT b.hid, a.Hotel_Address, a.Hotel_Name, a.Review_Date, a.Reviewer_Nationality, a.Negative_Review, a.Review_Total_Negative_Word_Counts, a.Total_Number_of_Reviews,a.Positive_Review,a.Review_Total_Positive_Word_Counts,a.Total_Number_of_Reviews_Reviewer_Has_Given,a.Reviewer_Score,a.Tags,a.days_since_review,a.lat,a.lng FROM hotel_data AS a, Hotel_Entity AS b WHERE a.Hotel_Name = b.Hotel_Name AND a.Hotel_Address = b.Hotel_Address AND a.lat = b.lat AND a.lng = b.lng;

CREATE TABLE Review_Entity AS SELECT rid, hid, Positive_Review, Negative_Review, Review_Date, Reviewer_Nationality, Review_Total_Positive_Word_Counts, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags

INSERT INTO Temp_Data

ALTER TABLE Temp_Data ADD [COLUMN] Review_Date CHAR(15)

CREATE TABLE Review_Entity AS SELECT DISTINCT rid, hid, Review_Date, Reviewer_Nationality, Positive_Review, Negative_Review, Review_Total_Positive_Word_Counts, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags FROM Temp_Data0

UPDATE hotel_data INNER JOIN Hotel_Entity ON (hotel_data.Hotel_Name = Hotel_Entity.Hotel_Name AND hotel_data.Hotel_Address = Hotel_Entity.Hotel_Address AND hotel_data.lat=Hotel_Entity.lat AND hotel_data.lng=Hotel_Entity.lng) SET hotel_data.hid = Hotel_Entity.hid;

CREATE TABLE tmp_hotel (rid INT NOT NULL, hid INT NOT NULL, Review_Date char(15), Reviewer_Nationality char(50), Positive_Review longtext, Reviewer_Total_Positive_Word_Counts int,  Negative_Review longtext, Reviewer_Total_Negative_Word_Counts int, Total_Number_of_Reviews_Reviewer_Has_Given int, Reviewer_Score decimal(3,1), Tags longtext, days_since_review int, Hotel_Name char(100), Hotel_Address CHAR(200), lat decimal(10,7), lng decimal(10,7), Total_Number_of_Reviews int, Average_Score decimal(3,1), Additional_Number_of_Scoring int, PRIMARY KEY(rid))

INSERT INTO tmp_hotel(rid, hid, Review_Date, Reviewer_Nationality, Positive_Review, Review_Total_Positive_Word_Counts, Negative_Review, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags, days_since_review, Hotel_Name, Hotel_Address, lat, lng, Total_Number_of_Reviews, Average_Score, Additional_Number_of_Scoring) SELECT hotel_data.rid, Hotel_Entity.hid, hotel_data.Review_Date, hotel_data.Reviewer_Nationality, hotel_data.Positive_Review, hotel_data.Review_Total_Positive_Word_Counts,hotel_data.Negative_Review, hotel_data.Review_Total_Negative_Word_Counts, hotel_data.Total_Number_of_Reviews_Reviewer_Has_Given,hotel_data.Reviewer_Score,hotel_data.Tags,hotel_data.days_since_review,hotel_data.Hotel_Name,hotel_data.Hotel_Address,hotel_data.lat,hotel_data.lng,hotel_data.Total_Number_of_Reviews,hotel_data.Average_Score,hotel_data.Additional_Number_of_Scoring FROM hotel_data LEFT JOIN Hotel_Entity ON (hotel_data.Hotel_Name = Hotel_Entity.Hotel_Name AND hotel_data.Hotel_Address = Hotel_Entity.Hotel_Address AND hotel_data.lat=Hotel_Entity.lat AND hotel_data.lng=Hotel_Entity.lng);

INSERT INTO reviews_review_entity(rid,hid,Review_Date,Reviewer_Nationality, Positive_Review, Negative_Review, Review_Total_Positive_Word_Counts, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags)

INSERT INTO reviews_review_entity(rid,hid_id,Review_Date,Reviewer_Nationality, Positive_Review, Negative_Review, Review_Total_Positive_Word_Counts, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags) SELECT rid,hid AS hid_id,Review_Date,Reviewer_Nationality, Positive_Review, Negative_Review, Review_Total_Positive_Word_Counts, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews_Reviewer_Has_Given, Reviewer_Score, Tags FROM tmp_hotel LIMIT 3;

INSERT INTO reviews_hotel_entity(Hotel_Name, Hotel_Address, lat, lng, Average_Score, Total_Number_of_Reviews, Additional_Number_of_Scoring, hid) SELECT Hotel_Name, Hotel_Address, lat, lng, Average_Score, Total_Number_of_Reviews, Additional_Number_of_Scoring, hid FROM Hotel_Entity;

CREATE TABLE reviews_review_entity (rid INT, hid INT, Review_Date CHAR(15), Reviewer_Nationality CHAR(50), Positive_Review LONGTEXT, Negative_Review LONGTEXT, Review_Total_Positive_Word_Counts INT, Review_Total_Negative_Word_Counts INT, Total_NUmber_of_Reviews_Reviewer_Has_Given INT, Reviewer_Score Decimal(3,1), Tags LONGTEXT);