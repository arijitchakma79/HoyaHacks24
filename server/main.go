package main

import (
	"log"
	"net/http"
)

var (
	robotLatitude  float64 = 0.0
	robotLongitude float64 = 0.0
	reportID       int     = 0
	reports        []Report
)

const portNum string = ":9090"

func main() {
	log.Println("Starting our simple http server.")

	// Robot
	http.HandleFunc("/robot-set-report", robotReportHandler)
	http.HandleFunc("/robot-set-location", robotLocationHandler)
	http.HandleFunc("/robot-get-all-reports", getAllReports)

	// App
	http.HandleFunc("/robot-get-location", appRobotLocationHandler)
	http.HandleFunc("/robot-get-report", GetReportNotification)


	err := http.ListenAndServe(portNum, nil)
	if err != nil {
		log.Fatal(err)
	}

}
