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

	fmt.Printf("Robot's location is recieved at: %f, %f", robotLatitude, robotLongitude)
}