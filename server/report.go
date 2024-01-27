// report.go
package main

import (
	"encoding/json"
	"log"
	"net/http"
	"time"
)

type reportNotification struct {
	ReportID   int    `json:"reportID"`
	Latitude   float64 `json:"latitude"`
	Longitude  float64 `json:"longitude"`
	ReportTime string  `json:"reportTime"`
	ReportDate string  `json:"reportDate"`
}


func GetReportNotification(w http.ResponseWriter, r *http.Request) {

	currentTime := time.Now()

	reportID++
	reportNotification := reportNotification{
		ReportID:   reportID,
		Latitude:   robotLatitude,
		Longitude:  robotLongitude,
		ReportTime: currentTime.Format("15:04:05"),
		ReportDate: currentTime.Format("Mon"),
	}

	jsonData, err := json.Marshal(reportNotification)
	if err != nil {
		log.Println("Error marshaling JSON:", err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonData)
}
