/*package main

import (
	"log"
	"net/http"
)

var robotLatitude float64 = 0.0
var robotLongitude float64 = 0.0

const portNum string = ":9090"

type LocationResponse struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

func main() {
	log.Println("Starting our simple http server.")

	http.HandleFunc("/robot-set-report", robotReportHandler)
	http.HandleFunc("/robot-set-location", robotLocationHandler)

	http.HandleFunc("/robot-get-location", appRobotLocationHandler)

<<<<<<< HEAD
=======
    err := http.ListenAndServe(portNum, nil)
    if err != nil {
        log.Fatal(err)
    }
}*/
package main

import (
	"log"
	"net/http"
)

var robotLatitude float64 = 0.0
var robotLongitude float64 = 0.0

const portNum string = ":9090"

func main() {
	log.Println("Starting our simple http server.")

	//http.HandleFunc("/robot-set-report", robotReportHandler)
	http.HandleFunc("/robot-set-location", robotLocationHandler)

	http.HandleFunc("/robot-get-location", appRobotLocationHandler)

>>>>>>> 56fbf0b9d379bb618a46ba5b44fbc711dbd9d275
	err := http.ListenAndServe(portNum, nil)
	if err != nil {
		log.Fatal(err)
	}
<<<<<<< HEAD
}
=======
}
>>>>>>> 56fbf0b9d379bb618a46ba5b44fbc711dbd9d275
