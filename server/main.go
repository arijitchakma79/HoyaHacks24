package main

import (
	"log"
	"net/http"
)

var robotLatitude float64 = 0.0
var robotLongitude float64 = 0.0
var reportID int = 0

const portNum string = ":9090"

func main() {
	log.Println("Starting our simple http server.")

	//http.HandleFunc("/robot-set-report", robotReportHandler)
	http.HandleFunc("/robot-set-location", robotLocationHandler)

	http.HandleFunc("/robot-get-location", appRobotLocationHandler)

	http.HandleFunc("/robot-get-report", GetReportNotification)

	err := http.ListenAndServe(portNum, nil)
	if err != nil {
		log.Fatal(err)
	}
}
