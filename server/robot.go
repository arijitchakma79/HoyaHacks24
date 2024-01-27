package main

import (
    "net/http" 
	"strconv"
	"log"
	"fmt"
)

func robotReportHandler(w http.ResponseWriter, r *http.Request) {
	//queryParams := r.URL.Query()

	//latStr := queryParams.Get("lat")
	//longStr := queryParams.Get("long")

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

	fmt.Printf("Robot's location is recieved at: %f, %f\n", robotLatitude, robotLongitude)
}
/*
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

var robotLatitude float64 = 0.0
var robotLongitude float64 = 0.0

type LocationResponse struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

func robotLocationHandler(w http.ResponseWriter, r *http.Request) {
	var location LocationResponse
	err := json.NewDecoder(r.Body).Decode(&location)
	if err != nil {
		log.Println("Error decoding JSON:", err)
		http.Error(w, "Bad Request", http.StatusBadRequest)
		return
	}

	robotLatitude = location.Latitude
	robotLongitude = location.Longitude

	fmt.Fprintf(w, "Robot location updated successfully")
}*/