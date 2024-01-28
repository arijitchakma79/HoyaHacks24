package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type LocationResponse struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

func appRobotLocationHandler(w http.ResponseWriter, r *http.Request) {
	locationResponse := LocationResponse{
		Latitude:  robotLatitude,
		Longitude: robotLongitude,
	}

	jsonData, err := json.Marshal(locationResponse)
	if err != nil {
		log.Println("Error marshaling JSON:", err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")

	w.Write(jsonData)
}
