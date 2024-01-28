package main

import (
	"context"
	"log"
	"net/http"
	"github.com/go-chi/chi"
)

var (
	robotLatitude  float64 = 0.0
	robotLongitude float64 = 0.0
	reportID       int     = 0
)

const portNum string = ":9090"

func main() {
	// Connect to MongoDB
	client, err := connectToMongoDB()
	if err != nil {
		log.Fatal("Error connecting to MongoDB:", err)
		return
	}
	defer client.Disconnect(context.Background())

	log.Println("Starting our simple http server.")

	r := chi.NewRouter()

	// Robot
	r.HandleFunc("/robot-set-report", robotReportHandler)
	r.HandleFunc("/robot-set-location", robotLocationHandler)
	r.HandleFunc("/robot-get-all-reports", getAllReports)
	r.HandleFunc("/delete-report/{id}", deleteReportHandler)

	// App
	r.HandleFunc("/robot-get-location", appRobotLocationHandler)
	r.HandleFunc("/robot-get-report", GetReportNotification)

	err = http.ListenAndServe(portNum, r)
	if err != nil {
		log.Fatal(err)
	}
}
