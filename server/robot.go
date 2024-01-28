package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"encoding/json"
	"context"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type Report struct {
    ID         primitive.ObjectID `json:"_id,omitempty" bson:"_id,omitempty"`
    Latitude   float64            `json:"latitude"`
    Longitude  float64            `json:"longitude"`
    ReportTime string             `json:"reportTime"`
    ReportDate string             `json:"reportDate"`
}


func robotLocationHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	latStr := queryParams.Get("lat")
	longStr := queryParams.Get("long")

	if lat, err := strconv.ParseFloat(latStr, 64); err == nil {
		robotLatitude = lat
	} else {
		log.Fatal(err)
	}

	if long, err := strconv.ParseFloat(longStr, 64); err == nil {
		robotLongitude = long
	} else {
		log.Fatal(err)
	}

	fmt.Printf("Robot's location is recieved at: %f, %f", robotLatitude, robotLongitude)
}


func robotReportHandler(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()

	latStr := queryParams.Get("lat")
	longStr := queryParams.Get("long")
	day := queryParams.Get("day")
	time := queryParams.Get("time")

	var lat, long float64
	var err error

	if lat, err = strconv.ParseFloat(latStr, 64); err != nil {
		log.Fatal(err)
		http.Error(w, "Invalid latitude", http.StatusBadRequest)
		return
	}

	if long, err = strconv.ParseFloat(longStr, 64); err != nil {
		log.Fatal(err)
		http.Error(w, "Invalid longitude", http.StatusBadRequest)
		return
	}

	report := Report{
		Latitude:   lat,
		Longitude:  long,
		ReportTime: time,
		ReportDate: day,
	}

	// Connect to MongoDB
	client, err := connectToMongoDB()
	if err != nil {
		log.Println("Error connecting to MongoDB:", err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}
	defer client.Disconnect(context.Background())

	// Insert report into MongoDB
	err = insertReport(client, "Records", "Records", report)
	if err != nil {
		log.Println("Error inserting report into MongoDB:", err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	fmt.Println("Report is received at location: %f, %f, time: %s %s", lat, long, day, time)
	w.WriteHeader(http.StatusOK)
}

func getAllReports(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")

    // Connect to MongoDB
    client, err := connectToMongoDB()
    if err != nil {
        log.Println("Error connecting to MongoDB:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }
    defer client.Disconnect(context.Background())

    // Get the database and collection
    db := client.Database("Records")
    collection := db.Collection("Records")

    // Find all documents in the collection
    cursor, err := collection.Find(context.Background(), bson.D{})
    if err != nil {
        log.Println("Error fetching reports from MongoDB:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }
    defer cursor.Close(context.Background())

    // Prepare the JSON array for response
    var result []byte
    result = append(result, []byte(`{"report":[`)...)

    for cursor.Next(context.Background()) {
        var report Report
        if err := cursor.Decode(&report); err != nil {
            log.Println("Error decoding report:", err)
            http.Error(w, "Internal Server Error", http.StatusInternalServerError)
            return
        }

        jsonData, err := json.Marshal(report)
        if err != nil {
            log.Println("Error marshaling JSON:", err)
            http.Error(w, "Internal Server Error", http.StatusInternalServerError)
            return
        }

        result = append(result, jsonData...)
        result = append(result, ',')
    }

    if len(result) > len(`{"report":[`) {
        result = result[:len(result)-1]
    }

    result = append(result, []byte("]}")...)
    w.Write(result)
}


func deleteReportHandler(w http.ResponseWriter, r *http.Request) {
    // Parse request parameters
    params := r.URL.Query()
    reportID := params.Get("reportID")

    // Convert reportID to ObjectID
    objectID, err := primitive.ObjectIDFromHex(reportID)
    if err != nil {
        http.Error(w, "Invalid reportID", http.StatusBadRequest)
        return
    }

    // Prepare filter to find the report by ID
    filter := bson.M{"_id": objectID}

    // Connect to MongoDB
    client, err := connectToMongoDB()
    if err != nil {
        log.Println("Error connecting to MongoDB:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }
    defer client.Disconnect(context.Background())

    // Get the database and collection
    db := client.Database("YourDBName")
    collection := db.Collection("YourCollectionName")

    // Delete the report
    _, err = collection.DeleteOne(context.Background(), filter)
    if err != nil {
        log.Println("Error deleting report from MongoDB:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }

    // Send success response
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("Report deleted successfully"))
}

