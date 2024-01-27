package main

import (
    "fmt" 
    "net/http" 
)

func appRobotLocationHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Robot is at %f, %f", robotLatitude, robotLongitude)
}