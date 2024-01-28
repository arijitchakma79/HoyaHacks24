package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"encoding/json"
)

type Report struct {
	Latitude   float64 `json:"latitude"`
	Longitude  float64 `json:"longitude"`
	ReportTime string  `json:"reportTime"`
	ReportDate string  `json:"reportDate"`
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
	}

	if long, err = strconv.ParseFloat(longStr, 64); err != nil {
		log.Fatal(err)
	}

	report := Report{
		Latitude:   lat,
		Longitude:  long,
		ReportTime: time,
		ReportDate: day,
	}

	reports = append(reports, report)
	fmt.Println(reports)
	fmt.Println(len(reports))
	fmt.Println("Report is received at location: %f, %f, time: %s %s", lat, long, day, time)
}


func getAllReports(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var result []byte
	result = append(result, []byte(`{"report":[`)...)

	for t := 0; t < len(reports); t++ {
		jsonData, err := json.Marshal(reports[t])
		if err != nil {
			log.Println("Error marshaling JSON:", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}

		result = append(result, jsonData...)
		if t < len(reports)-1 {
			result = append(result, ',')
		}
	}

	result = append(result, []byte("]}")...)
	w.Write(result)
}
